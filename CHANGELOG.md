# Changelog

This changelog is based on the format specified here: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Drop support for Python < 3.10; declare support for Python 3.10–3.13
- Migrate project metadata from `setup.py`/`setup.cfg` to PEP 621 `pyproject.toml`
- Switch dev workflow from Docker/Docker Compose to `uv`
- Replace `black`, `isort`, `flake8`, and `pylint` with `ruff`
- Remove leftover Python 2 compatibility code in `convert_html.py`
- **Breaking:** Make the boolean flags keyword-only arguments in `convert` (`debug`, `capture_element_values`, `capture_element_attributes`) and `convert_tables` (`record_children`, `debug`) (see [#9](https://github.com/fhightower/html-to-json/issues/9))

## [2.0.0] - 2021-02-27

### Added

* Ability to convert HTML tables without headers to JSON (see [#2](https://github.com/fhightower/html-to-json/issues/2))

## [1.0.8] - 2021-02-18

### Added

* Improved project README and metadata
