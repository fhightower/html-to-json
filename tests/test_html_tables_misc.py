#!/usr/bin/env python
"""Tests that exercise table-handling features which span multiple table classes,
such as parsing multiple tables from a single document or handling <thead> wrappers."""

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./{file_name}"))) as f:
        file_text = f.read()
    return file_text


def test_multiple_tables_in_single_document():
    html_string = _read_file('./data/test_two_tables.html')
    tables = html_to_json.convert_tables(html_string)
    assert len(tables) == 2
    assert tables[0] == [['Proxy port', 'Type of proxy', 'SSL support']]
    assert tables[1] == [
        {
            'IP address': '104.207.144.248',
            'Port': '10016',
            'Type': 'Socks5',
            'SSL': 'true',
            'Country': '\xa0United States\n',
            'Latency(msec)': '30',
            'Reliability(%)': '90.83',
            'Details': 'Details',
        },
        {
            'IP address': '104.236.154.163',
            'Port': '3128',
            'Type': 'Transparent',
            'SSL': 'true',
            'Country': '\xa0United States\n',
            'Latency(msec)': '21146',
            'Reliability(%)': '98.15',
            'Details': 'Details',
        },
        {},
    ]


def test_tables_with_thead():
    html_string = _read_file('./data/tables_with_thead.html')
    tables = html_to_json.convert_tables(html_string)
    assert tables == [
        [
            {'Country': 'United States', 'Code': 'US'},
            {'Country': 'Germany', 'Code': 'DE'},
        ],
        [
            {'Proxy': 'proxy-a.example.com', 'Port': '8080'},
        ],
    ]
    assert len(tables) == 2


def test_record_html_takes_precedence_over_record_children():
    html_string = """<table>
        <tr><th>Name</th><th>Link</th></tr>
        <tr><td>DarkComet</td><td><a href="/stats/DarkComet/">stats</a></td></tr>
    </table>"""
    tables = html_to_json.convert_tables(html_string, record_children=True, record_html=True)
    assert tables == [
        [
            {
                'Name': 'DarkComet',
                'Link': '<a href="/stats/DarkComet/">stats</a>',
            }
        ]
    ]


def test_single_row_table_with_one_th():
    """A table with a single <tr> whose first cell is a lone <th> should not raise
    an IndexError while disambiguating between class A and class B tables (see issue #34)."""
    tables = html_to_json.convert_tables('<table><tr><th>X</th><td></td></tr></table>')
    assert tables == []
