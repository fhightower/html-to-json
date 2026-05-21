#!/usr/bin/env python

import html_to_json


def test_empty_dict_returns_empty_string():
    assert html_to_json.json_to_html({}) == ''


def test_simple_value():
    assert html_to_json.json_to_html({'p': [{'_value': 'hello'}]}) == '<p>hello</p>'


def test_multiple_values():
    assert html_to_json.json_to_html({'p': [{'_values': ['a', 'b']}]}) == '<p>ab</p>'


def test_attributes():
    json_input = {'a': [{'_attributes': {'href': 'https://example.com'}, '_value': 'link'}]}
    assert html_to_json.json_to_html(json_input) == '<a href="https://example.com">link</a>'


def test_void_element_no_closing_tag():
    assert html_to_json.json_to_html({'br': [{}]}) == '<br>'


def test_void_element_with_attributes():
    json_input = {'meta': [{'_attributes': {'charset': 'UTF-8'}}]}
    assert html_to_json.json_to_html(json_input) == '<meta charset="UTF-8">'


def test_class_attribute_list_is_space_joined():
    json_input = {'div': [{'_attributes': {'class': ['foo', 'bar']}, '_value': 'x'}]}
    assert html_to_json.json_to_html(json_input) == '<div class="foo bar">x</div>'


def test_nested_elements():
    json_input = {
        'head': [
            {
                'title': [{'_value': "Floyd's"}],
                'meta': [{'_attributes': {'charset': 'UTF-8'}}],
            }
        ]
    }
    expected = '<head><title>Floyd\'s</title><meta charset="UTF-8"></head>'
    assert html_to_json.json_to_html(json_input) == expected


def test_special_characters_are_escaped():
    json_input = {'p': [{'_value': '<script>alert("x")</script>'}]}
    expected = '<p>&lt;script&gt;alert("x")&lt;/script&gt;</p>'
    assert html_to_json.json_to_html(json_input) == expected


def test_quotes_in_text_are_not_escaped():
    json_input = {'p': [{'_value': 'say "hi" & \'bye\''}]}
    assert html_to_json.json_to_html(json_input) == '<p>say "hi" &amp; \'bye\'</p>'


def test_attribute_values_are_escaped():
    json_input = {'a': [{'_attributes': {'title': 'He said "hi"'}, '_value': 'x'}]}
    expected = '<a title="He said &quot;hi&quot;">x</a>'
    assert html_to_json.json_to_html(json_input) == expected


def test_repeated_tags_preserve_order():
    json_input = {
        'ul': [
            {
                'li': [
                    {'_value': 'one'},
                    {'_value': 'two'},
                    {'_value': 'three'},
                ]
            }
        ]
    }
    assert html_to_json.json_to_html(json_input) == '<ul><li>one</li><li>two</li><li>three</li></ul>'


def test_roundtrip_simple():
    html = "<head><title>Test</title><meta charset=\"UTF-8\"></head>"
    json_output = html_to_json.convert(html)
    assert html_to_json.json_to_html(json_output) == html


def test_roundtrip_with_nested_anchors():
    html = '<ul><li><a href="/a">A</a></li><li><a href="/b">B</a></li></ul>'
    json_output = html_to_json.convert(html)
    assert html_to_json.json_to_html(json_output) == html


def test_roundtrip_lang_attribute_preserved():
    html = '<html lang="en"><head><meta charset="utf-8"></head><body></body></html>'
    json_output = html_to_json.convert(html)
    assert html_to_json.json_to_html(json_output) == html


def test_modify_then_convert_back():
    """The core use case from issue #23: convert -> modify -> convert back."""
    html = '<div><p>old text</p></div>'
    json_output = html_to_json.convert(html)
    json_output['div'][0]['p'][0]['_value'] = 'new text'
    assert html_to_json.json_to_html(json_output) == '<div><p>new text</p></div>'


def test_boolean_attribute_true_renders_bare():
    json_input = {'input': [{'_attributes': {'type': 'checkbox', 'checked': True}}]}
    assert html_to_json.json_to_html(json_input) == '<input type="checkbox" checked>'


def test_boolean_attribute_false_omitted():
    json_input = {'input': [{'_attributes': {'type': 'checkbox', 'checked': False}}]}
    assert html_to_json.json_to_html(json_input) == '<input type="checkbox">'


def test_non_list_tag_value_is_skipped():
    """Defensively ignore malformed nodes whose tag value isn't a list."""
    json_input = {'div': [{'_value': 'keep', 'p': 'not a list'}]}
    assert html_to_json.json_to_html(json_input) == '<div>keep</div>'
