#!/usr/bin/env python3

import json
import os
import time
from typing import Callable, Any
from zbig.zhash.args import args_hash


# 使用 json 缓存函数


# 默认 4 小时: 14400 秒
def cache(life_second: int = 14400) -> Callable:
    # check is file modify time in 4 hours
    def check_file_is_alive(file_name: str) -> bool:
        file = f"{file_name}.json"
        if not os.path.exists(file):
            return False
        # get the modify time of the file
        modify_time = os.path.getmtime(file)
        # get the current time
        current_time = time.time()
        # check if the file modify time is out of 4 hours ago
        return current_time - modify_time <= life_second

    def read_from_file(file_name: str) -> Any:
        with open(f"{file_name}.json", "r", encoding="utf-8") as outfile:
            data = json.load(outfile)
        return data

    def save_to_file(file_name: str, content: Any) -> None:
        # Create directory if it doesn't exist
        cache_dir = os.path.dirname(f"{file_name}.json")
        if cache_dir and not os.path.exists(cache_dir):
            os.makedirs(cache_dir, exist_ok=True)
        
        with open(f"{file_name}.json", "w", encoding="utf-8") as outfile:
            json.dump(content, outfile, ensure_ascii=False, separators=(',', ':'))

    def decorator(fn: Callable) -> Callable:
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            # 用函数名和入参作为 key
            hash_name = args_hash(*args, **kwargs)
            file_name = f"{fn.__name__}_{hash_name}"
            if check_file_is_alive(file_name):
                res = read_from_file(file_name)
                if res:
                    return res
            res = fn(*args, **kwargs)
            save_to_file(file_name, res)
            return res

        return wrapped

    return decorator


@cache()
def get_token(name: str):
    """
    >>> get_token("bigzhu")
    fu
    """
    # imaginary API call to get token
    return {"name": name, "time": time.time()}


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
