#!/usr/bin/env python
"""Convert html to json."""

import logging
from collections.abc import Iterable
from typing import Any

import bs4
from bs4.element import PageElement, Tag

logger = logging.getLogger(__name__)

# The JSON-like structure produced for an HTML section: a (possibly nested) mapping
# of tag names to lists of further structures of the same shape, plus any captured
# ``_value``/``_values``/``_attributes`` entries.
JSONDict = dict[str, Any]


def _debug(debug: bool, message: object, prefix: str = '') -> None:
    """Log the given message if debugging is true."""
    if debug:
        logger.debug('%s%s', prefix, message)


def _record_element_value(element: str, json_output: JSONDict) -> None:
    """Record the html element's value in the json_output."""
    element = element.strip()
    if element != '\n' and element != '':
        if json_output.get('_value'):
            json_output['_values'] = [json_output['_value']]
            json_output['_values'].append(element)
            del json_output['_value']
        elif json_output.get('_values'):
            json_output['_values'].append(element)
        else:
            json_output['_value'] = element


def _iterate(
    html_section: Iterable[PageElement],
    json_output: JSONDict,
    count: int,
    *,
    debug: bool,
    capture_element_values: bool,
    capture_element_attributes: bool,
) -> JSONDict:
    _debug(debug, '========== Start New Iteration ==========', '    ' * count)
    _debug(debug, f'HTML_SECTION:\n{html_section}')
    _debug(debug, f'JSON_OUTPUT:\n{json_output}')
    for part in html_section:
        if isinstance(part, Tag):
            if not json_output.get(part.name):
                json_output[part.name] = list()
            new_json_output_for_subparts: JSONDict = dict()
            if part.attrs and capture_element_attributes:
                new_json_output_for_subparts = {'_attributes': part.attrs}
            count += 1
            json_output[part.name].append(
                _iterate(
                    part,
                    new_json_output_for_subparts,
                    count,
                    debug=debug,
                    capture_element_values=capture_element_values,
                    capture_element_attributes=capture_element_attributes,
                )
            )
        else:
            if capture_element_values:
                _record_element_value(str(part), json_output)
    return json_output


def convert(
    html_string: str,
    *,
    debug: bool = False,
    capture_element_values: bool = True,
    capture_element_attributes: bool = True,
) -> JSONDict:
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    children = [child for child in soup.contents]
    return _iterate(
        children,
        {},
        0,
        debug=debug,
        capture_element_values=capture_element_values,
        capture_element_attributes=capture_element_attributes,
    )
