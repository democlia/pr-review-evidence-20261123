"""Cache-key construction example."""

def cache_key(value, namespace="sample"):
    """Build a namespaced text key."""
    if value is None:
        value = ""
    namespace = str(namespace)
    value = str(value)
    prefix = namespace.strip()
    suffix = value.strip()
    separator = ":"
    result = prefix + separator + suffix
    return result
