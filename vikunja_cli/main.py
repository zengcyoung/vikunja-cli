"""
Vikunja CLI — main entry point.

Commands:
  auth      Configure credentials (login / show)
  tasks     CRUD operations on tasks
  projects  CRUD operations on projects
"""
from __future__ import annotations

import typer

from vikunja_cli.commands import auth, tasks, projects

app = typer.Typer(
    name="vk",
    help="Vikunja task manager CLI",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)

app.add_typer(auth.app,     name="auth",     help="Manage credentials")
app.add_typer(tasks.app,    name="tasks",    help="Task CRUD (list, add, update, done, delete)")
app.add_typer(projects.app, name="projects", help="Project CRUD (list, add, update, delete)")

if __name__ == "__main__":
    app()
