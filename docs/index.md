# HTML to JSON

[![PyPI](https://img.shields.io/pypi/v/html-to-json.svg)](https://pypi.python.org/pypi/html-to-json)
![PyPI - Downloads](https://img.shields.io/pypi/dm/html-to-json)
[![codecov](https://codecov.io/gh/fhightower/html-to-json/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/fhightower/html-to-json)

Welcome to the documentation for the `html-to-json` library — a small Python library for converting HTML (and HTML tables) to JSON.

📢 *If this library is useful to you, please consider [sponsoring](https://github.com/sponsors/fhightower) the project.*

## Quick-Start

Install html-to-json:

```shell
pip install html-to-json
```

Use it:

```python
import html_to_json

html_string = """<head>
    <title>Test site</title>
    <meta charset="UTF-8"></head>"""

output_json = html_to_json.convert(html_string)
print(output_json)
```

## Try it in your browser (INTERACTIVE!)

No install required — run the real `html-to-json` library right in your browser via [Pyodide](https://pyodide.org/). Edit some HTML, flip the options, and watch the JSON update live.

[Open the interactive demo :material-arrow-right:](demo.md){ .md-button .md-button--primary }

## Capabilities

??? info "What this library converts"

    - Arbitrary HTML to a JSON-friendly Python dictionary (`html_to_json.convert`)
    - HTML tables to a list of row dictionaries (`html_to_json.convert_tables`), including:
        - Tables with headers in the first row
        - Tables with headers in the first column
        - Tables without headers

??? info "Configuration options"

    `convert()`:

    - `capture_element_values` (default `True`) — capture the text inside each element under the `_value` key.
    - `capture_element_attributes` (default `True`) — capture each element's attributes under the `_attributes` key.

    `convert_tables()`:

    - `record_html` (default `False`) — capture each cell's inner HTML as a string. Useful for preserving links and other inline markup.
    - `record_children` (default `False`) — capture each cell's children as JSON (using the same shape produced by `convert`). If both flags are set, `record_html` wins.

## Feedback

If you have ideas to improve this package, please [open an issue][issues_link]!

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and fhightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[issues_link]: https://github.com/fhightower/html-to-json/issues
