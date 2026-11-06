# Example: split-bill

The demo project from the `bugfix-test-first` video. This folder holds the **fixed** version.

**The bug** ([BUG.md](BUG.md)): splitting ₹100 between 3 people charged ₹33.33 each, so the bill came to ₹99.99. All 3 existing tests still passed.

**What the skill made the agent do:**
1. Wrote `test_shares_add_up_to_exact_total` in [test_billing.py](test_billing.py)
2. Ran it and showed it failing (`[33.33, 33.33, 33.33] != [33.34, 33.33, 33.33]`)
3. Made the smallest fix in [billing.py](billing.py): count in whole paise and give the leftover paisa to the first people
4. Ran the full suite (4 passed, no existing test changed) and checked edge cases with [check_edges.py](check_edges.py)

Run it yourself (Python 3.9+, no dependencies):

```bash
python -m unittest -v
python check_edges.py
```

To see the bug, replace the body of `split_bill` after the `if` with:

```python
    share = round(total / people, 2)
    return [share] * people
```
