---
name: vikunja
description: "Manage Vikunja tasks and projects via the local `vk` CLI. Use when the user asks to list, create, update, complete, or delete tasks or projects in Vikunja. Triggers on: 'add a task', 'show my tasks', 'create a project', 'mark task done', 'what's on my list', 'vikunja', or any task management request that implies Vikunja. Credentials stored in ~/.config/vikunja_cli/config.env (never printed)."
metadata:
  {"openclaw": {"emoji": "✅", "requires": {"bins": ["vk"]}}}
---

# Vikunja Skill

Manage tasks and projects via the `vk` CLI at `~/vikunja-cli`.

## Credentials

Stored in `~/.config/vikunja_cli/config.env` — never print or log.

```
VIKUNJA_BASE_URL=https://your.vikunja.instance
VIKUNJA_API_TOKEN=your_token
```

Set up with: `vk auth login`

## Tasks

```bash
vk tasks list                              # all tasks
vk tasks list --project ID                 # filter by project
vk tasks list --search "keyword" --undone  # search + filter undone
vk tasks get ID                            # full detail
vk tasks add PROJECT_ID "title"            # create
vk tasks add PROJECT_ID "title" \
  --due 2026-04-01 --priority 3 \
  --desc "notes here"
vk tasks update ID --title "new" --due 2026-04-05 --priority 5
vk tasks update ID --done                  # mark done
vk tasks update ID --undone                # reopen
vk tasks done ID                           # quick-complete
vk tasks delete ID --yes                   # delete (no prompt)
```

## Projects

```bash
vk projects list                           # list all
vk projects list --search "keyword"
vk projects get ID
vk projects add "Project Name" --desc "..." --parent PARENT_ID
vk projects update ID --title "New Name"
vk projects update ID --archived           # archive
vk projects update ID --active             # restore
vk projects delete ID --yes                # deletes all tasks too!
```

## Priority Values

0 = none · 1 = low · 2 = medium · 3 = high · 4 = urgent · 5 = DO NOW

## Notes

- Due dates: `YYYY-MM-DD` (time component added automatically)
- All commands print a ✓ on success or ✗ with an error message on failure
- `--yes` skips confirmation prompts on destructive operations
- Output is Rich-formatted tables; use `--limit N` on list commands for large datasets
- Project source + AGENTS.md: `~/vikunja-cli/`
