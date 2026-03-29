"""
auth commands — configure and inspect credentials.
"""
from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from vikunja_cli.config import CONFIG_FILE, get_base_url, get_token, save_config
from vikunja_cli.client import get_client

# Verify connectivity by hitting /api/v1/info (no auth required)
from vikunja_client.api.service import get_info

app = typer.Typer(no_args_is_help=True)
console = Console()
err_console = Console(stderr=True)


@app.command()
def login(
    base_url: str = typer.Option(..., prompt="Vikunja base URL (e.g. https://your.instance)", help="Base URL of your Vikunja instance"),
    token: str = typer.Option(..., prompt="API Token", hide_input=True, help="API token from Settings > API Tokens"),
) -> None:
    """Save credentials to ~/.config/vikunja_cli/config.env."""
    save_config(base_url.rstrip("/"), token)
    console.print(f"[green]✓[/green] Credentials saved to {CONFIG_FILE}")

    # Quick connectivity test
    client = get_client(base_url.rstrip("/"), token)
    result = get_info.sync(client=client)
    if result and hasattr(result, "version"):
        console.print(f"[green]✓[/green] Connected — Vikunja {result.version}")
    else:
        console.print("[yellow]⚠[/yellow] Saved, but could not verify connection.")


@app.command()
def show() -> None:
    """Show the currently configured credentials (token masked)."""
    url = get_base_url()
    token = get_token()
    if url:
        console.print(f"Base URL: [bold]{url}[/bold]")
    else:
        console.print("[yellow]Base URL: not set[/yellow]")
    if token:
        masked = token[:6] + "..." + token[-4:] if len(token) > 10 else "****"
        console.print(f"Token:    [bold]{masked}[/bold]")
    else:
        console.print("[yellow]Token: not set[/yellow]")
