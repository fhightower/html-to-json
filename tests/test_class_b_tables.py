#!/usr/bin/env python
"""Tests for class B tables: tables with table headers (<th>) in the first column of each row."""

import html_to_json


def test_class_b_basic():
    html_string = """<table class="table table-striped table-bordered table-hover">
                <tr>
                    <th>Malware Family</th>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <th>Date Added</th>
                    <td>July 9, 2018, 6:25 a.m.</td>
                </tr>
                <tr>
                    <th>MD5</th>
                    <td>034a37b2a2307f876adc9538986d7b86</td>
                </tr>
                <tr>
                    <th>Sha256</th>
                    <td>297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13</td>
                </tr>
                <tr>
                    <th>Robot</th>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    tables = html_to_json.convert_tables(html_string)
    assert tables == [
        {
            'Malware Family': 'DarkComet',
            'Date Added': 'July 9, 2018, 6:25 a.m.',
            'MD5': '034a37b2a2307f876adc9538986d7b86',
            'Sha256': '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13',
            'Robot': 'Robots lovingly delivered by robohash.org',
        }
    ]


def test_class_b_record_children():
    html_string = """<table class="table table-striped table-bordered table-hover">
                <tr>
                    <th>Malware Family</th>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <th>Date Added</th>
                    <td>July 9, 2018, 6:25 a.m.</td>
                </tr>
                <tr>
                    <th>MD5</th>
                    <td>034a37b2a2307f876adc9538986d7b86</td>
                </tr>
                <tr>
                    <th>Sha256</th>
                    <td>297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13</td>
                </tr>
                <tr>
                    <th>Robot</th>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    tables = html_to_json.convert_tables(html_string, record_children=True)
    assert tables == [
        {
            'Malware Family': [{'a': [{'_attributes': {'href': '/stats/DarkComet/'}, '_value': 'DarkComet'}]}],
            'Date Added': [{'_value': 'July 9, 2018, 6:25 a.m.'}],
            'MD5': [{'_value': '034a37b2a2307f876adc9538986d7b86'}],
            'Sha256': [{'_value': '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13'}],
            'Robot': [
                {
                    '_value': 'Robots lovingly delivered by',
                    'a': [{'_attributes': {'href': 'https://robohash.org'}, '_value': 'robohash.org'}],
                }
            ],
        }
    ]


def test_class_b_record_html():
    html_string = """<table>
                <tr>
                    <th>Malware Family</th>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <th>Date Added</th>
                    <td>July 9, 2018, 6:25 a.m.</td>
                </tr>
                <tr>
                    <th>Robot</th>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    tables = html_to_json.convert_tables(html_string, record_html=True)
    assert tables == [
        {
            'Malware Family': '<a href="/stats/DarkComet/">DarkComet</a>',
            'Date Added': 'July 9, 2018, 6:25 a.m.',
            'Robot': 'Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a>',
        }
    ]


def test_class_b_empty_value():
    """Empty <td> values in a class B table become empty strings."""
    html_string = """<table>
        <tr><th>Name</th><td>Alice</td></tr>
        <tr><th>Email</th><td></td></tr>
        <tr><th>Phone</th><td>555-0100</td></tr>
    </table>"""
    tables = html_to_json.convert_tables(html_string)
    assert tables == [
        {
            'Name': 'Alice',
            'Email': '',
            'Phone': '555-0100',
        }
    ]
