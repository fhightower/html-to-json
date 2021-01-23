#!/usr/bin/env python
"""Convert html tables to json."""

import bs4

from .convert_html import convert, _debug


def _handle_class_a_table(table, record_children, debug):
    """Handle tables with the table headers across the top row."""
    table_data = list()
    keys = [item.text for item in table.find_all('tr')[0].find_all('th')]
    _debug(debug, 'Found {} keys:\n{}'.format(len(keys), keys))
    _debug(debug, 'Found {} rows'.format(len(table.find_all('tr')[1:])))

    for row in table.find_all('tr')[1:]:
        _debug(debug, '========== New Row ==========')
        row_data = dict()
        for index, cell in enumerate(row.find_all('td')):
            if record_children:
                _debug(
                    debug,
                    'Key: "{}"\nValue: {}'.format(keys[index], convert(str(cell))['td']),
                )
                # if we are recording the children, convert the html of the <td>
                row_data[keys[index]] = convert(str(cell))['td']
            else:
                _debug(debug, 'Key: "{}"\nValue: {}'.format(keys[index], cell.text))
                row_data[keys[index]] = cell.text
        table_data.append(row_data)
    return table_data


def _handle_class_b_table(table, record_children, debug):
    """Handle tables with the table headers in the first column (the first cell of each row)."""
    table_data = dict()

    # TODO: document why the `row.find_all('td')[0]` code in the block below has a [0] at the end

    rows = table.find_all('tr')
    _debug(debug, 'Found {} rows'.format(len(rows)))
    for row in rows:
        _debug(debug, '========== New Row ==========')
        key = row.find_all('th')[0].text
        if record_children:
            _debug(
                debug,
                'Key: "{}"\nValue: {}'.format(key, convert(str(row.find_all('td')[0]))['td']),
            )
            # if we are recording the children, convert the html of the <td>
            table_data[key] = convert(str(row.find_all('td')[0]))['td']
        else:
            _debug(debug, 'Key: "{}"\nValue: {}'.format(key, row.find_all('td')[0].text))
            table_data[key] = row.find_all('td')[0].text
    return table_data


def _process_table(html_table, record_children, debug):
    """Process the given table."""
    table_data = list()

    table_class_debug_message = 'Processing table as class {} table (you can read more about the different types of tables here: https://github.com/fhightower/html-to-json#html-tables-to-json)'

    if len(html_table.find_all('tr')[0].find_all('th')) > 1:
        _debug(debug, table_class_debug_message.format('A'))
        table_data = _handle_class_a_table(html_table, record_children, debug)
    else:
        if (
            len(html_table.find_all('tr')[0].find_all('th')) == 1
            and len(html_table.find_all('tr')[1].find_all('th')) == 1
        ):
            _debug(debug, table_class_debug_message.format('B'))
            table_data = _handle_class_b_table(html_table, record_children, debug)
        elif len(html_table.find_all('tr')[0].find_all('th')) == 1:
            _debug(debug, table_class_debug_message.format('A'))
            table_data = _handle_class_a_table(html_table, record_children, debug)
        else:
            message = 'Unable to parse the format of the given table that starts with the text: "{}..."'.format(
                str(html_table)[:40]
            )
            print(message)
    return table_data


def convert_tables(html_string, record_children=False, debug=False):
    """Convert all of the tables in the html string to json."""
    tables = list()

    soup = bs4.BeautifulSoup(html_string, 'html.parser')

    _debug(debug, 'Found {} table(s)'.format(len(soup.find_all('table'))))
    for table in soup.find_all('table'):
        table_data = _process_table(table, record_children, debug)
        if table_data:
            tables.append(table_data)

    return tables
