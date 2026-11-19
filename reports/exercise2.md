# Bug reports for exercise2.py

Line: 13
Problem: The function incorrectly uses `min(x, low)` and then `max(low, ...)` which results in always returning `low` when `x < low`. The logic is flawed because `min(x, low)` should compare `x` with `high`, not `low`. 
Example: clamp(3, 1, 10) returns 1, expected 3
Fix: return max(low, min(x, high))
