"""A friendly greeting package."""


def greet(name: str) -> str:
    """Return a greeting, using world for an empty name."""
    clean_name = name.strip() or "world"
    return f"Hello, {clean_name}!"
