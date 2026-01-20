from src.core.preprocess import TextPreprocessor, TextPreprocessorConfig

def test_lowercase_and_strip():
    p = TextPreprocessor(TextPreprocessorConfig(lowercase = True, strip = True))

    result = p.clean_text("     Hello")

    assert result == "hello"

def test_whitespace():
    t = TextPreprocessor(TextPreprocessorConfig(collapse_whitespace = True))

    result = t.clean_text("a b \n c")

    assert result == "a b c"

def test_max_lenght():
    s = TextPreprocessor(TextPreprocessorConfig(max_len = 3))

    result = s.clean_text("abcdef")

    assert result == "abc"

def test_min_lenght():
    l = TextPreprocessor(TextPreprocessorConfig(min_len = 2))

    result = l.clean_text("a")

    assert result == ""

def test_texts():
    m = TextPreprocessor(TextPreprocessorConfig(lowercase = True))

    result = m.clean_texts([None, "A", " B "])

    assert result == ["", "a", "b"]
