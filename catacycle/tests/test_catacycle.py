"""
Unit and regression test for the catacycle package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import catacycle


def test_catacycle_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "catacycle" in sys.modules
