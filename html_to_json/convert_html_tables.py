#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert html tables to json."""

import bs4

from .convert_html import convert


def _handle_class_a_table(table, record_children):
    """Handle tables with the table headers across the top row."""
    table_data = list()
    keys = [item.text for item in table.find_all('tr')[0].find_all('th')]

    for row in table.find_all('tr')[1:]:
        row_data = dict()
        for index, cell in enumerate(row.find_all('td')):
            if record_children:
                # if we are recording the children, convert the html of the <td>
                row_data[keys[index]] = convert(str(cell))['td']
            else:
                row_data[keys[index]] = cell.text
        table_data.append(row_data)
    return table_data


def _handle_class_b_table(table, record_children):
    """Handle tables with the table headers in the first column (the first cell of each row)."""
    table_data = dict()

    # TODO: document why the `row.find_all('td')[0]` code in the block below has a [0] at the end

    for row in table.find_all('tr'):
        if record_children:
            # if we are recording the children, convert the html of the <td>
            table_data[row.find_all('th')[0].text] = convert(str(row.find_all('td')[0]))['td']
        else:
            table_data[row.find_all('th')[0].text] = row.find_all('td')[0].text
    return table_data


def _process_table(html_table, record_children):
    """Process the given table."""
    table_data = list()

    if len(html_table.find_all('tr')[0].find_all('th')) > 1:
        table_data = _handle_class_a_table(html_table, record_children)
    else:
        if len(html_table.find_all('tr')[0].find_all('th')) == 1 and len(html_table.find_all('tr')[1].find_all('th')) == 1:
            table_data = _handle_class_b_table(html_table, record_children)
        elif len(html_table.find_all('tr')[0].find_all('th')) == 1:
            table_data = _handle_class_a_table(html_table, record_children)
        else:
            raise RuntimeWarning('Unable to parse the format of the given table.')
    return table_data



def convert_tables(html_string, record_children=False):
    """Convert all of the tables in the html string to json."""
    tables = list()

    soup = bs4.BeautifulSoup(html_string, 'html.parser')

    for table in soup.find_all('table'):
        table_data = _process_table(table, record_children)
        tables.append(table_data)

    return tables
