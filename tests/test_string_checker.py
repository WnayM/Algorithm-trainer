from src.core.preprocess import TextPreprocessor, TextPreprocessorConfig
from src.core.checkers import make_string_checker

def test_strip_works():
    p = TextPreprocessor(TextPreprocessorConfig(strip = True))
    check = make_string_checker("4", p)
    res = check(" 4 ")
    assert res.is_correct is True

def test_lowercase_works():
    p = TextPreprocessor(TextPreprocessorConfig(lowercase = True))
    check = make_string_checker("HELLO", p)
    res = check("hello")
    assert res.is_correct is True

def test_collapse_whitespace_works():
    p = TextPreprocessor(TextPreprocessorConfig(collapse_whitespace = True))
    check = make_string_checker("a b c", p)
    res = check("a      b\nc")
    assert res.is_correct is True
    