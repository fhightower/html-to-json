#!/usr/bin/env python
"""Convert the JSON produced by :func:`html_to_json.convert` back to HTML."""

from html import escape
from typing import Any

JSONDict = dict[str, Any]

# HTML5 void elements - rendered without a closing tag.
# https://html.spec.whatwg.org/multipage/syntax.html#void-elements
_VOID_ELEMENTS = frozenset(
    {
        'area',
        'base',
        'br',
        'col',
        'embed',
        'hr',
        'img',
        'input',
        'link',
        'meta',
        'param',
        'source',
        'track',
        'wbr',
    }
)


def _render_attribute_value(value: Any) -> str:
    if isinstance(value, list):
        return ' '.join(str(item) for item in value)
    return str(value)


def _render_attributes(attributes: dict[str, Any]) -> str:
    parts = []
    for name, value in attributes.items():
        if value is True or value == '':
            parts.append(name)
        elif value is False or value is None:
            continue
        else:
            parts.append(f'{name}="{escape(_render_attribute_value(value), quote=True)}"')
    return ''.join(' ' + part for part in parts)


def _render_node(tag: str, node: JSONDict) -> str:
    attributes = node.get('_attributes', {})
    opening = f'<{tag}{_render_attributes(attributes)}>'

    if tag in _VOID_ELEMENTS:
        return opening

    inner = _render_children(node)
    return f'{opening}{inner}</{tag}>'


def _render_children(node: JSONDict) -> str:
    pieces: list[str] = []

    if '_value' in node:
        pieces.append(escape(str(node['_value'])))
    if '_values' in node:
        pieces.extend(escape(str(value)) for value in node['_values'])

    for key, children in node.items():
        if key in ('_value', '_values', '_attributes'):
            continue
        if not isinstance(children, list):
            continue
        for child in children:
            pieces.append(_render_node(key, child))

    return ''.join(pieces)


def json_to_html(json_input: JSONDict) -> str:
    """Convert a JSON dictionary produced by :func:`convert` back to an HTML string.

    The inverse is not perfect: the JSON representation groups sibling elements
    by tag name, so the relative order between *different* tags (and between
    tags and free-floating text nodes captured in ``_values``) is lost. Text
    captured in ``_value``/``_values`` is emitted before any child tags.
    """
    return _render_children(json_input)
