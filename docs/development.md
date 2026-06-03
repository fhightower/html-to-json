## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency and environment management. Python 3.10+ is required.

### Setup

```shell
git clone git@github.com:fhightower/html-to-json.git && cd html-to-json
uv sync
```

### Tests and linting

```shell
uv run pytest
./scripts/lint.sh
```

### Building the docs

The docs are built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme.

```shell
pip install mkdocs-material
mkdocs serve  # live-reload preview at http://127.0.0.1:8000
mkdocs build  # static site in ./site
```

The interactive demo on the home page runs the library directly in the browser via [Pyodide](https://pyodide.org/). The Pyodide bootstrap lives in `docs/overrides/main.html`; the markup for the widgets is in `docs/index.md`.

When the home page loads, the override script:

1. Loads Pyodide from the CDN.
2. Calls `micropip.install("html-to-json")` to install the latest published wheel from PyPI.
3. Wires the `Convert` / `Convert tables` buttons to `html_to_json.convert` and `html_to_json.convert_tables`.

To test the demo against an unreleased version of the library, replace the `micropip.install("html-to-json")` call in `docs/overrides/main.html` with a `micropip.install` of a local wheel URL, or paste the source of `convert_html.py` / `convert_html_tables.py` directly into the bootstrap.

### Releasing

Releases are published to PyPI via the `python-publish.yml` GitHub Actions workflow. After a release, the in-browser demo will pick up the new version automatically the next time the page is loaded (Pyodide always installs the latest from PyPI).
