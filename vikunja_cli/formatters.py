"""
Vikunja CLI - Rich output formatters.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
err_console = Console(stderr=True)


def _fmt_date(val: Any) -> str:
    """Format an ISO datetime string to a short human-readable form. Suppress zero/epoch dates."""
    if not val:
        return ""
    try:
        if isinstance(val, str):
            dt = datetime.fromisoformat(val.replace("Z", "+00:00"))
        else:
            dt = val
        # Vikunja uses 0001-01-01 as "not set"
        if dt.year <= 1:
            return ""
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(val)


def _priority_label(p: int) -> str:
    return {0: "", 1: "low", 2: "medium", 3: "high", 4: "urgent", 5: "DO NOW"}.get(p, str(p))


def print_tasks(tasks: list[Any], title: str = "Tasks") -> None:
    """Render a list of task objects as a Rich table."""
    table = Table(title=title, box=box.ROUNDED, show_lines=False)
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", min_width=30)
    table.add_column("Done", width=5)
    table.add_column("Priority", width=9)
    table.add_column("Due", width=17)
    table.add_column("Labels")

    for task in tasks:
        done = "✓" if getattr(task, "done", False) else ""
        priority = _priority_label(getattr(task, "priority", 0) or 0)
        due = _fmt_date(getattr(task, "due_date", None))
        labels_raw = getattr(task, "labels", None) or []
        labels = ", ".join(
            getattr(lb, "title", str(lb)) for lb in labels_raw if lb
        )
        table.add_row(
            str(task.id),
            task.title or "",
            done,
            priority,
            due,
            labels,
        )

    console.print(table)


def print_task_detail(task: Any) -> None:
    """Print full details of a single task."""
    console.print(f"\n[bold]#{task.id} — {task.title}[/bold]")
    console.print(f"  Done:        {'Yes' if getattr(task, 'done', False) else 'No'}")
    console.print(f"  Priority:    {_priority_label(getattr(task, 'priority', 0) or 0)}")
    due = _fmt_date(getattr(task, "due_date", None))
    if due:
        console.print(f"  Due:         {due}")
    created = _fmt_date(getattr(task, "created", None))
    if created:
        console.print(f"  Created:     {created}")
    updated = _fmt_date(getattr(task, "updated", None))
    if updated:
        console.print(f"  Updated:     {updated}")
    desc = getattr(task, "description", None)
    if desc:
        console.print(f"  Description:\n    {desc}")
    labels_raw = getattr(task, "labels", None) or []
    if labels_raw:
        labels = ", ".join(getattr(lb, "title", str(lb)) for lb in labels_raw if lb)
        console.print(f"  Labels:      {labels}")
    console.print()


def print_projects(projects: list[Any]) -> None:
    """Render a list of projects as a Rich table."""
    table = Table(title="Projects", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", min_width=25)
    table.add_column("Description")
    table.add_column("Owner")

    for p in projects:
        owner_obj = getattr(p, "owner", None)
        owner = ""
        if owner_obj:
            owner = getattr(owner_obj, "username", None) or getattr(owner_obj, "name", "") or ""
        table.add_row(
            str(p.id),
            p.title or "",
            (p.description or "")[:60],
            owner,
        )

    console.print(table)


def print_project_detail(p: Any) -> None:
    """Print full details of a single project."""
    console.print(f"\n[bold]#{p.id} — {p.title}[/bold]")
    if p.description:
        console.print(f"  Description: {p.description}")
    owner_obj = getattr(p, "owner", None)
    if owner_obj:
        owner = getattr(owner_obj, "username", None) or getattr(owner_obj, "name", "") or ""
        if owner:
            console.print(f"  Owner:       {owner}")
    created = _fmt_date(getattr(p, "created", None))
    if created:
        console.print(f"  Created:     {created}")
    console.print()
