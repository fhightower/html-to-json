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
- **Breaking:** Make the boolean flags keyword-only arguments in `convert` (`debug`, `capture_element_values`, `capture_element_attributes`) and `convert_tables` (`record_children`, `debug`) (see [#9](https://github.com/fhightower/html-to-json/issues/9))
- Fix `IndexError` in `convert_tables` when a table has a single `<tr>` whose first cell is a lone `<th>` (see [#34](https://github.com/fhightower/html-to-json/issues/34))
- Switch the build backend from `setuptools` to `hatchling`
- Pin the `beautifulsoup4` runtime dependency to an exact version and the dev dependencies to their major versions
- Simplify the `ruff` configuration
- Update the Dependabot `package-ecosystem` from `pip` to `uv` (see [#36](https://github.com/fhightower/html-to-json/issues/36))

## [2.0.0] - 2021-02-27

### Added

* Ability to convert HTML tables without headers to JSON (see [#2](https://github.com/fhightower/html-to-json/issues/2))

## [1.0.8] - 2021-02-18

### Added

* Improved project README and metadata
