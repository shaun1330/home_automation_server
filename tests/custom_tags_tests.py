
from internet_of_things.templatetags.custom_filters import capitalize, dict_get, replace

def test_capitalize():
    value = "hello"
    expected = "Hello"
    output = capitalize(value)
    assert output == expected

def test_replace():
    value = "hello_world"
    expected = "hello+world"
    output = replace(value, "_,+")
    assert output == expected

def test_dict_get():
    value = {"foo": "bar", "hello": "world"}
    expected = "bar"
    output = dict_get(value, "foo")
    assert output == expected

def test_dict_get_none_case():
    value = {"foo": "bar", "hello": "world"}
    expected = ""
    output = dict_get(value, "chair")
    assert output == expected
