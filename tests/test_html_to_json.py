#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))), 'r') as f:
        file_text = f.read()
    return file_text


def test_content_1():
    html_string = _read_file('./data/test1.html')
    json_output = html_to_json.convert(html_string)


def test_content_2():
    html_string = _read_file('./data/test2.html')
    json_output = html_to_json.convert(html_string)
    assert json_output['html'][0]['body'][0]['div'][0]['div'][3]['table'][0]['tr'][1:] == [{'td': [{'value': '25546'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/ebae9a144636a11dc7bb42724d830109'}, 'value': 'ebae9a144636a11dc7bb42724d830109'}]}, {'value': 'June 20, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25545'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/eed5dcfdaea99ce886ce8cb2bed9425f'}, 'value': 'eed5dcfdaea99ce886ce8cb2bed9425f'}]}, {'value': 'June 20, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25544'}, {'a': [{'attributes': {'href': '/stats/PoisonIvy/'}, 'value': 'PoisonIvy'}]}, {'a': [{'attributes': {'href': '/config/ba38eb35dc8e6688e4b4aa4f8951ed7f'}, 'value': 'ba38eb35dc8e6688e4b4aa4f8951ed7f'}]}, {'value': 'June 4, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25543'}, {'a': [{'attributes': {'href': '/stats/PoisonIvy/'}, 'value': 'PoisonIvy'}]}, {'a': [{'attributes': {'href': '/config/e167b6311a7c435b4d65287ace236591'}, 'value': 'e167b6311a7c435b4d65287ace236591'}]}, {'value': 'June 4, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25542'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/6024467685f74f4129512207b2510e43'}, 'value': '6024467685f74f4129512207b2510e43'}]}, {'value': 'May 30, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25541'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/c65c3c8c4035481a6833394476c82ff1'}, 'value': 'c65c3c8c4035481a6833394476c82ff1'}]}, {'value': 'May 27, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25540'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/41c60a7201487465e7e06921b20c3ec8'}, 'value': '41c60a7201487465e7e06921b20c3ec8'}]}, {'value': 'May 6, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25539'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/d953a90802ca685f564ee9a4562f8304'}, 'value': 'd953a90802ca685f564ee9a4562f8304'}]}, {'value': 'May 4, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25538'}, {'a': [{'attributes': {'href': '/stats/Xtreme/'}, 'value': 'Xtreme'}]}, {'a': [{'attributes': {'href': '/config/7799e36a2e9c54c3ef1c3b379d620d82'}, 'value': '7799e36a2e9c54c3ef1c3b379d620d82'}]}, {'value': 'April 27, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25537'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/757e55d3785c8bcebb0c20c764923cfd'}, 'value': '757e55d3785c8bcebb0c20c764923cfd'}]}, {'value': 'April 22, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25536'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/376568c88494ccb037c91727e0330a96'}, 'value': '376568c88494ccb037c91727e0330a96'}]}, {'value': 'April 22, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25535'}, {'a': [{'attributes': {'href': '/stats/CyberGate/'}, 'value': 'CyberGate'}]}, {'a': [{'attributes': {'href': '/config/b1730fff58fd04367cff9b39b2942d15'}, 'value': 'b1730fff58fd04367cff9b39b2942d15'}]}, {'value': 'April 20, 2018, 6:37 a.m.'}]}, {'td': [{'value': '25534'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/222d3bc7996197f02093c156eee501b0'}, 'value': '222d3bc7996197f02093c156eee501b0'}]}, {'value': 'April 15, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25533'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/fe36d10f6bb264f0059be752f4d5772e'}, 'value': 'fe36d10f6bb264f0059be752f4d5772e'}]}, {'value': 'April 14, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25532'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/5ad6c554bd80683b037bd5cccae435f6'}, 'value': '5ad6c554bd80683b037bd5cccae435f6'}]}, {'value': 'April 12, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25531'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/51dd3b397a83c7d4c82d0c7b1a3f2800'}, 'value': '51dd3b397a83c7d4c82d0c7b1a3f2800'}]}, {'value': 'April 9, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25530'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/5922c431e3c8868cfd6bb729b6389586'}, 'value': '5922c431e3c8868cfd6bb729b6389586'}]}, {'value': 'April 8, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25529'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/f58e5c0213c3d16c0735d5a53ff2b2ce'}, 'value': 'f58e5c0213c3d16c0735d5a53ff2b2ce'}]}, {'value': 'April 6, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25528'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/202210615e3d74385e58b6242a1373ea'}, 'value': '202210615e3d74385e58b6242a1373ea'}]}, {'value': 'April 2, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25527'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/628abfc87f7e7adaf3bfcf6adad6d167'}, 'value': '628abfc87f7e7adaf3bfcf6adad6d167'}]}, {'value': 'April 2, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25526'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/ad20b1d4c948a33f0ffbfdc2aaf5275a'}, 'value': 'ad20b1d4c948a33f0ffbfdc2aaf5275a'}]}, {'value': 'April 2, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25525'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/e0ee266cb78120568f5fd139d0f60f94'}, 'value': 'e0ee266cb78120568f5fd139d0f60f94'}]}, {'value': 'April 2, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25524'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/b7e97ed0da34cc9991d729c35f0249c7'}, 'value': 'b7e97ed0da34cc9991d729c35f0249c7'}]}, {'value': 'April 2, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25523'}, {'a': [{'attributes': {'href': '/stats/DarkComet/'}, 'value': 'DarkComet'}]}, {'a': [{'attributes': {'href': '/config/dc141691c1b1530896f13594a17f62d6'}, 'value': 'dc141691c1b1530896f13594a17f62d6'}]}, {'value': 'March 26, 2018, 6:25 a.m.'}]}, {'td': [{'value': '25522'}, {'a': [{'attributes': {'href': '/stats/Xtreme/'}, 'value': 'Xtreme'}]}, {'a': [{'attributes': {'href': '/config/81160e72402be519311eb81cf4775f6f'}, 'value': '81160e72402be519311eb81cf4775f6f'}]}, {'value': 'March 25, 2018, 6:25 a.m.'}]}]


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
        'title': [
        {
            'value': 'MalwareConfig - Rule Manager'
        }],
        'meta': [
        {
            'attributes':
            {
                'charset': 'UTF-8'
            }
        },
        {
            'attributes':
            {
                'name': 'description',
                'content': 'Yara Rule Manager'
            }
        },
        {
            'attributes':
            {
                'name': 'google-site-verification',
                'content': 'zI3MVR02eLr7MZ_BbS_4ZMlqjmmuriRFcvymZ6dD5Vc'
            },
            'meta': [
            {
                'attributes':
                {
                    'name': 'keywords',
                    'content': 'yara,rules'
                }
            }],
            'link': [
            {
                'attributes':
                {
                    'href': '/static/css/bootstrap.css',
                    'rel': ['stylesheet']
                }
            },
            {
                'attributes':
                {
                    'href': '/static/css/style.css',
                    'rel': ['stylesheet']
                }
            }],
            'script': [
            {
                'attributes':
                {
                    'src': 'https://maps.googleapis.com/maps/api/js?v=3.exp'
                }
            }]
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
    'ul': [
    {
        'attributes':
        {
            'class': ['nav', 'navbar-nav', 'navbar-right']
        },
        'li': [
        {
            'a': [
            {
                'attributes':
                {
                    'href': 'http://viper.malwareconfig.com'
                },
                'value': 'Viper'
            }]
        },
        {
            'a': [
            {
                'attributes':
                {
                    'href': 'http://aptnotes.malwareconfig.com'
                },
                'value': 'APTNotes'
            }]
        },
        {
            'a': [
            {
                'attributes':
                {
                    'href': '/search/'
                },
                'value': 'Search'
            }]
        },
        {
            'a': [
            {
                'attributes':
                {
                    'href': '#',
                    'data-toggle': 'modal',
                    'data-target': '#aboutModal'
                },
                'value': 'About'
            }]
        },
        {
            'attributes':
            {
                'class': ['dropdown']
            },
            'a': [
            {
                'attributes':
                {
                    'href': '#',
                    'class': ['dropdown-toggle'],
                    'data-toggle': 'dropdown'
                },
                'value': 'Help ',
                'span': [
                {
                    'attributes':
                    {
                        'class': ['caret']
                    }
                }]
            }],
            'ul': [
            {
                'attributes':
                {
                    'class': ['dropdown-menu'],
                    'role': 'menu'
                },
                'li': [
                {
                    'a': [
                    {
                        'attributes':
                        {
                            'href': '/admin'
                        },
                        'value': 'Admin'
                    }]
                },
                {
                    'a': [
                    {
                        'attributes':
                        {
                            'href': '#'
                        },
                        'value': 'Docs'
                    }]
                },
                {
                    'a': [
                    {
                        'attributes':
                        {
                            'href': '#'
                        },
                        'value': 'Issues'
                    }]
                },
                {
                    'a': [
                    {
                        'attributes':
                        {
                            'href': '#'
                        },
                        'value': 'ChangeLog'
                    }]
                },
                {
                    'attributes':
                    {
                        'class': ['divider']
                    }
                },
                {
                    'a': [
                    {
                        'attributes':
                        {
                            'href': '#',
                            'data-toggle': 'modal',
                            'data-target': '#aboutModal'
                        },
                        'value': 'About'
                    }]
                }]
            }]
        }]
    }]
}
