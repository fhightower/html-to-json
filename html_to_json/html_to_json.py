#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert html to json."""

import bs4


def iterate(html_section, json_output):
    for part in html_section:
        if not isinstance(part, str):
            if not json_output.get(part.name):
                json_output[part.name] = list()
            json_output[part.name].append(iterate(part, {}))
        else:
            if part != '\n' and part != '':
                json_output['value'] = part
    return json_output


def convert(html_string):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    l = [child for child in soup.contents]
    return iterate(l, {})
