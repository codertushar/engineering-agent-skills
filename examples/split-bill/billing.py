"""Split a restaurant bill between friends."""


def split_bill(total, people):
    """Return how much each person pays, in rupees (2 decimals)."""
    if people <= 0:
        raise ValueError("people must be at least 1")
    paise = round(total * 100)
    base, leftover = divmod(paise, people)
    # The first `leftover` people pay 1 paisa more, so shares add up exactly.
    return [(base + (1 if i < leftover else 0)) / 100 for i in range(people)]
