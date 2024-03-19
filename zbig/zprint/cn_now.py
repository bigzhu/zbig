from zbig import ztime


# print whith zh_now time
def cn_now(str_in: str):
    """

    Args:
        str_in:

    >>> cn_now('BigZhu')
    2...-... ... BigZhu
    >>> cn_now('こんにちは世界！')
    2...-... ... こんにちは世界！

    """
    t = ztime.cn_now()
    print(f"{t} {str_in}", flush=True)


if __name__ == "__main__":
    # cn_now("Hello, World!")
    # cn_now("你好，世界！")
    # cn_now("こんにちは世界！")
    # cn_now("안녕하세요 세계!")
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
