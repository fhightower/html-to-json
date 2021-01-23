#!/usr/bin/env python
"""Convert html to json."""

import bs4


def _debug(debug, message, prefix=''):
    """Print the given message if debugging is true."""
    if debug:
        print('{}{}'.format(prefix, message))
        # add a newline after every message
        print('')


def _record_element_value(element, json_output):
    """Record the html element's value in the json_output."""
    element = element.strip()
    if element != '\n' and element != '':
        if json_output.get('_value'):
            json_output['_values'] = [json_output['_value']]
            json_output['_values'].append(element)
            del json_output['_value']
        elif json_output.get('_values'):
            json_output['_values'].append(element)
        else:
            json_output['_value'] = element


def _iterate(
    html_section,
    json_output,
    count,
    debug,
    capture_element_values,
    capture_element_attributes,
):
    _debug(debug, '========== Start New Iteration ==========', '    ' * count)
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
                    new_json_output_for_subparts = dict()
                    if part.attrs and capture_element_attributes:
                        new_json_output_for_subparts = {'_attributes': part.attrs}
                    count += 1
                    json_output[part.name].append(
                        _iterate(
                            part,
                            new_json_output_for_subparts,
                            count,
                            debug=debug,
                            capture_element_values=capture_element_values,
                            capture_element_attributes=capture_element_attributes,
                        )
                    )
                # this will only be true in python2 - handle an entry that is unicode
                else:
                    if capture_element_values:
                        _record_element_value(part, json_output)
        else:
            if capture_element_values:
                _record_element_value(part, json_output)
    return json_output


def convert(
    html_string,
    debug=False,
    capture_element_values=True,
    capture_element_attributes=True,
):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    l = [child for child in soup.contents]
    return _iterate(
        l,
        {},
        0,
        debug=debug,
        capture_element_values=capture_element_values,
        capture_element_attributes=capture_element_attributes,
    )
