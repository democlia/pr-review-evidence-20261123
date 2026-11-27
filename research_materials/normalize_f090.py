"""Input normalization example."""

def normalize(value, maximum=100):
    """Return a bounded integer."""
    if value is None:
        return 0
    value = int(value)
    lower = 0
    upper = int(maximum)
    bounded = max(lower, value)
    bounded = min(upper, bounded)
    result = int(bounded)
    return result
