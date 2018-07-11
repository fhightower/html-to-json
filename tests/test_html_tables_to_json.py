#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))), 'r') as f:
        file_text = f.read()
    return file_text


def test_content_2():
    html_string = _read_file('./data/test2.html')
    json_output = html_to_json.convert(html_string)
    assert 1 == 2


def test_simple_class_a_table():
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
    assert tables == [[{
        '#': '25548',
        'Malware': 'DarkComet',
        'MD5': '034a37b2a2307f876adc9538986d7b86',
        'Date Added': 'July 9, 2018, 6:25 a.m.'
    }, {
        '#': '25547',
        'Malware': 'DarkComet',
        'MD5': '706eeefbac3de4d58b27d964173999c3',
        'Date Added': 'July 7, 2018, 6:25 a.m.'
    }]]


def test_simple_class_b_table():
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
    assert tables == [{
        'Malware Family': 'DarkComet',
        'Date Added': 'July 9, 2018, 6:25 a.m.',
        'MD5': '034a37b2a2307f876adc9538986d7b86',
        'Sha256': '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13',
        'Robot': 'Robots lovingly delivered by robohash.org'
    }]


def test_malformed_table():
    html_string = """<table class="table table-striped table-bordered table-hover">
                <tr>
                    <th>Malware Family</th>
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
    json_output = html_to_json.convert(html_string)
    assert 1 == 2
