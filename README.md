# Algorithms Trainer (CLI)

A small CLI app for training algorithms in an interview-style format:
it generates tasks, accepts your answers, checks them, and (later) will track progress & stats.

---

## What it does

- Choose a topic/algorithm (e.g. `toposort`, later: `bfs`, `dfs`, `dijkstra`, arrays, etc.)
- Get a generated (or fixed for MVP) task
- Enter your answer in the terminal
- The checker validates it and shows:
  - ✅ correct / ❌ wrong
  - a short reason (if wrong)
  - an example of a correct answer

---

## Features (MVP)

- CLI runner
- Topics list
- Task generation (currently: fixed example for Toposort, next: random DAG generator)
- Answer checker with input cleaning (strip/lowercase/whitespace collapse)
- Tests with `pytest`

---

Run

python3 -m src.algtrainer.cli

---

CLI commands(planned) 

algotrainer topics
algotrainer new toposort
algotrainer new dijkstra
algotrainer stats
algotrainer export --format json

Roadmap

Next
 Random DAG generator + difficulty levels for Toposort
 Add BFS / DFS tasks (graph generation + checker)
 Add Dijkstra task (weighted graph generation + checker)
Soon
 Progress tracking (attempt history)
 Stats (accuracy per topic, streaks)
 Export results (JSON/CSV)
Later
 More array topics (two pointers, sliding window, prefix sums)
 Explanation mode (show correct reasoning steps)

