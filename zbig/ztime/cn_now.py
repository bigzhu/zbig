#!/usr/bin/env python
from datetime import datetime
import pytz

# China timezone (Shanghai)
CHINA_TIMEZONE = pytz.timezone("Asia/Shanghai")


def get_china_current_time() -> str:
    """
    Get current time in China timezone as formatted string.

    Returns:
        Formatted timestamp string in YYYY-MM-DD HH:MM:SS format

    >>> get_china_current_time()
    '2...-...-... ...:...:...'
    """
    china_datetime = datetime.now(CHINA_TIMEZONE)
    return china_datetime.strftime("%Y-%m-%d %H:%M:%S")


# Backward compatibility alias
cn_now = get_china_current_time


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
