"""Tests for the pubkit.core module."""
from pubkit.core import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() == "Hello from pubkit!" 