#!/usr/bin/env python3

import json
import os
import time
from typing import Callable, Any
from zbig.zhash.args import generate_arguments_hash


# 使用 json 缓存函数


# 默认 4 小时: 14400 秒
def json_cache(cache_lifetime_seconds: int = 14400) -> Callable:
    """
    Decorator for caching function results to JSON files.

    Args:
        cache_lifetime_seconds: Cache lifetime in seconds (default: 4 hours)

    Returns:
        Decorator function
    """

    def is_cache_file_valid(cache_file_base_name: str) -> bool:
        """Check if cache file exists and is within the lifetime."""
        cache_file_path = f"{cache_file_base_name}.json"
        if not os.path.exists(cache_file_path):
            return False

        file_modification_time = os.path.getmtime(cache_file_path)
        current_timestamp = time.time()
        return current_timestamp - file_modification_time <= cache_lifetime_seconds

    def load_cached_data(cache_file_base_name: str) -> Any:
        """Load data from cache file."""
        cache_file_path = f"{cache_file_base_name}.json"
        with open(cache_file_path, "r", encoding="utf-8") as cache_file:
            cached_data = json.load(cache_file)
        return cached_data

    def save_data_to_cache(cache_file_base_name: str, data_to_cache: Any) -> None:
        """Save data to cache file."""
        cache_file_path = f"{cache_file_base_name}.json"
        cache_directory = os.path.dirname(cache_file_path)

        if cache_directory and not os.path.exists(cache_directory):
            os.makedirs(cache_directory, exist_ok=True)

        with open(cache_file_path, "w", encoding="utf-8") as cache_file:
            json.dump(
                data_to_cache, cache_file, ensure_ascii=False, separators=(",", ":")
            )

    def cache_decorator(target_function: Callable) -> Callable:
        """The actual decorator function."""

        def cached_function_wrapper(*function_args: Any, **function_kwargs: Any) -> Any:
            # Generate cache key from function name and arguments
            arguments_hash = generate_arguments_hash(*function_args, **function_kwargs)
            cache_key = f"{target_function.__name__}_{arguments_hash}"

            # Try to load from cache first
            if is_cache_file_valid(cache_key):
                cached_result = load_cached_data(cache_key)
                if cached_result is not None:
                    return cached_result

            # Execute function and cache result
            function_result = target_function(*function_args, **function_kwargs)
            save_data_to_cache(cache_key, function_result)
            return function_result

        return cached_function_wrapper

    return cache_decorator


@json_cache()
def get_user_token(username: str):
    """
    Example function demonstrating cache usage.

    >>> get_user_token("bigzhu")
    {'name': 'bigzhu', 'timestamp': ...}
    """
    # Simulate API call to get token
    return {"name": username, "timestamp": time.time()}


# Backward compatibility alias
cache = json_cache


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
