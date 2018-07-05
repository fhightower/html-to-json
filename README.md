# HTML to JSON

Convert html to json.

## Installation

You can install html-to-json as follows:

```
git clone https://gitlab.com/fhightower/html-to-json.git && cd html-to-json;
python setup.py install --user;
```

## Usage

```python
import html_to_json

html_string = """<head>
    <title>Test site</title>
    <meta charset="UTF-8"></head>"""
output_json = html_to_json.convert(html_string)
print(output_json)
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and fhightower's [Python project template](https://github.com/fhightower-templates/python-project-template).
