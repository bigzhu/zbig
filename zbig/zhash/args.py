#!/usr/bin/env python
import hashlib


def _convert_to_bytes(input_value, encoding="utf-8"):
    """Convert input value to bytes with specified encoding."""
    if isinstance(input_value, str):
        return input_value.encode(encoding)
    return b"" if input_value is None else bytes(input_value)


def generate_arguments_hash(*positional_args, **keyword_args):
    """Calculate a hash value from function arguments.

    Given the same positional arguments and keyword arguments,
    this function will produce the same hash key.

    Args:
        *positional_args: Positional arguments
        **keyword_args: Keyword arguments

    Returns:
        SHA1 hash string of the arguments

    >>> generate_arguments_hash(name='bigzhu', age='18')
    '5505ff0b8f82e73373f86c22dcd91efdd59dcafb'
    """
    # Combine positional and keyword arguments
    all_items = list(positional_args) + [
        item for tuple_item in sorted(keyword_args.items()) for item in tuple_item
    ]
    # Convert None values to a consistent string representation
    normalized_items = ("__NoneType__" if item is None else item for item in all_items)
    # Create a string representation of all arguments
    arguments_string = "|".join(normalized_items)
    return hashlib.sha1(_convert_to_bytes(arguments_string)).hexdigest()


# Backward compatibility alias
args_hash = generate_arguments_hash


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
