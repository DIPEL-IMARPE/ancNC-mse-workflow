# Workflow scripts (`scripts/`)

> **Primary documentation language:** Spanish · [Versión en español](README.md) · [Repository map](../REPOSITORY_MAP.en.md)

This folder contains the files that **start and coordinate complete stages of the MSE workflow**. Rather than using the software term *entrypoint*, the Spanish documentation calls these *scripts de ejecución* (execution scripts).

The scripts should organize tasks, read configurations, call reusable functions from `src/`, save outputs, and record what was run. Reusable scientific equations and calculations belong in `src/`, not duplicated across scripts.

The numbered subfolders follow the main workflow: repository checks, data preparation, OM conditioning, OM validation, closed-loop MSE execution, performance summarization, report generation, and preparation of shareable releases.
