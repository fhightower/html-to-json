#!/usr/bin/env python
"""Tests for class A tables: tables with table headers (<th>) in the first row."""

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./{file_name}"))) as f:
        file_text = f.read()
    return file_text


def test_class_a_basic():
    html_string = """<table class="table table-striped table-bordered table-hover">
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
    assert tables == [
        [
            {
                '#': '25548',
                'Malware': 'DarkComet',
                'MD5': '034a37b2a2307f876adc9538986d7b86',
                'Date Added': 'July 9, 2018, 6:25 a.m.',
            },
            {
                '#': '25547',
                'Malware': 'DarkComet',
                'MD5': '706eeefbac3de4d58b27d964173999c3',
                'Date Added': 'July 7, 2018, 6:25 a.m.',
            },
        ]
    ]


def test_class_a_record_children():
    html_string = """<table class="table table-striped table-bordered table-hover">
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
    tables = html_to_json.convert_tables(html_string, record_children=True)
    assert tables == [
        [
            {
                '#': [{'_value': '25548'}],
                'Malware': [{'a': [{'_attributes': {'href': '/stats/DarkComet/'}, '_value': 'DarkComet'}]}],
                'MD5': [
                    {
                        'a': [
                            {
                                '_attributes': {'href': '/config/034a37b2a2307f876adc9538986d7b86'},
                                '_value': '034a37b2a2307f876adc9538986d7b86',
                            }
                        ]
                    }
                ],
                'Date Added': [{'_value': 'July 9, 2018, 6:25 a.m.'}],
            },
            {
                '#': [{'_value': '25547'}],
                'Malware': [{'a': [{'_attributes': {'href': '/stats/DarkComet/'}, '_value': 'DarkComet'}]}],
                'MD5': [
                    {
                        'a': [
                            {
                                '_attributes': {'href': '/config/706eeefbac3de4d58b27d964173999c3'},
                                '_value': '706eeefbac3de4d58b27d964173999c3',
                            }
                        ]
                    }
                ],
                'Date Added': [{'_value': 'July 7, 2018, 6:25 a.m.'}],
            },
        ]
    ]


def test_class_a_single_column():
    """A class A table with only one header column still parses correctly."""
    html_string = """<table>
        <tr><th>Name</th></tr>
        <tr><td>Alice</td></tr>
        <tr><td>Bob</td></tr>
    </table>"""
    tables = html_to_json.convert_tables(html_string)
    assert tables == [[{'Name': 'Alice'}, {'Name': 'Bob'}]]


def test_class_a_empty_cells():
    """Empty <td> cells in a class A table become empty string values."""
    html_string = """<table>
        <tr><th>A</th><th>B</th><th>C</th></tr>
        <tr><td>1</td><td></td><td>3</td></tr>
        <tr><td></td><td>5</td><td></td></tr>
    </table>"""
    tables = html_to_json.convert_tables(html_string)
    assert tables == [
        [
            {'A': '1', 'B': '', 'C': '3'},
            {'A': '', 'B': '5', 'C': ''},
        ]
    ]


def test_class_a_from_file():
    html_string = _read_file('./data/class_a_table.html')
    json_output = html_to_json.convert_tables(html_string)
    assert json_output == [
        [
            {
                '#': '25546',
                'Malware': 'DarkComet',
                'MD5': 'ebae9a144636a11dc7bb42724d830109',
                'Date Added': 'June 20, 2018, 6:25 a.m.',
            },
            {
                '#': '25544',
                'Malware': 'PoisonIvy',
                'MD5': 'ba38eb35dc8e6688e4b4aa4f8951ed7f',
                'Date Added': 'June 4, 2018, 6:25 a.m.',
            },
            {
                '#': '25522',
                'Malware': 'Xtreme',
                'MD5': '81160e72402be519311eb81cf4775f6f',
                'Date Added': 'March 25, 2018, 6:25 a.m.',
            },
        ]
    ]
