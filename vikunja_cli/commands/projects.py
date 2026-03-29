"""
projects commands — CRUD for Vikunja projects.

  vk projects list [--search TEXT] [--archived]
  vk projects get ID
  vk projects add TITLE [--desc TEXT] [--parent ID]
  vk projects update ID [--title TEXT] [--desc TEXT]
  vk projects delete ID [--yes]
"""
from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console

from vikunja_cli.client import get_client
from vikunja_cli.formatters import print_projects, print_project_detail, err_console

from vikunja_client.api.project import (
    get_projects,
    get_projects_id,
    put_projects,
    post_projects_id,
    delete_projects_id,
)
from vikunja_client.models.models_project import ModelsProject
from vikunja_client.types import UNSET

app = typer.Typer(no_args_is_help=True)
console = Console()


def _check_error(result: object, action: str) -> None:
    """Exit with an error message if the API call failed."""
    if result is None:
        err_console.print(f"[red]✗[/red] {action}: empty response from server")
        raise typer.Exit(1)
    if hasattr(result, "message") and not hasattr(result, "id"):
        err_console.print(f"[red]✗[/red] {action}: {result.message}")
        raise typer.Exit(1)


@app.command("list")
def list_projects(
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Filter by name"),
    archived: bool = typer.Option(False, "--archived", help="Include archived projects"),
    limit: int = typer.Option(100, "--limit", "-n", help="Max results"),
) -> None:
    """List all projects you have access to."""
    client = get_client()
    result = get_projects.sync(
        client=client,
        s=search if search else UNSET,
        is_archived=archived if archived else UNSET,
        per_page=limit,
    )

    if result is None or not isinstance(result, list):
        err_console.print(f"[red]✗[/red] Failed to fetch projects: {getattr(result, 'message', 'unknown error')}")
        raise typer.Exit(1)

    if not result:
        console.print("[dim]No projects found.[/dim]")
        return

    print_projects(result)


@app.command("get")
def get_project(
    project_id: int = typer.Argument(..., help="Project ID"),
) -> None:
    """Show details of a single project."""
    client = get_client()
    result = get_projects_id.sync(id=project_id, client=client)
    _check_error(result, f"get project {project_id}")
    print_project_detail(result)


@app.command("add")
def add_project(
    title: str = typer.Argument(..., help="Project title"),
    desc: Optional[str] = typer.Option(None, "--desc", "-d", help="Project description"),
    parent: Optional[int] = typer.Option(None, "--parent", "-p", help="Parent project ID"),
) -> None:
    """Create a new project."""
    client = get_client()

    project = ModelsProject(
        title=title,
        description=desc if desc else UNSET,
        parent_project_id=parent if parent else UNSET,
    )

    result = put_projects.sync(body=project, client=client)
    _check_error(result, "create project")
    console.print(f"[green]✓[/green] Project created: #{result.id} — {result.title}")


@app.command("update")
def update_project(
    project_id: int = typer.Argument(..., help="Project ID to update"),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New title"),
    desc: Optional[str] = typer.Option(None, "--desc", "-d", help="New description"),
    archived: Optional[bool] = typer.Option(None, "--archived/--active", help="Archive or restore the project"),
) -> None:
    """Update an existing project's fields."""
    client = get_client()

    # Fetch current state to preserve untouched fields
    current = get_projects_id.sync(id=project_id, client=client)
    _check_error(current, f"fetch project {project_id}")

    updated = ModelsProject(
        id=project_id,
        title=title if title is not None else current.title,
        description=desc if desc is not None else current.description,
        is_archived=archived if archived is not None else current.is_archived,
    )

    result = post_projects_id.sync(id=project_id, body=updated, client=client)
    _check_error(result, f"update project {project_id}")
    console.print(f"[green]✓[/green] Project #{result.id} updated")


@app.command("delete")
def delete_project(
    project_id: int = typer.Argument(..., help="Project ID to delete"),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt"),
) -> None:
    """Permanently delete a project and all its tasks."""
    if not yes:
        typer.confirm(
            f"Delete project #{project_id} and ALL its tasks? This cannot be undone.",
            abort=True,
        )

    client = get_client()
    result = delete_projects_id.sync(id=project_id, client=client)

    if result is None:
        err_console.print(f"[red]✗[/red] Failed to delete project #{project_id}")
        raise typer.Exit(1)
    if hasattr(result, "code") and result.code and result.code != 0:
        err_console.print(f"[red]✗[/red] {result.message}")
        raise typer.Exit(1)

    console.print(f"[green]✓[/green] Project #{project_id} deleted")
