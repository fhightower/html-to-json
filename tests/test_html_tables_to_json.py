#!/usr/bin/env python

import os

import html_to_json


def _read_file(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./{}".format(file_name))), 'r') as f:
        file_text = f.read()
    return file_text


def test_content_2():
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
    assert tables == [
        {
            'Malware Family': 'DarkComet',
            'Date Added': 'July 9, 2018, 6:25 a.m.',
            'MD5': '034a37b2a2307f876adc9538986d7b86',
            'Sha256': '297248d6dafe0798e7ec352aae078863b935e6257fc7e9d390bc47c324ecee13',
            'Robot': 'Robots lovingly delivered by robohash.org',
        }
    ]


def test_strange_table_format():
    """This table should fail because there are no <th> elements."""
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
    assert json_output == []


def test_record_children_class_a_table():
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
    print("tables {}".format(tables))
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


def test_record_children_class_b_table():
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
    print("tables {}".format(tables))
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


def test_html_with_bad_table():
    html_string = _read_file('./data/test_bad_table.html')
    tables = html_to_json.convert_tables(html_string)
    assert len(tables) == 1
    assert tables == [
        [
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
            {
                'IP address': '104.236.175.94',
                'Port': '10000',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1381',
                'Reliability(%)': '87.23',
                'Details': 'Details',
            },
            {
                'IP address': '104.236.241.203',
                'Port': '3129',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '10102',
                'Reliability(%)': '98.64',
                'Details': 'Details',
            },
            {
                'IP address': '104.236.55.48',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1817',
                'Reliability(%)': '98.43',
                'Details': 'Details',
            },
            {
                'IP address': '104.236.82.218',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '49.99',
                'Details': 'Details',
            },
            {
                'IP address': '104.237.241.20',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '104.238.146.146',
                'Port': '8118',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '947',
                'Reliability(%)': '43.43',
                'Details': 'Details',
            },
            {
                'IP address': '104.244.159.63',
                'Port': '1080',
                'Type': 'Socks4',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '57.97',
                'Details': 'Details',
            },
            {
                'IP address': '13.91.38.119',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '419',
                'Reliability(%)': '98.15',
                'Details': 'Details',
            },
            {
                'IP address': '13.92.196.150',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '303',
                'Reliability(%)': '69.23',
                'Details': 'Details',
            },
            {
                'IP address': '132.148.131.31',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '16789',
                'Reliability(%)': '49.11',
                'Details': 'Details',
            },
            {
                'IP address': '138.197.173.107',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '5972',
                'Reliability(%)': '70.98',
                'Details': 'Details',
            },
            {
                'IP address': '138.68.140.197',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '2952',
                'Reliability(%)': '57.77',
                'Details': 'Details',
            },
            {
                'IP address': '138.68.184.67',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.11.99',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '2023',
                'Reliability(%)': '82.7',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.110.167',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '376',
                'Reliability(%)': '99.32',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.129.210',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '3451',
                'Reliability(%)': '60.11',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.13.101',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '863',
                'Reliability(%)': '96.08',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.136.198',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '757',
                'Reliability(%)': '98.04',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.142.92',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '2081',
                'Reliability(%)': '98.04',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.143.250',
                'Port': '8080',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '716',
                'Reliability(%)': '99.01',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.212.93',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '159.65.3.96',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '11088',
                'Reliability(%)': '25',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.175.86',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '859',
                'Reliability(%)': '98.08',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.192.39',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '759',
                'Reliability(%)': '92.3',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.196.170',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '845',
                'Reliability(%)': '94.22',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.201.112',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '902',
                'Reliability(%)': '94.22',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.201.219',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1126',
                'Reliability(%)': '97.92',
                'Details': 'Details',
            },
            {
                'IP address': '159.89.30.73',
                'Port': '3128',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '16554',
                'Reliability(%)': '99.04',
                'Details': 'Details',
            },
            {
                'IP address': '162.243.118.179',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '278',
                'Reliability(%)': '99.32',
                'Details': 'Details',
            },
            {
                'IP address': '165.227.145.128',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '165.227.94.207',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '4857',
                'Reliability(%)': '58.5',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.111.217',
                'Port': '3130',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '97.49',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.33.139',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1799',
                'Reliability(%)': '57.14',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.42.165',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '2354',
                'Reliability(%)': '58.43',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.42.6',
                'Port': '8080',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '241',
                'Reliability(%)': '98.74',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.61.206',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '275',
                'Reliability(%)': '97.96',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.64.242',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '9424',
                'Reliability(%)': '99.32',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.67.244',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '774',
                'Reliability(%)': '93.74',
                'Details': 'Details',
            },
            {
                'IP address': '167.99.82.226',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '3103',
                'Reliability(%)': '57.45',
                'Details': 'Details',
            },
            {
                'IP address': '172.104.100.120',
                'Port': '3128',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '7981',
                'Reliability(%)': '71.11',
                'Details': 'Details',
            },
            {
                'IP address': '172.104.161.188',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1067',
                'Reliability(%)': '97.88',
                'Details': 'Details',
            },
            {
                'IP address': '172.87.221.221',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '11364',
                'Reliability(%)': '32.09',
                'Details': 'Details',
            },
            {
                'IP address': '173.201.177.140',
                'Port': '3001',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '35283',
                'Reliability(%)': '19.17',
                'Details': 'Details',
            },
            {
                'IP address': '173.219.43.147',
                'Port': '11008',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '173.255.248.234',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '98.88',
                'Details': 'Details',
            },
            {
                'IP address': '173.45.67.182',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '7416',
                'Reliability(%)': '40.08',
                'Details': 'Details',
            },
            {
                'IP address': '192.126.123.222',
                'Port': '1080',
                'Type': 'Socks4',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '93.71',
                'Details': 'Details',
            },
            {
                'IP address': '192.241.154.247',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '5198',
                'Reliability(%)': '55.55',
                'Details': 'Details',
            },
            {
                'IP address': '192.30.85.19',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '198.211.121.46',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '9946',
                'Reliability(%)': '66.67',
                'Details': 'Details',
            },
            {
                'IP address': '198.98.49.82',
                'Port': '443',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '39.99',
                'Details': 'Details',
            },
            {
                'IP address': '199.167.213.238',
                'Port': '14681',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '66.65',
                'Details': 'Details',
            },
            {
                'IP address': '199.244.51.120',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '10328',
                'Reliability(%)': '88.89',
                'Details': 'Details',
            },
            {
                'IP address': '204.111.249.191',
                'Port': '10200',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '11.43',
                'Details': 'Details',
            },
            {
                'IP address': '204.186.76.75',
                'Port': '33009',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '15.97',
                'Details': 'Details',
            },
            {
                'IP address': '205.158.57.2',
                'Port': '53281',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '15295',
                'Reliability(%)': '41.57',
                'Details': 'Details',
            },
            {
                'IP address': '206.162.238.38',
                'Port': '39880',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '206.189.40.40',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1013',
                'Reliability(%)': '91.67',
                'Details': 'Details',
            },
            {
                'IP address': '206.189.47.247',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1814',
                'Reliability(%)': '88.89',
                'Details': 'Details',
            },
            {
                'IP address': '207.2.201.116',
                'Port': '1080',
                'Type': 'Socks4',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '97.62',
                'Details': 'Details',
            },
            {
                'IP address': '207.237.36.181',
                'Port': '60248',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '84.17',
                'Details': 'Details',
            },
            {
                'IP address': '209.181.248.29',
                'Port': '9050',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '97.18',
                'Details': 'Details',
            },
            {
                'IP address': '216.1.75.152',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1153',
                'Reliability(%)': '98.01',
                'Details': 'Details',
            },
            {
                'IP address': '216.172.56.41',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '0.55',
                'Details': 'Details',
            },
            {
                'IP address': '23.226.93.13',
                'Port': '19183',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '49.97',
                'Details': 'Details',
            },
            {
                'IP address': '34.217.107.89',
                'Port': '8888',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '715',
                'Reliability(%)': '97.22',
                'Details': 'Details',
            },
            {
                'IP address': '34.231.247.236',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '474',
                'Reliability(%)': '88.89',
                'Details': 'Details',
            },
            {
                'IP address': '34.239.167.200',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '306',
                'Reliability(%)': '88.89',
                'Details': 'Details',
            },
            {
                'IP address': '34.240.231.232',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '8909',
                'Reliability(%)': '63.7',
                'Details': 'Details',
            },
            {
                'IP address': '35.162.122.16',
                'Port': '8888',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '471',
                'Reliability(%)': '90.91',
                'Details': 'Details',
            },
            {
                'IP address': '35.182.108.144',
                'Port': '80',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '13996',
                'Reliability(%)': '80.95',
                'Details': 'Details',
            },
            {
                'IP address': '35.196.22.227',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '328',
                'Reliability(%)': '83.33',
                'Details': 'Details',
            },
            {
                'IP address': '35.196.56.10',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '310',
                'Reliability(%)': '83.33',
                'Details': 'Details',
            },
            {
                'IP address': '40.114.14.173',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '12079',
                'Reliability(%)': '60.97',
                'Details': 'Details',
            },
            {
                'IP address': '45.32.193.119',
                'Port': '8124',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '5012',
                'Reliability(%)': '46.08',
                'Details': 'Details',
            },
            {
                'IP address': '45.32.195.95',
                'Port': '8123',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '4630',
                'Reliability(%)': '44.46',
                'Details': 'Details',
            },
            {
                'IP address': '45.63.111.240',
                'Port': '8118',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '6006',
                'Reliability(%)': '52.85',
                'Details': 'Details',
            },
            {
                'IP address': '45.77.119.127',
                'Port': '8123',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '5577',
                'Reliability(%)': '55.42',
                'Details': 'Details',
            },
            {
                'IP address': '45.77.119.206',
                'Port': '8118',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '4147',
                'Reliability(%)': '54.43',
                'Details': 'Details',
            },
            {
                'IP address': '45.77.95.158',
                'Port': '8123',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1067',
                'Reliability(%)': '53.37',
                'Details': 'Details',
            },
            {
                'IP address': '47.254.22.115',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '10046',
                'Reliability(%)': '97.22',
                'Details': 'Details',
            },
            {
                'IP address': '47.35.79.9',
                'Port': '24618',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '16.66',
                'Details': 'Details',
            },
            {
                'IP address': '47.52.153.167',
                'Port': '443',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '13776',
                'Reliability(%)': '76.19',
                'Details': 'Details',
            },
            {
                'IP address': '47.52.231.140',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1316',
                'Reliability(%)': '97.05',
                'Details': 'Details',
            },
            {
                'IP address': '47.74.9.208',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '807',
                'Reliability(%)': '97.22',
                'Details': 'Details',
            },
            {
                'IP address': '47.75.0.253',
                'Port': '8081',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '981',
                'Reliability(%)': '83.49',
                'Details': 'Details',
            },
            {
                'IP address': '47.75.152.236',
                'Port': '3128',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '8772',
                'Reliability(%)': '71.43',
                'Details': 'Details',
            },
            {
                'IP address': '47.75.48.133',
                'Port': '1080',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '88.85',
                'Details': 'Details',
            },
            {
                'IP address': '47.89.10.103',
                'Port': '80',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1481',
                'Reliability(%)': '98.82',
                'Details': 'Details',
            },
            {
                'IP address': '47.89.22.200',
                'Port': '80',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '5914',
                'Reliability(%)': '99.18',
                'Details': 'Details',
            },
            {
                'IP address': '47.89.241.103',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '379',
                'Reliability(%)': '98.33',
                'Details': 'Details',
            },
            {
                'IP address': '47.90.63.202',
                'Port': '80',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1520',
                'Reliability(%)': '86.12',
                'Details': 'Details',
            },
            {
                'IP address': '47.90.72.227',
                'Port': '8088',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '977',
                'Reliability(%)': '99.32',
                'Details': 'Details',
            },
            {
                'IP address': '47.90.87.225',
                'Port': '88',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1009',
                'Reliability(%)': '86.68',
                'Details': 'Details',
            },
            {
                'IP address': '47.91.139.78',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '3008',
                'Reliability(%)': '94.42',
                'Details': 'Details',
            },
            {
                'IP address': '47.91.165.126',
                'Port': '80',
                'Type': 'Transparent',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1369',
                'Reliability(%)': '99.32',
                'Details': 'Details',
            },
            {
                'IP address': '50.198.134.65',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '793',
                'Reliability(%)': '86.66',
                'Details': 'Details',
            },
            {
                'IP address': '50.202.139.150',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '375',
                'Reliability(%)': '99.14',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.32',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '250',
                'Reliability(%)': '97.43',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.33',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1001',
                'Reliability(%)': '97.65',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.35',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '7231',
                'Reliability(%)': '98.01',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.36',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '280',
                'Reliability(%)': '97.26',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.37',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '588',
                'Reliability(%)': '98.38',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.38',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '231',
                'Reliability(%)': '98.61',
                'Details': 'Details',
            },
            {
                'IP address': '50.233.137.39',
                'Port': '80',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '230',
                'Reliability(%)': '98.67',
                'Details': 'Details',
            },
            {
                'IP address': '52.187.144.187',
                'Port': '80',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '1683',
                'Reliability(%)': '93.48',
                'Details': 'Details',
            },
            {
                'IP address': '54.183.251.107',
                'Port': '8088',
                'Type': 'Anonymous',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '572',
                'Reliability(%)': '77.78',
                'Details': 'Details',
            },
            {
                'IP address': '54.245.217.100',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '623',
                'Reliability(%)': '97.22',
                'Details': 'Details',
            },
            {
                'IP address': '64.71.130.34',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '6312',
                'Reliability(%)': '62.31',
                'Details': 'Details',
            },
            {
                'IP address': '66.82.144.29',
                'Port': '8080',
                'Type': 'Anonymous',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '363',
                'Reliability(%)': '76.26',
                'Details': 'Details',
            },
            {
                'IP address': '67.52.84.206',
                'Port': '48678',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '6923',
                'Reliability(%)': '46.49',
                'Details': 'Details',
            },
            {
                'IP address': '67.78.143.182',
                'Port': '8080',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '474',
                'Reliability(%)': '97.98',
                'Details': 'Details',
            },
            {
                'IP address': '70.88.158.166',
                'Port': '3389',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '9.66',
                'Details': 'Details',
            },
            {
                'IP address': '71.191.75.67',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '9665',
                'Reliability(%)': '94.63',
                'Details': 'Details',
            },
            {
                'IP address': '71.94.37.238',
                'Port': '25264',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '75.151.213.85',
                'Port': '3366',
                'Type': 'Socks4',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '78.69',
                'Details': 'Details',
            },
            {
                'IP address': '76.227.128.22',
                'Port': '7000',
                'Type': 'Socks4',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '100',
                'Details': 'Details',
            },
            {
                'IP address': '96.85.35.233',
                'Port': '3128',
                'Type': 'Distorting',
                'SSL': 'false',
                'Country': '\xa0United States\n',
                'Latency(msec)': '25897',
                'Reliability(%)': '67.54',
                'Details': 'Details',
            },
            {
                'IP address': '98.174.87.168',
                'Port': '13574',
                'Type': 'Socks5',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '30',
                'Reliability(%)': '6.08',
                'Details': 'Details',
            },
            {
                'IP address': '98.191.98.146',
                'Port': '3128',
                'Type': 'Transparent',
                'SSL': 'true',
                'Country': '\xa0United States\n',
                'Latency(msec)': '609',
                'Reliability(%)': '97.02',
                'Details': 'Details',
            },
            {},
        ]
    ]


def test_tables_with_thead():
    html_string = _read_file('./data/Free Proxy Lists.html')
    tables = html_to_json.convert_tables(html_string)
    assert len(tables) == 1
