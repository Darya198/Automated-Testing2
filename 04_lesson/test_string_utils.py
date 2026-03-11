import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('input_text, expected_output',
                         [
                             ('text', 'Text'),
                             ('12345', '12345'),
                             ('text and texts', 'Text and texts')
                             ])
def test_capitalise_positive(input_text, expected_output):
    my_text = StringUtils()
    assert my_text.capitalize(input_text) == expected_output


@pytest.mark.parametrize('input_text, expected_output',
                         [
                             ('', ''),
                             ('   ', '')
                             ])
def test_capitalise_negative(input_text, expected_output):
    my_text = StringUtils()
    with pytest.raises(AttributeError):
        my_text.capitalize(None)


@pytest.mark.parametrize('input_text, expected_output',
                         [
                             (' Text and texts', 'Text and texts'),
                             (' Text', 'Text'),
                             (' 12345', '12345')
                             ])
def test_trim_positive(input_text, expected_output):
    my_text = StringUtils()
    assert my_text.trim(input_text) == expected_output


@pytest.mark.parametrize('input_text, expected_output',
                         [
                             ('', ''),
                             ('   ', '')
                             ])
def test_trim_negative(input_text, expected_output):
    my_text = StringUtils()
    with pytest.raises(AttributeError):
        my_text.trim(None)


@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Text', 'T', True),
                             ('text', 't', True),
                             ('text', 'x', True),
                             ('12345', '5', True),
                             ('Text and texts', 'd', True)
                             ])
def test_contains_positive(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.contains(input_text, input_symbol) == expected_output


@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Text', 'G', False),
                             ('text', 'i', False),
                             ('text', 'd', False),
                             ('12345', '8', False),
                             ('Text and texts', 'h', False),
                             ('', '', True),
                             ('   ', '   ', True)
                             ])
def test_contains_negative(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.contains(input_text, input_symbol) == expected_output


@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Text', 'T', 'ext'),
                             ('Text', 't', 'Tex'),
                             ('12345', '3', '1245'),
                             ('12345', '34', '125'),
                             ('text', '', 'text')
                             ])
def test_delete_symbol_positive(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.delete_symbol(input_text, input_symbol) == expected_output


@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Text', 'f', 'Text'),
                             ('Text', 'K', 'Text'),
                             ('12345', '0', '12345'),
                             ('12345', '87', '12345'),
                             ('test string', 'z', 'test string'),
                             ('', 'a', ''),
                             ('', '', '')
                             ])
def test_delete_symbol_negative(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.delete_symbol(input_text, input_symbol) == expected_output
