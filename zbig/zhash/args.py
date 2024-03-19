#!/usr/bin/env python
import hashlib


def _tob(_string, enc="utf8"):
    if isinstance(_string, str):
        return _string.encode(enc)
    return b"" if _string is None else bytes(_string)


def args_hash(*args, **kw):
    """Calculate a hash value from string args and kwargs.
    Given the same positional arguments and keyword
    arguments, this function will produce the same
    hash key.
    >>> args_hash(name='bigzhu', age='18')
    '5505ff0b8f82e73373f86c22dcd91efdd59dcafb'
    """
    items = list(args) + [i for t in sorted(kw.items()) for i in t]
    items = ("__NoneType__" if _i is None else _i for _i in items)
    # All items must be strings
    args_string = "|".join(items)
    return hashlib.sha1(_tob(args_string)).hexdigest()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
