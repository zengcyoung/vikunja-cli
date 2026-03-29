"""
Vikunja CLI - Configuration management.
Reads credentials from ~/.config/vikunja_cli/config.env
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

CONFIG_DIR = Path.home() / ".config" / "vikunja_cli"
CONFIG_FILE = CONFIG_DIR / "config.env"


def _read_env_file(path: Path) -> dict[str, str]:
    """Parse a simple KEY=value env file, ignoring comments and blank lines."""
    result: dict[str, str] = {}
    if not path.exists():
        return result
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def load_config() -> dict[str, str]:
    """Load config from file, then override with environment variables."""
    cfg = _read_env_file(CONFIG_FILE)
    # Environment variables always win
    for key in ("VIKUNJA_BASE_URL", "VIKUNJA_API_TOKEN"):
        val = os.environ.get(key)
        if val:
            cfg[key] = val
    return cfg


def get_base_url() -> Optional[str]:
    return load_config().get("VIKUNJA_BASE_URL")


def get_token() -> Optional[str]:
    return load_config().get("VIKUNJA_API_TOKEN")


def save_config(base_url: str, token: str) -> None:
    """Write credentials to the config file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(
        f"VIKUNJA_BASE_URL={base_url}\nVIKUNJA_API_TOKEN={token}\n"
    )
    CONFIG_FILE.chmod(0o600)
