# `.github` directory

This directory contains files that GitHub interprets automatically for repository governance and automation.

## Contents

| Element | Function |
|---|---|
| `ISSUE_TEMPLATE/` | Templates for scientific decisions, issues, and changes. |
| `workflows/` | GitHub Actions for automated repository checks. |
| `pull_request_template.md` | Checklist shown when opening a Pull Request. |

## Why this file is `ABOUT.md`, not `README.md`

GitHub can prioritize a `README.md` located inside `.github/` when deciding which document to display as the repository landing page. To ensure that the root `README.md`-the MSE overview-is always the repository cover, this directory is documented with `ABOUT.md`.

## Rule

Do not create `.github/README.md` or `.github/README.en.md`. Keep bilingual documentation here as `ABOUT.md` and `ABOUT.en.md`.
