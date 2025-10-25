[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bGoygCWz)
# Team Standup Levels (BFS + Zigzag + Right-Side View)

## Story
You’re organizing standups for a binary org chart. You need:
- **level groups** for meeting waves,
- a **zigzag** intro order (left→right, then right→left),
- and the **right-side view** (who is visible if you look from the right).

## Task (What to Build)
In `src/levels.py`, implement:
- `level_order(root) -> list[list]`
- `zigzag_level_order(root) -> list[list]` (alternate direction each level)
- `right_side_view(root) -> list` (last node at each level)

**Node API:** `Node(val, left=None, right=None)`

## Hints
- Use a queue (`collections.deque`) and process one **level** at a time.
- Zigzag: reverse every odd-indexed level **after** collecting it.
- Right-side view: take the last value of each level.

## Run Tests Locally
```bash
python -m pytest -q
```

## Common Problems

- Reusing the same list across levels (leaks values between levels).
- Enqueuing None by accident.
- Doing DFS and getting the wrong order for BFS tasks.

## Complexity
- All functions: O(n) time, O(w) space, where w is the maximum level width.

## Example
```bash
    4
   / \
  2   6
 / \ / \
1  3 5  7

level_order -> [[4],[2,6],[1,3,5,7]]
zigzag_level_order -> [[4],[6,2],[1,3,5,7]]
right_side_view -> [4,6,7]
```