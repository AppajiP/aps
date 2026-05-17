# AGENTS.md

## Cursor Cloud specific instructions

### Repository overview

This is "aps" — a Marathi-language Python programming course for Maharashtra board students. The `main` branch contains only a minimal `README.md`. Course content (chapter-organized Python scripts and Marathi-language READMEs) lives on feature branches such as `cursor/python-course-marathi-*`.

### Development environment

- **Language:** Python 3 (stdlib only — no third-party dependencies).
- **No package manager, lockfile, build system, or services** are needed.
- **Running scripts:** Each `.py` file is a standalone lab exercise. Run with `python3 <file>.py`. Some labs use `input()` and require interactive TTY input — avoid those in automated CI.
- **Linting:** No linter is configured in the repo. You can use `python3 -m py_compile <file>.py` to syntax-check any script.
- **Testing:** No test framework is configured. Validate scripts by running them and checking stdout.

### Gotchas

- The main branch is nearly empty; most content is on feature branches. Always check which branch you need before making changes.
- Lab scripts that call `input()` will block if run non-interactively. Pipe input via `echo "value" | python3 script.py` or skip those in automated runs.
