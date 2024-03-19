#!/usr/bin/env python
from datetime import datetime
import pytz

# Get the timezone object for China
tz_cn = pytz.timezone("Asia/Shanghai")


def cn_now() -> str:
    """

    >>> cn_now()
    '2...-...-... ...:...:...'

    """
    datetime_cn = datetime.now(tz_cn)
    return datetime_cn.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
