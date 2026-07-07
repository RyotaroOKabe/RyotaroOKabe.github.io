# Slash Command: /site-audit

This command runs a repository audit to check styling, content mismatches, and build environments.

## Command Definition
```bash
# Check branch status
git status

# Check if there are any untracked or modified CV files
Get-ChildItem -Path files/*cv*.pdf

# List top-level Jekyll pages and settings
Get-ChildItem -Path _pages/*.md, _config.yml

# List recent publications in the CSV database
Select-String -Path markdown_generator/publications.csv -Pattern "2025|2026"
```

## Intended Behavior
- Ensure that the local git branch is clean or currently on the redesign branch.
- Flag any new PDF files under `files/` that are not synced in the markdown contents.
- Report any difference in publications between the CV PDF and the CSV database.
