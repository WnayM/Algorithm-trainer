from src.core.types import Problem, CheckResult

def test_check_cycle():
    def check_fn(user_text: str) -> CheckResult:
    got = user_text.strip()
    expected = "4"
    ok = (got == expected)

    return CheckResult(is_correct = ok, expected = expected, got = got )

    p = Problem(
        prompt = "2 + 2 = ?",
        expected = "4",
        check_fn = check_fn
    )

    res_ok = p.check_fn("4")
    assert res_ok.is_correct is True

    res_bad = p.check_fn("5")
    assert res_bad.is_correct is False
    assert res_bad.expected == "4"
    assert res_bad.got == "5"

