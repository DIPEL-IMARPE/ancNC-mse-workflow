# Project data (`data/`)

> **Primary documentation language:** Spanish · [Versión en español](README.md) · [Repository map](../REPOSITORY_MAP.en.md)

This folder separates data by access level and processing stage. `examples/` contains fictitious data for testing the template; `public/` contains redistributable data; `raw_private/` is for restricted original data and is ignored by Git; `interim/` and `processed/` contain reproducible derived products; and `metadata/` stores variable definitions, units, coverage, protocol changes, and quality-control rules.

Every important dataset should be registered in `registry/data_inventory.csv`. Restricted raw data must not be committed to Git even when the repository itself is private.
