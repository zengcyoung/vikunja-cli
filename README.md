# vikunja-cli

A command-line tool for [Vikunja](https://vikunja.io) — manage tasks and projects from your terminal.

Built with [Typer](https://typer.tiangolo.com) + [Rich](https://rich.readthedocs.io), with a fully type-safe API client auto-generated from the Vikunja OpenAPI spec.

---

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) — Python package manager
- `swagger2openapi` (Node.js) — only needed if regenerating the client

---

## Installation

```bash
cd ~/vikunja-cli
uv sync
```

This creates `.venv/` and installs all dependencies. The `vk` command is available at `.venv/bin/vk` and symlinked to `~/.local/bin/vk`.

---

## Configuration

Create an API token in your Vikunja instance: **Settings → API Tokens**

Then configure the CLI:

```bash
vk auth login
```

Or write the config file manually:

```bash
mkdir -p ~/.config/vikunja_cli
cat > ~/.config/vikunja_cli/config.env << 'EOF'
VIKUNJA_BASE_URL=https://your.vikunja.instance
VIKUNJA_API_TOKEN=your_api_token_here
EOF
chmod 600 ~/.config/vikunja_cli/config.env
```

Environment variables `VIKUNJA_BASE_URL` and `VIKUNJA_API_TOKEN` override the config file.

---

## Usage

### Auth

```bash
vk auth login    # Interactive setup: base URL + API token
vk auth show     # Show current config (token masked)
```

### Tasks

```bash
# List tasks (all projects)
vk tasks list

# Filter by project, keyword, or status
vk tasks list --project 3
vk tasks list --search "deploy" --undone
vk tasks list --limit 100

# Show full detail
vk tasks get 42

# Create a task
vk tasks add 3 "Write release notes"
vk tasks add 3 "Deploy to staging" --due 2026-04-01 --priority 3 --desc "Use the blue-green flow"

# Update fields (only specified fields change)
vk tasks update 42 --title "New title"
vk tasks update 42 --due 2026-04-05 --priority 5
vk tasks update 42 --done        # mark done
vk tasks update 42 --undone      # reopen

# Quick-complete
vk tasks done 42

# Delete
vk tasks delete 42          # prompts for confirmation
vk tasks delete 42 --yes    # skip prompt
```

### Projects

```bash
# List
vk projects list
vk projects list --search "work"
vk projects list --archived

# Show
vk projects get 3

# Create
vk projects add "My Project"
vk projects add "Sub-project" --parent 3 --desc "Description here"

# Update
vk projects update 3 --title "Renamed"
vk projects update 3 --archived    # archive
vk projects update 3 --active      # restore

# Delete (also deletes all tasks — confirms before acting)
vk projects delete 3
vk projects delete 3 --yes
```

---

## Priority Reference

| Value | Label    |
|-------|----------|
| 0     | (none)   |
| 1     | low      |
| 2     | medium   |
| 3     | high     |
| 4     | urgent   |
| 5     | DO NOW   |

---

## Project Structure

```
vikunja-cli/
├── vikunja_client/        # Auto-generated API client (do not edit manually)
│   ├── api/               # One module per endpoint group
│   └── models/            # Pydantic models for all API types
├── vikunja_cli/           # CLI source
│   ├── main.py            # Typer app root
│   ├── client.py          # Authenticated client factory
│   ├── config.py          # Config file read/write
│   ├── formatters.py      # Rich table output helpers
│   └── commands/
│       ├── auth.py        # vk auth *
│       ├── tasks.py       # vk tasks *
│       └── projects.py    # vk projects *
├── openapi.json           # Swagger 2.0 spec (source of truth)
├── openapi3.json          # OpenAPI 3.0 spec (converted, used for codegen)
├── openapi-python-client.yaml  # Codegen config
└── pyproject.toml
```

---

## Regenerating the API Client

If the Vikunja API spec changes:

```bash
# 1. Fetch the latest spec from your instance
curl -s https://your.vikunja.instance/api/v1/docs.json -o openapi.json

# 2. Convert Swagger 2.0 → OpenAPI 3.0
swagger2openapi openapi.json -o openapi3.json

# 3. Regenerate vikunja_client/
uv run openapi-python-client generate \
  --path openapi3.json \
  --meta none \
  --output-path vikunja_client \
  --config openapi-python-client.yaml
```

`vikunja_client/` is entirely generated — do not edit it by hand.

---

## Development

```bash
# Run directly without installing
uv run vk tasks list

# Add a runtime dependency
uv add some-package

# Add a dev-only dependency
uv add --group dev some-dev-tool
```
