# Data policy - `ancNC-mse-workflow`

This GitHub repository is public. Only information authorized for public distribution may be committed. The project distinguishes `public`, `derived_public`, `internal`, and `restricted` information.

`data/raw_private/` and `local_private/` are restricted and never committed. `data/interim/`, `data/processed/`, and `outputs/` are internal by default and are also excluded from Git. Public metadata may describe the existence, ownership, coverage, and MSE role of a restricted dataset without exposing its observations.

Always register datasets in `registry/data_inventory.csv` and documentary sources in `registry/source_registry.csv`.
