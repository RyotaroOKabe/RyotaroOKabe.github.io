# Slash Command: /implementation-pass

This command runs the actual style integration and content syncing.

## Command Definition
```bash
# Pauses Dropbox Sync if needed, and runs local jekyll server to test changes
bundle exec jekyll serve

# Run python script to regenerate publications from CSV
python markdown_generator/publications.py
```

## Intended Behavior
- Ensure that the CSS variables token system is implemented under `_sass/_tokens.scss` and imported in `assets/css/main.scss`.
- Ensure that the manual dark mode toggle is functional.
- Validate that the generated HTML files in `_site/` build successfully.
