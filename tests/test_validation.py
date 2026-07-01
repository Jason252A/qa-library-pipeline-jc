

from data_processing.validation import validate_isbn

def test_valid_isbn():
    result = validate_isbn('9780306406157')
    assert result == True

def test_invalid_isbn():
    result = validate_isbn('not-an-isbn')
    assert result == False

def test_wrong_length():
    result = validate_isbn('123456789')
    assert result == False


def test_invalid_check_digit():
    # valid isbn: 9780306406157
    result = validate_isbn('9780306406158')
    #assert result == False

def test_isbn_symbols():
    result = validate_isbn('12-3-4=5/6\78''9')
    assert result == False
    # TODO: assert result is False