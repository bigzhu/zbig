#!/usr/bin/env python3

import re
from zbig.ztime.cn_now import get_china_current_time


class TestZTime:
    """Test suite for ztime module."""

    def test_cn_now_format(self):
        """Test that get_china_current_time returns correct format."""
        result = get_china_current_time()
        # Should match YYYY-MM-DD HH:MM:SS format
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
        assert re.match(pattern, result)

    def test_cn_now_returns_string(self):
        """Test that get_china_current_time returns a string."""
        result = get_china_current_time()
        assert isinstance(result, str)
        assert len(result) == 19  # "YYYY-MM-DD HH:MM:SS" is 19 characters
