#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert html to json."""

import bs4


def iterate(html_section, json_output):
    for part in html_section:
        if not isinstance(part, str):
            # for python2 - check if part is unicode
            try:
                string_is_unicode = isinstance(part, unicode)
            # for python3 - catch error when trying to use the name 'unicode'
            except NameError as e:
                string_is_unicode = False
            # no matter what - if part is not unicode, record it
            finally:
                if not string_is_unicode:
                    if not json_output.get(part.name):
                        json_output[part.name] = list()
                    
                    attribute_dict = dict()
                    if part.attrs:
                        attribute_dict = {
                            'attributes': part.attrs
                        }
                    json_output[part.name].append(iterate(part, attribute_dict))
                else:
                    if part != '\n' and part != '':
                        json_output['value'] = part
        else:
            if part != '\n' and part != '':
                json_output['value'] = part
    return json_output


def convert(html_string):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    l = [child for child in soup.contents]
    return iterate(l, {})
