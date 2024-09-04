import pytest
from string_utils import StringUtils

utils = StringUtils()

#capitilize
@pytest.mark.parametrize("text_1, text_2", [
    ("hello", "Hello"),
    ("как дела?", "Как дела?"),
    ("6547", "6547"),
    ("приvet700", "Приvet700"),
    (" ", " "),
    ("", ""),
    ("!^", "!^")
])
def test_capitilize(text_1, text_2):
    assert utils.capitilize(text_1) == (text_2)

#trim
@pytest.mark.parametrize("text1, text2", [
    (" hello", "hello"),
    (" как дела?", "как дела?"),
    (" YES", "YES"),
    (" ", ""),
    ("", ""),
    ("привет", "привет")
])
def test_trim(text1, text2):
    assert utils.trim(text1) == (text2)

@pytest.mark.xfail()
def test_trim_numbers():
     assert utils.trim(6547) == "6547"

# to_list
@pytest.mark.parametrize('string, delimeter, result', [
    ("один,два,три", ",", ["один", "два", "три"]),
    ("one,two,three", ",", ["one", "two", "three"]),
    ("1,2,3", ",", ["1", "2", "3"]),
    ("", None, []),
    ("1 2 3 4", None, ["1 2 3 4"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

#contains
@pytest.mark.parametrize('string, symbol, result', [
    ("солнце", "л", True),
    ("Hello", "o", True),
    ("что-то", "-", True),
    ("456", "5", True),
    ("", "", True),
    ("привет", "а", False),
    ("", "g", False),
    ("6789", "0", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

#delete_symbol
@pytest.mark.parametrize('string, symbol, result', [
    ("солнце", "л", "сонце"),
    ("Hello", "o", "Hell"),
    ("что-то", "-", "чтото"),
    ("456", "5", "46"),
    ("", "", ""),
    (" ", "g", " "),
    ("привет", "", "привет"),
    ("6789", " ", "6789")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result
    
#starts_with
@pytest.mark.parametrize('string, symbol, result', [
    ("солнце", "с", True),
    ("Hello", "H", True),
    ("что-то", "ч", True),
    ("456", "4", True),
    ("", "", True),
    ("Hello", "h", False),
    ("привет", "а", False),
    ("", "g", False),
    ("6789", "0", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

#end_with
@pytest.mark.parametrize('string, symbol, result', [
    ("солнце", "е", True),
    ("Hello", "o", True),
    ("что-то", "о", True),
    ("456", "6", True),
    ("", "", True),
    ("привет", "а", False),
    ("", "g", False),
    ("6789", "0", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

#is_empty
@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("   ", True),
    ("привет", False),
    ("тут есть слово", False),
    ("6789", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

#list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
   (["a", "b", "c"], ",", "a, b, c"),
   (["1", "2", "3"], "", "123"),
   (["один", "два"], "-", "один-два"),
   (["один", "три"], "два", "одиндватри"),
   ([], None,""),
   ([], ",", "")
])
def list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result