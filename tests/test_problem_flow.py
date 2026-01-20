from src.problems.arrays.toposort.problem import make_toposort_problem

def test_toposort_correct_answer():
    p = make_toposort_problem()
    res = p.check_fn("A B C E D")
    assert res.is_correct is True


def test_toposort_edge_violation():
    p = make_toposort_problem()
    res = p.check_fn("C A B D E")
    assert res.is_correct is False


def test_toposort_missing_node():
    p = make_toposort_problem()
    res = p.check_fn("A B C D") 
    assert res.is_correct is False
