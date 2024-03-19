#!/usr/bin/env python
import json


# Print JSON data with indentation
def json_print(data, indent=4):
    """

    Args:
        data:
        indent:

    >>> json_print({"name": "BigZhu", "age": 18})
    {
        "name": "BigZhu",
        "age": 18
    }
    """
    print(json.dumps(data, indent=indent))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
