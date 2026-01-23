from src.problems.registry import list_algorithms, make_problem


def main() -> None:
    print("Algorithm Trainer")
    print("Available algorithms:", ", ".join(list_algorithms()))
    alg = input("Choose algorithm: ").strip().lower()

    problem = make_problem(alg)

    print("\n--- TASK ---")
    print(problem.prompt)

    user_answer = input("Your answer: ")
    res = problem.check_fn(user_answer)

    if res.is_correct:
        print("✅ Correct!")
    else:
        print("❌ Wrong.")
        print("Reason:", res.message)
        print("Expected (example):", res.expected)
        print("Your (cleaned):", res.got)


if __name__ == "__main__":
    main()
