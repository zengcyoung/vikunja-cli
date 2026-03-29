#!/usr/bin/env python3
"""
Migrate pending tasks from taskwarrior sqlite conflict files into Vikunja.
Maps taskwarrior projects to Vikunja project IDs, creating new ones as needed.
"""
import json
import sqlite3
import httpx
import os
from datetime import datetime, timezone
from pathlib import Path

# --- Config ---
BASE_URL = os.environ.get("VIKUNJA_BASE_URL", "").rstrip("/") + "/api/v1"
TOKEN = os.environ.get("VIKUNJA_API_TOKEN", "")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def api_get(path):
    r = httpx.get(f"{BASE_URL}{path}", headers=HEADERS, verify=False)
    r.raise_for_status()
    return r.json()


def api_put(path, body):
    r = httpx.put(f"{BASE_URL}{path}", headers=HEADERS, json=body, verify=False)
    r.raise_for_status()
    return r.json()


def load_merged_tasks():
    """Load and merge tasks from both conflict sqlite files, pending only."""
    conflict_files = [
        Path.home() / ".task/taskchampion.sqlite3.conflict2",
        Path.home() / ".task/taskchampion.sqlite3.conflict1",  # conflict1 wins
    ]
    merged = {}
    for path in conflict_files:
        if not path.exists():
            continue
        conn = sqlite3.connect(str(path))
        rows = conn.execute("SELECT uuid, data FROM tasks").fetchall()
        conn.close()
        for uuid, data_str in rows:
            try:
                d = json.loads(data_str)
                d["uuid"] = uuid
                merged[uuid] = d
            except Exception:
                pass
    # Only pending tasks
    return [t for t in merged.values() if t.get("status") == "pending"]


def get_or_create_project(name, existing):
    """Return project ID for name, creating it if not found."""
    for p in existing:
        if p["title"].lower() == name.lower():
            return p["id"]
    print(f"  Creating project: {name}")
    result = api_put("/projects", {"title": name})
    return result["id"]


def fmt_due(epoch_str):
    """Convert taskwarrior epoch string to ISO 8601."""
    if not epoch_str:
        return None
    try:
        dt = datetime.fromtimestamp(int(epoch_str), tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return None


def main():
    print("Loading taskwarrior tasks...")
    tasks = load_merged_tasks()
    print(f"Found {len(tasks)} pending tasks to migrate\n")

    print("Fetching existing Vikunja projects...")
    existing_projects = api_get("/projects")
    for p in existing_projects:
        print(f"  [{p['id']}] {p['title']}")

    # Build project map: taskwarrior project name → vikunja project ID
    # Tasks with no project go to Inbox (id=1)
    project_map = {"": 1, "(none)": 1}
    tw_projects = set(t.get("project", "") for t in tasks if t.get("project"))
    print(f"\nTaskwarrior projects to map: {tw_projects}")
    for proj_name in tw_projects:
        project_map[proj_name] = get_or_create_project(proj_name, existing_projects)
    print(f"Project map: {project_map}\n")

    # Import tasks
    success = 0
    skipped = 0
    for task in tasks:
        desc = task.get("description", "").strip()
        if not desc:
            skipped += 1
            continue

        proj_name = task.get("project", "")
        project_id = project_map.get(proj_name, 1)
        due_date = fmt_due(task.get("due"))

        body = {"title": desc}
        if due_date:
            body["due_date"] = due_date

        try:
            result = api_put(f"/projects/{project_id}/tasks", body)
            due_str = f" due={due_date}" if due_date else ""
            print(f"  ✓ [{project_id}/{proj_name or 'Inbox'}] {desc[:60]}{due_str}")
            success += 1
        except Exception as e:
            print(f"  ✗ FAILED: {desc[:60]} — {e}")
            skipped += 1

    print(f"\nDone: {success} imported, {skipped} skipped")


if __name__ == "__main__":
    main()
