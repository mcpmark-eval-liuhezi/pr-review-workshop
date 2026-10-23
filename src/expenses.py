"""Expense helpers for the code-review workshop demo."""

# Approximate rates to USD.
RATES = {
    "USD": 1.0,
    "EUR": 1.08,
    "JPY": 0.0064,
}


def convert_to_usd(amount, currency):
    """Convert an amount in the given currency to US dollars."""
    try:
        return amount * RATES[currency]
    except KeyError:
        pass  # unknown currency: nothing to do


def total_in_usd(expenses):
    """Return the combined total of the ledger in US dollars."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return round(total, 2)
