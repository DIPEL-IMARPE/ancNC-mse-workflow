# Automatic checks (`tests/`)

> **Primary documentation language:** Spanish · [Versión en español](README.md) · [Repository map](../REPOSITORY_MAP.en.md)

This folder contains automated checks for both software behavior and scientific consistency. `unit/` checks individual functions; `scientific/` checks biological and fishery invariants; `integration/` checks that OM, observation, estimation, MP, and implementation components connect correctly; and `regression/` detects unintended changes to previously accepted results.

A simulation can run without a software error and still be scientifically wrong, so both types of checks are required for formal MSE work.
