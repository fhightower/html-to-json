# Changelog

This changelog is based on the format specified here: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Add a `record_html` keyword argument to `convert_tables()` to capture each cell's inner HTML as a string, preserving nested tags and attributes (see [#20](https://github.com/fhightower/html-to-json/issues/20))
- Document the existing `record_children` keyword argument of `convert_tables()` in the README
- Drop support for Python < 3.10; declare support for Python 3.10–3.13
- Migrate project metadata from `setup.py`/`setup.cfg` to PEP 621 `pyproject.toml`
- Switch dev workflow from Docker/Docker Compose to `uv`
- Replace `black`, `isort`, `flake8`, and `pylint` with `ruff`
- Remove leftover Python 2 compatibility code in `convert_html.py`

## [2.0.0] - 2021-02-27

### Added

* Ability to convert HTML tables without headers to JSON (see [#2](https://github.com/fhightower/html-to-json/issues/2))

## [1.0.8] - 2021-02-18

### Added

* Improved project README and metadata
