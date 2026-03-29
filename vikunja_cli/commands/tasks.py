"""
tasks commands — CRUD for Vikunja tasks.

  vk tasks list [--project ID] [--search TEXT] [--undone]
  vk tasks get ID
  vk tasks add PROJECT_ID TITLE [--desc TEXT] [--due YYYY-MM-DD] [--priority 0-5]
  vk tasks update ID [--title TEXT] [--desc TEXT] [--due YYYY-MM-DD] [--priority 0-5]
  vk tasks done ID
  vk tasks delete ID [--yes]
"""
from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console

from vikunja_cli.client import get_client
from vikunja_cli.formatters import print_tasks, print_task_detail, err_console

from vikunja_client.api.task import (
    get_tasks,
    get_tasks_id,
    put_projects_id_tasks,
    post_tasks_id,
    delete_tasks_id,
)
from vikunja_client.models.models_task import ModelsTask
from vikunja_client.types import UNSET

app = typer.Typer(no_args_is_help=True)
console = Console()


def _check_error(result: object, action: str) -> None:
    """Exit with a message if the API returned an error."""
    if result is None:
        err_console.print(f"[red]✗[/red] {action}: empty response from server")
        raise typer.Exit(1)
    # WebHTTPError and ModelsMessage both have a `message` attribute but not `id`
    if hasattr(result, "message") and not hasattr(result, "id"):
        err_console.print(f"[red]✗[/red] {action}: {result.message}")
        raise typer.Exit(1)


@app.command("list")
def list_tasks(
    project: Optional[int] = typer.Option(None, "--project", "-p", help="Filter by project ID"),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search by title"),
    undone: bool = typer.Option(False, "--undone", help="Show only undone tasks"),
    limit: int = typer.Option(50, "--limit", "-n", help="Max number of tasks to fetch"),
) -> None:
    """List tasks across all projects, or filtered by project."""
    client = get_client()

    filter_parts = []
    if project:
        filter_parts.append(f"project_id = {project}")
    if undone:
        filter_parts.append("done = false")

    filter_str = " && ".join(filter_parts) if filter_parts else UNSET

    result = get_tasks.sync(
        client=client,
        s=search if search else UNSET,
        filter_=filter_str,
        per_page=limit,
    )

    if result is None or (hasattr(result, "message") and not isinstance(result, list)):
        err_console.print(f"[red]✗[/red] Failed to fetch tasks: {getattr(result, 'message', 'unknown error')}")
        raise typer.Exit(1)

    tasks_list = result if isinstance(result, list) else []

    if not tasks_list:
        console.print("[dim]No tasks found.[/dim]")
        return

    title = "Tasks"
    if project:
        title = f"Tasks in project #{project}"
    if search:
        title += f' matching "{search}"'

    print_tasks(tasks_list, title=title)


@app.command("get")
def get_task(
    task_id: int = typer.Argument(..., help="Task ID"),
) -> None:
    """Show full details of a single task."""
    client = get_client()
    result = get_tasks_id.sync(id=task_id, client=client)
    _check_error(result, f"get task {task_id}")
    print_task_detail(result)


@app.command("add")
def add_task(
    project_id: int = typer.Argument(..., help="Project ID to add the task to"),
    title: str = typer.Argument(..., help="Task title"),
    desc: Optional[str] = typer.Option(None, "--desc", "-d", help="Task description"),
    due: Optional[str] = typer.Option(None, "--due", help="Due date (YYYY-MM-DD or ISO datetime)"),
    priority: int = typer.Option(0, "--priority", "-P", min=0, max=5, help="Priority 0–5 (0=none, 5=do now)"),
) -> None:
    """Create a new task in a project."""
    client = get_client()

    due_value: str | type(UNSET) = UNSET
    if due:
        # Normalise to RFC3339 / ISO 8601 with time component
        if "T" not in due:
            due_value = due + "T00:00:00Z"
        else:
            due_value = due

    task = ModelsTask(
        title=title,
        description=desc if desc else UNSET,
        due_date=due_value,
        priority=priority if priority else UNSET,
    )

    result = put_projects_id_tasks.sync(id=project_id, body=task, client=client)
    _check_error(result, "create task")

    console.print(f"[green]✓[/green] Task created: #{result.id} — {result.title}")


@app.command("update")
def update_task(
    task_id: int = typer.Argument(..., help="Task ID to update"),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New title"),
    desc: Optional[str] = typer.Option(None, "--desc", "-d", help="New description"),
    due: Optional[str] = typer.Option(None, "--due", help="New due date (YYYY-MM-DD)"),
    priority: Optional[int] = typer.Option(None, "--priority", "-P", min=0, max=5, help="Priority 0–5"),
    done: Optional[bool] = typer.Option(None, "--done/--undone", help="Mark as done or undone"),
) -> None:
    """Update fields on an existing task."""
    client = get_client()

    # Fetch current state first so we don't accidentally wipe fields
    current = get_tasks_id.sync(id=task_id, client=client)
    _check_error(current, f"fetch task {task_id}")

    due_value = UNSET
    if due:
        due_value = due + "T00:00:00Z" if "T" not in due else due

    updated = ModelsTask(
        id=task_id,
        title=title if title is not None else current.title,
        description=desc if desc is not None else current.description,
        due_date=due_value if due else current.due_date,
        priority=priority if priority is not None else current.priority,
        done=done if done is not None else current.done,
        percent_done=100.0 if done is True else (0.0 if done is False else current.percent_done),
    )

    result = post_tasks_id.sync(id=task_id, body=updated, client=client)
    _check_error(result, f"update task {task_id}")
    console.print(f"[green]✓[/green] Task #{result.id} updated")


@app.command("done")
def mark_done(
    task_id: int = typer.Argument(..., help="Task ID to mark as done"),
) -> None:
    """Mark a task as done (percent_done = 100)."""
    client = get_client()

    current = get_tasks_id.sync(id=task_id, client=client)
    _check_error(current, f"fetch task {task_id}")

    updated = ModelsTask(
        id=task_id,
        title=current.title,
        done=True,
        percent_done=100.0,
    )

    result = post_tasks_id.sync(id=task_id, body=updated, client=client)
    _check_error(result, f"complete task {task_id}")
    console.print(f"[green]✓[/green] Task #{task_id} marked as done")


@app.command("delete")
def delete_task(
    task_id: int = typer.Argument(..., help="Task ID to delete"),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt"),
) -> None:
    """Permanently delete a task."""
    if not yes:
        typer.confirm(f"Delete task #{task_id}?", abort=True)

    client = get_client()
    result = delete_tasks_id.sync(id=task_id, client=client)

    # delete returns a message on success too
    if result is None:
        err_console.print(f"[red]✗[/red] Failed to delete task #{task_id}")
        raise typer.Exit(1)
    if hasattr(result, "code") and result.code and result.code != 0:
        err_console.print(f"[red]✗[/red] {result.message}")
        raise typer.Exit(1)

    console.print(f"[green]✓[/green] Task #{task_id} deleted")
