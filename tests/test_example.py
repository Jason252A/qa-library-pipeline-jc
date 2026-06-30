"""Example test to demonstrate pytest.

Copy this pattern for your own tests!
"""

import pytest
import pandas as pd


@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'EndDate': ['a','b','c']
    })


#@pytest.mark.skip(reason="testing the skip")
def test_example_len(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3


def test_example_id(sample_df):
    """Example test - shows pytest working."""
    assert 'id' in sample_df.columns


def test_example_unique(sample_df):
    """Example test - shows pytest working."""
    assert sample_df['id'].is_unique


def test_example_sdate(sample_df):
    """Example test - shows pytest working."""
    assert 'StartDate' not in sample_df.columns


def test_example_edate(sample_df):
    """Example test - shows pytest working."""
    assert 'EndDate' in sample_df.columns