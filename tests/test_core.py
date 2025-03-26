"""Tests for the mypackage.core module."""

from mypackage.core import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() == "Hello from mypackage!"
