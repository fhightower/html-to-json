#!/usr/bin/env python
"""Tests for class C tables: tables without any <th> headers."""

import html_to_json


def test_class_c_basic():
    html_string = '''<table>
<tr><td>A</td><td>B</td></tr>
<tr><td>C</td><td>D</td></tr>
</table>'''
    json_output = html_to_json.convert_tables(html_string)
    assert json_output == [[['A', 'B'], ['C', 'D']]]


def test_class_c_two_columns():
    html_string = """<table class="table table-striped table-bordered table-hover">
                <tr>
                    <td>Malware Family</td>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <td>Date Added</td>
                    <td>July 9, 2018, 6:25 a.m.</td>
                </tr>
                <tr>
                    <td>MD5</td>
                    <td>034a37b2a2307f876adc9538986d7b86</td>
                </tr>
                <tr>
                    <td>Sha256</td>
                    <td>297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13</td>
                </tr>
                <tr>
                    <td>Robot</td>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    json_output = html_to_json.convert_tables(html_string)
    assert json_output == [
        [
            ['Malware Family', 'DarkComet'],
            ['Date Added', 'July 9, 2018, 6:25 a.m.'],
            ['MD5', '034a37b2a2307f876adc9538986d7b86'],
            ['Sha256', '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13'],
            ['Robot', 'Robots lovingly delivered by robohash.org'],
        ]
    ]


def test_class_c_record_children():
    html_string = """<table class="table table-striped table-bordered table-hover">
                <tr>
                    <td>Malware Family</td>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <td>Date Added</td>
                    <td>July 9, 2018, 6:25 a.m.</td>
                </tr>
                <tr>
                    <td>MD5</td>
                    <td>034a37b2a2307f876adc9538986d7b86</td>
                </tr>
                <tr>
                    <td>Sha256</td>
                    <td>297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13</td>
                </tr>
                <tr>
                    <td>Robot</td>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    json_output = html_to_json.convert_tables(html_string, record_children=True)
    assert json_output == [
        [
            [
                [{'_value': 'Malware Family'}],
                [{'a': [{'_attributes': {'href': '/stats/DarkComet/'}, '_value': 'DarkComet'}]}],
            ],
            [[{'_value': 'Date Added'}], [{'_value': 'July 9, 2018, 6:25 a.m.'}]],
            [[{'_value': 'MD5'}], [{'_value': '034a37b2a2307f876adc9538986d7b86'}]],
            [[{'_value': 'Sha256'}], [{'_value': '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13'}]],
            [
                [{'_value': 'Robot'}],
                [
                    {
                        '_value': 'Robots lovingly delivered by',
                        'a': [{'_attributes': {'href': 'https://robohash.org'}, '_value': 'robohash.org'}],
                    }
                ],
            ],
        ]
    ]


def test_class_c_record_html():
    html_string = """<table>
                <tr>
                    <td>Malware Family</td>
                    <td><a href="/stats/DarkComet/">DarkComet</a></td>
                </tr>
                <tr>
                    <td>Robot</td>
                    <td>Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a></td>
                </tr>
        </table>"""
    json_output = html_to_json.convert_tables(html_string, record_html=True)
    assert json_output == [
        [
            ['Malware Family', '<a href="/stats/DarkComet/">DarkComet</a>'],
            ['Robot', 'Robots lovingly delivered by <a href="https://robohash.org">robohash.org</a>'],
        ]
    ]


def test_class_c_variable_columns():
    """Class C tables tolerate rows with different numbers of cells."""
    html_string = """<table>
        <tr><td>A</td><td>B</td><td>C</td></tr>
        <tr><td>D</td><td>E</td></tr>
        <tr><td>F</td></tr>
    </table>"""
    json_output = html_to_json.convert_tables(html_string)
    assert json_output == [[['A', 'B', 'C'], ['D', 'E'], ['F']]]


def test_class_c_empty_cells():
    """Empty <td> cells in a class C table become empty strings."""
    html_string = """<table>
        <tr><td>A</td><td></td><td>C</td></tr>
        <tr><td></td><td>E</td><td></td></tr>
    </table>"""
    json_output = html_to_json.convert_tables(html_string)
    assert json_output == [[['A', '', 'C'], ['', 'E', '']]]
