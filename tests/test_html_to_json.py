#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))), 'r') as f:
        file_text = f.read()
    return file_text


def test_content():
    html_string = _read_file('./test1.html')
    json_output = html_to_json.convert(html_string)


def test_simple_html1():
    html_string = """<head>
    <title>MalwareConfig - Rule Manager</title>
    <meta charset="UTF-8">
    <meta name="description" content="Yara Rule Manager">
    <meta name="google-site-verification" content="zI3MVR02eLr7MZ_BbS_4ZMlqjmmuriRFcvymZ6dD5Vc" />
    <meta name="keywords" content="yara,rules">
    <link href="/static/css/bootstrap.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
</head>"""
    json_output = html_to_json.convert(html_string)
    assert json_output == {
        'head': [
        {
            'meta': [
            {},
            {},
            {
                'link': [
                {},
                {}],
                'meta': [
                {}],
                'script': [
                {}]
            }],
            'title': [
            {
                'value': 'MalwareConfig - Rule Manager'
            }]
        }]
    }


def test_simple_html2():
    html_string = """<ul class="nav navbar-nav navbar-right">
        <li><a href="http://viper.malwareconfig.com">Viper</a></li>
        <li><a href="http://aptnotes.malwareconfig.com">APTNotes</a></li>
        <li><a href="/search/">Search</a></li>
        <li><a href="#" data-toggle="modal" data-target="#aboutModal">About</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Help <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="/admin">Admin</a></li>
            <li><a href="#">Docs</a></li>
            <li><a href="#">Issues</a></li>
            <li><a href="#">ChangeLog</a></li>
            <li class="divider"></li>
            <li><a href="#" data-toggle="modal" data-target="#aboutModal">About</a></li>

          </ul>
        </li>
      </ul>"""
    json_output = html_to_json.convert(html_string)
    print("json_output {}".format(json_output))
    assert json_output == {
        'ul': [{
            'li': [{
                'a': [{'value': 'Viper'}]
            }, {
                'a': [{'value': 'APTNotes'}]
            }, {
                'a': [{'value': 'Search'}]
            }, {
                'a': [{'value': 'About'}]
            }, {
                'a': [{
                    'value': 'Help ',
                    'span': [{}]
                }],
                'ul': [{
                    'li': [{
                        'a': [{'value': 'Admin'}]
                    }, {
                        'a': [{'value': 'Docs'}]
                    }, {
                        'a': [{'value': 'Issues'}]
                    }, {
                        'a': [{'value': 'ChangeLog'}]
                    },
                    {},
                    {
                        'a': [{'value': 'About'}]
                    }]
                }]
            }]
        }]
    }
