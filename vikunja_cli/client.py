"""
Vikunja CLI - Authenticated API client factory.
"""
from __future__ import annotations

from typing import Optional

import httpx
import typer

from vikunja_cli.config import get_base_url, get_token
from vikunja_client import AuthenticatedClient


def get_client(base_url: Optional[str] = None, token: Optional[str] = None) -> AuthenticatedClient:
    """
    Build an authenticated Vikunja API client.

    Reads credentials from ~/.config/vikunja_cli/config.env unless overridden.
    Exits with a helpful message if credentials are missing.
    """
    url = base_url or get_base_url()
    tok = token or get_token()

    if not url:
        typer.echo(
            "[error] VIKUNJA_BASE_URL not set. Run `vk auth login` or set it in "
            "~/.config/vikunja_cli/config.env",
            err=True,
        )
        raise typer.Exit(1)

    if not tok:
        typer.echo(
            "[error] VIKUNJA_API_TOKEN not set. Run `vk auth login` or set it in "
            "~/.config/vikunja_cli/config.env",
            err=True,
        )
        raise typer.Exit(1)

    url = url.rstrip("/")
    # The generated client uses paths like /tasks, /projects, etc.
    # Vikunja serves everything under /api/v1, so we append it here.
    if not url.endswith("/api/v1"):
        url = url + "/api/v1"
    return AuthenticatedClient(base_url=url, token=tok, verify_ssl=False)
