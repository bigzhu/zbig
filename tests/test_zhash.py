#!/usr/bin/env python3

from zbig.zhash.args import args_hash


class TestZHash:
    """Test suite for zhash module."""

    def test_args_hash_consistent(self):
        """Test that args_hash produces consistent results."""
        hash1 = args_hash("test", "data")
        hash2 = args_hash("test", "data")
        assert hash1 == hash2

    def test_args_hash_with_kwargs(self):
        """Test args_hash with keyword arguments."""
        hash1 = args_hash(name="bigzhu", age="18")
        hash2 = args_hash(name="bigzhu", age="18")
        assert hash1 == hash2
        assert hash1 == "5505ff0b8f82e73373f86c22dcd91efdd59dcafb"

    def test_args_hash_different_inputs(self):
        """Test that different inputs produce different hashes."""
        hash1 = args_hash("test1")
        hash2 = args_hash("test2")
        assert hash1 != hash2

    def test_args_hash_with_none(self):
        """Test args_hash handles None values."""
        hash1 = args_hash(None, "test")
        hash2 = args_hash(None, "test")
        assert hash1 == hash2

    def test_args_hash_order_independence(self):
        """Test that kwargs order doesn't affect hash."""
        hash1 = args_hash(name="test", age="25")
        hash2 = args_hash(age="25", name="test")
        assert hash1 == hash2
