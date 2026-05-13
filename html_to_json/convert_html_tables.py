#!/usr/bin/env python
"""Convert html tables to json."""

from typing import Any

import bs4
from bs4.element import Tag

from .convert_html import _debug, convert

# A single parsed cell value: plain text, the cell's inner HTML, or the cell's
# children converted to JSON (see ``_cell_value``).
CellValue = Any
# The parsed representation of one table; the concrete shape depends on the table
# layout (see ``_process_table``).
TableData = list[dict[str, CellValue]] | dict[str, CellValue] | list[list[CellValue]]


def _cell_value(cell: Tag, record_children: bool, record_html: bool, debug: bool) -> CellValue:
    """Return the value for the given table cell based on the recording options.

    By default the cell's text is returned (nested tags are dropped). Pass
    ``record_html=True`` to return the cell's inner HTML as a string, or
    ``record_children=True`` to return the cell's children converted to JSON.
    If both are given, ``record_html`` takes precedence.
    """
    if record_html:
        value = cell.decode_contents().strip()
        _debug(debug, f'Value (html): {value}')
        return value
    if record_children:
        # if we are recording the children, convert the html of the <td>
        value = convert(str(cell))['td']
        _debug(debug, f'Value (children): {value}')
        return value
    _debug(debug, f'Value: {cell.text}')
    return cell.text


def _handle_class_a_table(
    table: Tag, *, record_children: bool, record_html: bool, debug: bool
) -> list[dict[str, CellValue]]:
    """Handle tables with the table headers across the top row."""
    table_data: list[dict[str, CellValue]] = list()
    keys = [item.text for item in table.find_all('tr')[0].find_all('th')]
    _debug(debug, f'Found {len(keys)} keys:\n{keys}')
    _debug(debug, f'Found {len(table.find_all("tr")[1:])} rows')

    for row in table.find_all('tr')[1:]:
        _debug(debug, '========== New Row ==========')
        row_data: dict[str, CellValue] = dict()
        for index, cell in enumerate(row.find_all('td')):
            _debug(debug, f'Key: "{keys[index]}"')
            row_data[keys[index]] = _cell_value(cell, record_children, record_html, debug)
        table_data.append(row_data)
    return table_data


def _handle_class_b_table(table: Tag, *, record_children: bool, record_html: bool, debug: bool) -> dict[str, CellValue]:
    """Handle tables with the table headers in the first column (the first cell of each row)."""
    table_data: dict[str, CellValue] = dict()

    # TODO: document why the `row.find_all('td')[0]` code in the block below has a [0] at the end

    rows = table.find_all('tr')
    _debug(debug, f'Found {len(rows)} rows')
    for row in rows:
        _debug(debug, '========== New Row ==========')
        key = row.find_all('th')[0].text
        _debug(debug, f'Key: "{key}"')
        table_data[key] = _cell_value(row.find_all('td')[0], record_children, record_html, debug)
    return table_data


def _handle_headless_table(
    table: Tag, *, record_children: bool, record_html: bool, debug: bool
) -> list[list[CellValue]]:
    """Handle tables without "th" elements."""
    table_data: list[list[CellValue]] = list()

    rows = table.find_all('tr')
    _debug(debug, f'Found {len(rows)} rows')

    for row in rows:
        _debug(debug, '========== New Row ==========')
        row_data = [_cell_value(column, record_children, record_html, debug) for column in row.find_all('td')]
        table_data.append(row_data)
    return table_data


def _process_table(html_table: Tag, *, record_children: bool, record_html: bool, debug: bool) -> TableData:
    """Process the given table."""
    table_data: TableData = list()

    table_class_debug_message = (
        'Processing table as a {} table '
        + '(you can read more about the different types of tables here: '
        + 'https://github.com/fhightower/html-to-json#html-tables-to-json)'
    )

    if len(html_table.find_all('tr')[0].find_all('th')) > 1:
        _debug(debug, table_class_debug_message.format('class A'))
        table_data = _handle_class_a_table(
            html_table, record_children=record_children, record_html=record_html, debug=debug
        )
    else:
        if (
            len(html_table.find_all('tr')) > 1
            and len(html_table.find_all('tr')[0].find_all('th')) == 1
            and len(html_table.find_all('tr')[1].find_all('th')) == 1
        ):
            _debug(debug, table_class_debug_message.format('class B'))
            table_data = _handle_class_b_table(
                html_table, record_children=record_children, record_html=record_html, debug=debug
            )
        elif len(html_table.find_all('tr')[0].find_all('th')) == 1:
            _debug(debug, table_class_debug_message.format('class A'))
            table_data = _handle_class_a_table(
                html_table, record_children=record_children, record_html=record_html, debug=debug
            )
        else:
            _debug(debug, table_class_debug_message.format('headless'))
            table_data = _handle_headless_table(
                html_table, record_children=record_children, record_html=record_html, debug=debug
            )
    return table_data


def convert_tables(
    html_string: str, *, record_children: bool = False, record_html: bool = False, debug: bool = False
) -> list[TableData]:
    """Convert all of the tables in the html string to json.

    By default, only the text of each table cell is captured. To preserve
    nested tags (e.g. ``<a>`` elements) and their attributes, pass either:

    * ``record_children=True`` to capture each cell's children as JSON (using
      the same structure produced by ``convert``), or
    * ``record_html=True`` to capture each cell's inner HTML as a string.

    If both are given, ``record_html`` takes precedence.
    """
    tables: list[TableData] = list()

    soup = bs4.BeautifulSoup(html_string, 'html.parser')

    _debug(debug, 'Found {} table(s)'.format(len(soup.find_all('table'))))
    for table in soup.find_all('table'):
        table_data = _process_table(table, record_children=record_children, record_html=record_html, debug=debug)
        if table_data:
            tables.append(table_data)

    return tables
