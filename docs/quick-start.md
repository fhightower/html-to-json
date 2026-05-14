## Installation

The recommended means of installation is using [pip](https://pypi.python.org/pypi/pip/):

```shell
pip install html-to-json
```

Alternatively, you can work with a local checkout:

```shell
git clone git@github.com:fhightower/html-to-json.git && cd html-to-json
uv sync
```

## Usage

### HTML to JSON

```python
import html_to_json

html_string = """<head>
    <title>Test site</title>
    <meta charset="UTF-8"></head>"""
output_json = html_to_json.convert(html_string)
print(output_json)
```

`html_to_json.convert` accepts the following keyword arguments:

- `capture_element_values` (default `True`) — capture the text inside each element under the `_value` key.
- `capture_element_attributes` (default `True`) — capture each element's attributes under the `_attributes` key.

#### Example

Input:

```html
<head>
    <title>Floyd Hightower's Projects</title>
    <meta charset="UTF-8">
    <meta name="description" content="Floyd Hightower&#39;s Projects">
    <meta name="keywords" content="projects,fhightower,Floyd,Hightower">
</head>
```

Output:

```json
{
    "head": [
    {
        "title": [
        {
            "_value": "Floyd Hightower's Projects"
        }],
        "meta": [
        {
            "_attributes":
            {
                "charset": "UTF-8"
            }
        },
        {
            "_attributes":
            {
                "name": "description",
                "content": "Floyd Hightower's Projects"
            }
        },
        {
            "_attributes":
            {
                "name": "keywords",
                "content": "projects,fhightower,Floyd,Hightower"
            }
        }]
    }]
}
```

### HTML tables to JSON

This library can intelligently convert HTML tables to JSON. It handles three shapes:

- A. Tables with [table headers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) in the first row
- B. Tables with table headers in the first column
- C. Tables without table headers

#### Example

```python
import html_to_json

html_string = """<table>
    <tr>
        <th>#</th>
        <th>Malware</th>
        <th>MD5</th>
        <th>Date Added</th>
    </tr>
    <tr>
        <td>25548</td>
        <td><a href="/stats/DarkComet/">DarkComet</a></td>
        <td><a href="/config/034a37b2a2307f876adc9538986d7b86">034a37b2a2307f876adc9538986d7b86</a></td>
        <td>July 9, 2018, 6:25 a.m.</td>
    </tr>
    <tr>
        <td>25547</td>
        <td><a href="/stats/DarkComet/">DarkComet</a></td>
        <td><a href="/config/706eeefbac3de4d58b27d964173999c3">706eeefbac3de4d58b27d964173999c3</a></td>
        <td>July 7, 2018, 6:25 a.m.</td>
    </tr></table>"""
tables = html_to_json.convert_tables(html_string)
print(tables)
```

produces:

```json
[
    [
        {
            "#": "25548",
            "Malware": "DarkComet",
            "MD5": "034a37b2a2307f876adc9538986d7b86",
            "Date Added": "July 9, 2018, 6:25 a.m."
        },
        {
            "#": "25547",
            "Malware": "DarkComet",
            "MD5": "706eeefbac3de4d58b27d964173999c3",
            "Date Added": "July 7, 2018, 6:25 a.m."
        }
    ]
]
```

#### Preserving nested tags in table cells

By default, `convert_tables()` only captures the *text* of each cell, so nested tags (such as `<a>` elements) and their attributes are dropped. To keep them, pass one of:

- `record_html=True` — capture each cell's inner HTML as a string.
- `record_children=True` — capture each cell's children as JSON, using the same structure produced by `convert()`.

If both are given, `record_html` takes precedence.

For more examples, see [`tests/`](https://github.com/fhightower/html-to-json/tree/main/tests) or play with the [interactive demo](index.md#try-it-in-your-browser-interactive).
