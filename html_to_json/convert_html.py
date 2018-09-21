#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert html to json."""

import bs4


def _debug(debug, message, prefix=''):
    """Print the given message if debugging is true."""
    if debug:
        print('{}{}'.format(prefix, message))
        # add a newline after every message
        print('')


def _iterate(html_section, json_output, count, debug):
    _debug(debug, '========== Start New Iteration ==========', '    '*count)
    _debug(debug, 'HTML_SECTION:\n{}'.format(html_section))
    _debug(debug, 'JSON_OUTPUT:\n{}'.format(json_output))
    for part in html_section:
        if not isinstance(part, str):
            # for python2 - check if part is unicode
            try:
                string_is_unicode = isinstance(part, unicode)
            # for python3 - catch error when trying to use the name 'unicode'
            except NameError as e:
                string_is_unicode = False
            # no matter what - keep going
            finally:
                # if part is not unicode, record it
                if not string_is_unicode:
                    if not json_output.get(part.name):
                        json_output[part.name] = list()
                    attribute_dict = dict()
                    if part.attrs:
                        attribute_dict = {
                            'attributes': part.attrs
                        }
                    count += 1
                    json_output[part.name].append(_iterate(part, attribute_dict, count, debug))
                # this will only be true in python2 - handle an entry that is unicode
                else:
                    part = part.strip()
                    if part != '\n' and part != '':
                        if json_output.get('value'):
                            json_output['values'] = [json_output['value']]
                            json_output['values'].append(part)
                            del json_output['value']
                        elif json_output.get('values'):
                            json_output['values'].append(part)
                        else:
                            json_output['value'] = part
        else:
            part = part.strip()
            if part != '\n' and part != '':
                if json_output.get('value'):
                    json_output['values'] = [json_output['value']]
                    json_output['values'].append(part)
                    del json_output['value']
                elif json_output.get('values'):
                    json_output['values'].append(part)
                else:
                    json_output['value'] = part
    return json_output


def convert(html_string, debug=False):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    l = [child for child in soup.contents]
    return _iterate(l, {}, 0, debug)
