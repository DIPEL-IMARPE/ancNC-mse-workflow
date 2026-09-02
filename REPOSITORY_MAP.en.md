# Repository map

> **Primary documentation language:** Spanish · [Versión en español](REPOSITORY_MAP.md)

This is the clickable navigation index for the template. Each linked folder contains local documentation explaining what belongs there and how it connects to the MSE workflow.

## Main structure

- [`.github/`](.github/ABOUT.en.md) — GitHub automation and change-review tools; not part of the scientific MSE.
- [`docs/`](docs/) — scientific and institutional documentation, ordered from objectives and system knowledge through adoption and review.
- [`data/`](data/) — data separated by access level and processing stage.
- [`references/`](references/) — regulations, assessment/survey reports, and scientific literature.
- [`registry/`](registry/) — project traceability logbooks for sources, data, parameters, objectives, uncertainties, MPs, runs, and decisions.
- [`config/`](config/) — configuration files read by the code to define what scenario or experiment to run.
- [`models/`](models/) — scientific specifications for each closed-loop component.
- [`src/`](src/) — reusable calculation functions.
- [`scripts/`](scripts/) — scripts that start and coordinate complete workflow stages by calling functions from `src/`.
- [`tests/`](tests/) — automatic software and scientific checks.
- [`reports/`](reports/) — reproducible technical, management, and stakeholder reports.
- [`outputs/`](outputs/) — generated simulation results.
- [`certification/`](certification/) — frozen approved versions supporting reproducibility and audit.

For the full folder-by-folder Spanish explanation, use [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md). The Spanish document is the authoritative navigation guide.
