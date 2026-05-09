#!/usr/bin/env python
"""Tests for class A tables: tables with table headers (<th>) in the first row."""

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))), 'r') as f:
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
    html_string = _read_file('./data/test2.html')
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
                '#': '25545',
                'Malware': 'DarkComet',
                'MD5': 'eed5dcfdaea99ce886ce8cb2bed9425f',
                'Date Added': 'June 20, 2018, 6:25 a.m.',
            },
            {
                '#': '25544',
                'Malware': 'PoisonIvy',
                'MD5': 'ba38eb35dc8e6688e4b4aa4f8951ed7f',
                'Date Added': 'June 4, 2018, 6:25 a.m.',
            },
            {
                '#': '25543',
                'Malware': 'PoisonIvy',
                'MD5': 'e167b6311a7c435b4d65287ace236591',
                'Date Added': 'June 4, 2018, 6:25 a.m.',
            },
            {
                '#': '25542',
                'Malware': 'DarkComet',
                'MD5': '6024467685f74f4129512207b2510e43',
                'Date Added': 'May 30, 2018, 6:25 a.m.',
            },
            {
                '#': '25541',
                'Malware': 'DarkComet',
                'MD5': 'c65c3c8c4035481a6833394476c82ff1',
                'Date Added': 'May 27, 2018, 6:25 a.m.',
            },
            {
                '#': '25540',
                'Malware': 'DarkComet',
                'MD5': '41c60a7201487465e7e06921b20c3ec8',
                'Date Added': 'May 6, 2018, 6:25 a.m.',
            },
            {
                '#': '25539',
                'Malware': 'DarkComet',
                'MD5': 'd953a90802ca685f564ee9a4562f8304',
                'Date Added': 'May 4, 2018, 6:25 a.m.',
            },
            {
                '#': '25538',
                'Malware': 'Xtreme',
                'MD5': '7799e36a2e9c54c3ef1c3b379d620d82',
                'Date Added': 'April 27, 2018, 6:25 a.m.',
            },
            {
                '#': '25537',
                'Malware': 'DarkComet',
                'MD5': '757e55d3785c8bcebb0c20c764923cfd',
                'Date Added': 'April 22, 2018, 6:25 a.m.',
            },
            {
                '#': '25536',
                'Malware': 'DarkComet',
                'MD5': '376568c88494ccb037c91727e0330a96',
                'Date Added': 'April 22, 2018, 6:25 a.m.',
            },
            {
                '#': '25535',
                'Malware': 'CyberGate',
                'MD5': 'b1730fff58fd04367cff9b39b2942d15',
                'Date Added': 'April 20, 2018, 6:37 a.m.',
            },
            {
                '#': '25534',
                'Malware': 'DarkComet',
                'MD5': '222d3bc7996197f02093c156eee501b0',
                'Date Added': 'April 15, 2018, 6:25 a.m.',
            },
            {
                '#': '25533',
                'Malware': 'DarkComet',
                'MD5': 'fe36d10f6bb264f0059be752f4d5772e',
                'Date Added': 'April 14, 2018, 6:25 a.m.',
            },
            {
                '#': '25532',
                'Malware': 'DarkComet',
                'MD5': '5ad6c554bd80683b037bd5cccae435f6',
                'Date Added': 'April 12, 2018, 6:25 a.m.',
            },
            {
                '#': '25531',
                'Malware': 'DarkComet',
                'MD5': '51dd3b397a83c7d4c82d0c7b1a3f2800',
                'Date Added': 'April 9, 2018, 6:25 a.m.',
            },
            {
                '#': '25530',
                'Malware': 'DarkComet',
                'MD5': '5922c431e3c8868cfd6bb729b6389586',
                'Date Added': 'April 8, 2018, 6:25 a.m.',
            },
            {
                '#': '25529',
                'Malware': 'DarkComet',
                'MD5': 'f58e5c0213c3d16c0735d5a53ff2b2ce',
                'Date Added': 'April 6, 2018, 6:25 a.m.',
            },
            {
                '#': '25528',
                'Malware': 'DarkComet',
                'MD5': '202210615e3d74385e58b6242a1373ea',
                'Date Added': 'April 2, 2018, 6:25 a.m.',
            },
            {
                '#': '25527',
                'Malware': 'DarkComet',
                'MD5': '628abfc87f7e7adaf3bfcf6adad6d167',
                'Date Added': 'April 2, 2018, 6:25 a.m.',
            },
            {
                '#': '25526',
                'Malware': 'DarkComet',
                'MD5': 'ad20b1d4c948a33f0ffbfdc2aaf5275a',
                'Date Added': 'April 2, 2018, 6:25 a.m.',
            },
            {
                '#': '25525',
                'Malware': 'DarkComet',
                'MD5': 'e0ee266cb78120568f5fd139d0f60f94',
                'Date Added': 'April 2, 2018, 6:25 a.m.',
            },
            {
                '#': '25524',
                'Malware': 'DarkComet',
                'MD5': 'b7e97ed0da34cc9991d729c35f0249c7',
                'Date Added': 'April 2, 2018, 6:25 a.m.',
            },
            {
                '#': '25523',
                'Malware': 'DarkComet',
                'MD5': 'dc141691c1b1530896f13594a17f62d6',
                'Date Added': 'March 26, 2018, 6:25 a.m.',
            },
            {
                '#': '25522',
                'Malware': 'Xtreme',
                'MD5': '81160e72402be519311eb81cf4775f6f',
                'Date Added': 'March 25, 2018, 6:25 a.m.',
            },
        ]
    ]
