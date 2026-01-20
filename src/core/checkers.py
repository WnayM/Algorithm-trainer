from src.core.preprocess import TextPreprocessor
from src.core.types import CheckResult

def make_string_checker(expected: str, preprocessor: TextPreprocessor ):
    def check_fn(user_text: str ) -> CheckResult:

        got = preprocessor.clean_text(user_text)
        exp = preprocessor.clean_text(expected)
        ok = (got == exp)

        message = "OK" if ok else "WRONG"

        return CheckResult(is_correct = ok, expected = expected, got = got, message = message)

    return check_fn
