#!/usr/bin/env python

import os

import html_to_json


def _read_file(file_name):
    with open(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))),
        'r',
    ) as f:
        file_text = f.read()
    return file_text


def test_content_1():
    html_string = _read_file('./data/test1.html')
    json_output = html_to_json.convert(html_string)


def test_content_2():
    html_string = _read_file('./data/test2.html')
    json_output = html_to_json.convert(html_string)
    print('json_output {}'.format(json_output))
    assert json_output['html'][0]['body'][0]['div'][0]['div'][3]['table'][0]['tr'][1:] == [
        {
            'td': [
                {'_value': '25546'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/ebae9a144636a11dc7bb42724d830109'},
                            '_value': 'ebae9a144636a11dc7bb42724d830109',
                        }
                    ]
                },
                {'_value': 'June 20, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25545'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/eed5dcfdaea99ce886ce8cb2bed9425f'},
                            '_value': 'eed5dcfdaea99ce886ce8cb2bed9425f',
                        }
                    ]
                },
                {'_value': 'June 20, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25544'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/PoisonIvy/'},
                            '_value': 'PoisonIvy',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/ba38eb35dc8e6688e4b4aa4f8951ed7f'},
                            '_value': 'ba38eb35dc8e6688e4b4aa4f8951ed7f',
                        }
                    ]
                },
                {'_value': 'June 4, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25543'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/PoisonIvy/'},
                            '_value': 'PoisonIvy',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/e167b6311a7c435b4d65287ace236591'},
                            '_value': 'e167b6311a7c435b4d65287ace236591',
                        }
                    ]
                },
                {'_value': 'June 4, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25542'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/6024467685f74f4129512207b2510e43'},
                            '_value': '6024467685f74f4129512207b2510e43',
                        }
                    ]
                },
                {'_value': 'May 30, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25541'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/c65c3c8c4035481a6833394476c82ff1'},
                            '_value': 'c65c3c8c4035481a6833394476c82ff1',
                        }
                    ]
                },
                {'_value': 'May 27, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25540'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/41c60a7201487465e7e06921b20c3ec8'},
                            '_value': '41c60a7201487465e7e06921b20c3ec8',
                        }
                    ]
                },
                {'_value': 'May 6, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25539'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/d953a90802ca685f564ee9a4562f8304'},
                            '_value': 'd953a90802ca685f564ee9a4562f8304',
                        }
                    ]
                },
                {'_value': 'May 4, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25538'},
                {'a': [{'_attributes': {'href': '/stats/Xtreme/'}, '_value': 'Xtreme'}]},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/7799e36a2e9c54c3ef1c3b379d620d82'},
                            '_value': '7799e36a2e9c54c3ef1c3b379d620d82',
                        }
                    ]
                },
                {'_value': 'April 27, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25537'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/757e55d3785c8bcebb0c20c764923cfd'},
                            '_value': '757e55d3785c8bcebb0c20c764923cfd',
                        }
                    ]
                },
                {'_value': 'April 22, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25536'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/376568c88494ccb037c91727e0330a96'},
                            '_value': '376568c88494ccb037c91727e0330a96',
                        }
                    ]
                },
                {'_value': 'April 22, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25535'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/CyberGate/'},
                            '_value': 'CyberGate',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/b1730fff58fd04367cff9b39b2942d15'},
                            '_value': 'b1730fff58fd04367cff9b39b2942d15',
                        }
                    ]
                },
                {'_value': 'April 20, 2018, 6:37 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25534'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/222d3bc7996197f02093c156eee501b0'},
                            '_value': '222d3bc7996197f02093c156eee501b0',
                        }
                    ]
                },
                {'_value': 'April 15, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25533'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/fe36d10f6bb264f0059be752f4d5772e'},
                            '_value': 'fe36d10f6bb264f0059be752f4d5772e',
                        }
                    ]
                },
                {'_value': 'April 14, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25532'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/5ad6c554bd80683b037bd5cccae435f6'},
                            '_value': '5ad6c554bd80683b037bd5cccae435f6',
                        }
                    ]
                },
                {'_value': 'April 12, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25531'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/51dd3b397a83c7d4c82d0c7b1a3f2800'},
                            '_value': '51dd3b397a83c7d4c82d0c7b1a3f2800',
                        }
                    ]
                },
                {'_value': 'April 9, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25530'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/5922c431e3c8868cfd6bb729b6389586'},
                            '_value': '5922c431e3c8868cfd6bb729b6389586',
                        }
                    ]
                },
                {'_value': 'April 8, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25529'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/f58e5c0213c3d16c0735d5a53ff2b2ce'},
                            '_value': 'f58e5c0213c3d16c0735d5a53ff2b2ce',
                        }
                    ]
                },
                {'_value': 'April 6, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25528'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/202210615e3d74385e58b6242a1373ea'},
                            '_value': '202210615e3d74385e58b6242a1373ea',
                        }
                    ]
                },
                {'_value': 'April 2, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25527'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/628abfc87f7e7adaf3bfcf6adad6d167'},
                            '_value': '628abfc87f7e7adaf3bfcf6adad6d167',
                        }
                    ]
                },
                {'_value': 'April 2, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25526'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/ad20b1d4c948a33f0ffbfdc2aaf5275a'},
                            '_value': 'ad20b1d4c948a33f0ffbfdc2aaf5275a',
                        }
                    ]
                },
                {'_value': 'April 2, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25525'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/e0ee266cb78120568f5fd139d0f60f94'},
                            '_value': 'e0ee266cb78120568f5fd139d0f60f94',
                        }
                    ]
                },
                {'_value': 'April 2, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25524'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/b7e97ed0da34cc9991d729c35f0249c7'},
                            '_value': 'b7e97ed0da34cc9991d729c35f0249c7',
                        }
                    ]
                },
                {'_value': 'April 2, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25523'},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/stats/DarkComet/'},
                            '_value': 'DarkComet',
                        }
                    ]
                },
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/dc141691c1b1530896f13594a17f62d6'},
                            '_value': 'dc141691c1b1530896f13594a17f62d6',
                        }
                    ]
                },
                {'_value': 'March 26, 2018, 6:25 a.m.'},
            ]
        },
        {
            'td': [
                {'_value': '25522'},
                {'a': [{'_attributes': {'href': '/stats/Xtreme/'}, '_value': 'Xtreme'}]},
                {
                    'a': [
                        {
                            '_attributes': {'href': '/config/81160e72402be519311eb81cf4775f6f'},
                            '_value': '81160e72402be519311eb81cf4775f6f',
                        }
                    ]
                },
                {'_value': 'March 25, 2018, 6:25 a.m.'},
            ]
        },
    ]


def test_simple_html1():
    html_string = """<head>
    <title>MalwareConfig - Rule Manager</title>
    <meta charset='UTF-8'>
    <meta name='description' content='Yara Rule Manager'>
    <meta name='google-site-verification' content='zI3MVR02eLr7MZ_BbS_4ZMlqjmmuriRFcvymZ6dD5Vc' />
    <meta name='keywords' content='yara,rules'>
    <link href='/static/css/bootstrap.css' rel='stylesheet'>
    <link href='/static/css/style.css' rel='stylesheet'>
    <script src='https://maps.googleapis.com/maps/api/js?v=3.exp'></script>
</head>"""
    json_output = html_to_json.convert(html_string)
    print('json_output {}'.format(json_output))
    assert json_output == {
        'head': [
            {
                'title': [{'_value': 'MalwareConfig - Rule Manager'}],
                'meta': [
                    {'_attributes': {'charset': 'UTF-8'}},
                    {
                        '_attributes': {
                            'name': 'description',
                            'content': 'Yara Rule Manager',
                        }
                    },
                    {
                        '_attributes': {
                            'name': 'google-site-verification',
                            'content': 'zI3MVR02eLr7MZ_BbS_4ZMlqjmmuriRFcvymZ6dD5Vc',
                        },
                        'meta': [
                            {
                                '_attributes': {
                                    'name': 'keywords',
                                    'content': 'yara,rules',
                                }
                            }
                        ],
                        'link': [
                            {
                                '_attributes': {
                                    'href': '/static/css/bootstrap.css',
                                    'rel': ['stylesheet'],
                                }
                            },
                            {
                                '_attributes': {
                                    'href': '/static/css/style.css',
                                    'rel': ['stylesheet'],
                                }
                            },
                        ],
                        'script': [{'_attributes': {'src': 'https://maps.googleapis.com/maps/api/js?v=3.exp'}}],
                    },
                ],
            }
        ]
    }


def test_simple_html2():
    html_string = """<ul class='nav navbar-nav navbar-right'>
        <li><a href='http://viper.malwareconfig.com'>Viper</a></li>
        <li><a href='http://aptnotes.malwareconfig.com'>APTNotes</a></li>
        <li><a href='/search/'>Search</a></li>
        <li><a href='#' data-toggle='modal' data-target='#aboutModal'>About</a></li>
        <li class='dropdown'>
          <a href='#' class='dropdown-toggle' data-toggle='dropdown'>Help <span class='caret'></span></a>
          <ul class='dropdown-menu' role='menu'>
            <li><a href='/admin'>Admin</a></li>
            <li><a href='#'>Docs</a></li>
            <li><a href='#'>Issues</a></li>
            <li><a href='#'>ChangeLog</a></li>
            <li class='divider'></li>
            <li><a href='#' data-toggle='modal' data-target='#aboutModal'>About</a></li>
          </ul>
        </li>
      </ul>"""
    json_output = html_to_json.convert(html_string)
    print('json_output {}'.format(json_output))
    assert json_output == {
        'ul': [
            {
                '_attributes': {'class': ['nav', 'navbar-nav', 'navbar-right']},
                'li': [
                    {
                        'a': [
                            {
                                '_attributes': {'href': 'http://viper.malwareconfig.com'},
                                '_value': 'Viper',
                            }
                        ]
                    },
                    {
                        'a': [
                            {
                                '_attributes': {'href': 'http://aptnotes.malwareconfig.com'},
                                '_value': 'APTNotes',
                            }
                        ]
                    },
                    {'a': [{'_attributes': {'href': '/search/'}, '_value': 'Search'}]},
                    {
                        'a': [
                            {
                                '_attributes': {
                                    'href': '#',
                                    'data-toggle': 'modal',
                                    'data-target': '#aboutModal',
                                },
                                '_value': 'About',
                            }
                        ]
                    },
                    {
                        '_attributes': {'class': ['dropdown']},
                        'a': [
                            {
                                '_attributes': {
                                    'href': '#',
                                    'class': ['dropdown-toggle'],
                                    'data-toggle': 'dropdown',
                                },
                                '_value': 'Help',
                                'span': [{'_attributes': {'class': ['caret']}}],
                            }
                        ],
                        'ul': [
                            {
                                '_attributes': {
                                    'class': ['dropdown-menu'],
                                    'role': 'menu',
                                },
                                'li': [
                                    {
                                        'a': [
                                            {
                                                '_attributes': {'href': '/admin'},
                                                '_value': 'Admin',
                                            }
                                        ]
                                    },
                                    {
                                        'a': [
                                            {
                                                '_attributes': {'href': '#'},
                                                '_value': 'Docs',
                                            }
                                        ]
                                    },
                                    {
                                        'a': [
                                            {
                                                '_attributes': {'href': '#'},
                                                '_value': 'Issues',
                                            }
                                        ]
                                    },
                                    {
                                        'a': [
                                            {
                                                '_attributes': {'href': '#'},
                                                '_value': 'ChangeLog',
                                            }
                                        ]
                                    },
                                    {'_attributes': {'class': ['divider']}},
                                    {
                                        'a': [
                                            {
                                                '_attributes': {
                                                    'href': '#',
                                                    'data-toggle': 'modal',
                                                    'data-target': '#aboutModal',
                                                },
                                                '_value': 'About',
                                            }
                                        ]
                                    },
                                ],
                            }
                        ],
                    },
                ],
            }
        ]
    }


def test_missing_content():
    html_string = _read_file('./data/test3_missing_content.html')
    json_output = html_to_json.convert(html_string)
    print('json_output {}'.format(json_output))
    assert 'hxxp://ioa993u.space/vnc.exe' in str(json_output)
    assert '2018-08-22' in str(json_output)


def test_multiple_text_entries():
    """Make sure multiple text entries are handled well."""
    html_string = """<p>bingo</p>test<br/>
ing<br/>"""
    json_output = html_to_json.convert(html_string)
    assert json_output == {
        'br': [{}, {}],
        'p': [{'_value': 'bingo'}],
        '_values': ['test', 'ing'],
    }


def test_pdfexaminer():
    html_string = _read_file('./data/pdfexaminer.com.html')
    json_output = html_to_json.convert(html_string)
    json_output_string = str(json_output)
    assert '33.0@4675: pdf.exploit Corrupted JPEG2000' in json_output_string
    assert '1.0@25957: suspicious.obfuscation using app.setTimeOut to eval code' in json_output_string


def test_empty_spaces():
    """Make sure empty spaces are not recorded as values."""
    html_string = """<p>bingo</p>test  <br/>   <br/>
ing<br/>"""
    json_output = html_to_json.convert(html_string)
    assert json_output == {
        'br': [{}, {}, {}],
        'p': [{'_value': 'bingo'}],
        '_values': ['test', 'ing'],
    }


def test_not_capturing_element_values():
    html_string = """<p id='foo'>bingo</p>test  <br/>   <br/>
ing<br/>"""
    json_output = html_to_json.convert(html_string, capture_element_values=False)
    assert json_output == {'br': [{}, {}, {}], 'p': [{'_attributes': {'id': 'foo'}}]}


def test_not_capturing_element_attributes():
    html_string = """<p id='foo'>bingo</p>test  <br/>   <br/>
ing<br/>"""
    json_output = html_to_json.convert(html_string, capture_element_attributes=False)
    assert json_output == {
        'br': [{}, {}, {}],
        'p': [{'_value': 'bingo'}],
        '_values': ['test', 'ing'],
    }


def test_capturing_neither_attributes_nor_values():
    html_string = """<p id='foo'>bingo</p>test  <br/>   <br/>
ing<br/>"""
    json_output = html_to_json.convert(html_string, capture_element_values=False, capture_element_attributes=False)
    assert json_output == {'br': [{}, {}, {}], 'p': [{}]}
