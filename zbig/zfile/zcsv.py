#!/usr/bin/env python3

import csv


def read_csv(file_path: str) -> tuple:
    """

    Args:
        file_path:

    Returns:
    >>> header, rows = read_csv("hosts.csv")
    >>> print(header)
    ['User', 'Host', 'Description']
    >>> print(rows)
    [['bigzhu', 'ssh.entube.app', 'digitalocean'], ['root', 'google.com', 'just test']]

    """
    rows = []
    with open(file_path, "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows.extend(iter(csvreader))
    return header, rows


def write_csv_append(file_path: str, row: list):
    if is_duplicate(file_path, row):
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        raise ValueError(f"Duplicate data {row}")
    with open(file_path, "a") as file:
        # 默认是 windows 的换行结束符
        csvwriter = csv.writer(file, lineterminator="\n")
        csvwriter.writerow(row)


def write_csv_delete(file_path: str, number: int):
    """
    >>> write_csv_delete("hosts.csv", 15)
    """
    current_rows = read_csv(file_path)
    if len(current_rows) < number:
        raise ValueError(f"Does't exist number {number} data")
    with open(file_path, "w", newline="") as wrt:
        writer = csv.writer(wrt, lineterminator="\n")
        for row in current_rows:
            writer.writerow(row)


def is_duplicate(file_path: str, row: list) -> bool:
    """

    Args:
        file_path:
        row:

    Returns:
    >>> is_duplicate("hosts.csv", ['bigzhu', 'ssh.entube.app', 'digitalocean'])
    True
    """
    _, rows = read_csv(file_path)
    return any(r == row for r in rows)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
