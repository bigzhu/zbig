#!/usr/bin/env python3

import csv


def read_csv(file_path: str) -> tuple[list[str], list[list[str]]]:
    """
    Read CSV file and return header and data rows.

    Args:
        file_path: Path to the CSV file

    Returns:
        Tuple of (header_row, data_rows)

    >>> header, rows = read_csv("test_hosts.csv")
    >>> print(header)
    ['User', 'Host', 'Description']
    """
    data_rows: list[list[str]] = []
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header_row = next(csv_reader)
        data_rows.extend(iter(csv_reader))
    return header_row, data_rows


def append_csv_row(file_path: str, row_data: list[str]) -> None:
    """
    Append a new row to CSV file, checking for duplicates.

    Args:
        file_path: Path to the CSV file
        row_data: List of strings representing the row data

    Raises:
        ValueError: If the row already exists in the file
    """
    if is_duplicate_row(file_path, row_data):
        raise ValueError(f"Duplicate row data: {row_data}")

    with open(file_path, "a", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator="\n")
        csv_writer.writerow(row_data)


def delete_csv_row(file_path: str, row_index: int) -> None:
    """
    Delete a specific row from CSV file by index.

    Args:
        file_path: Path to the CSV file
        row_index: Index of the row to delete (0-based)

    >>> delete_csv_row("test_hosts.csv", 0)  # doctest: +SKIP
    """
    header, data_rows = read_csv(file_path)
    if row_index >= len(data_rows) or row_index < 0:
        raise ValueError(
            f"Row index {row_index} out of range. File has {len(data_rows)} rows"
        )

    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator="\n")
        csv_writer.writerow(header)
        for current_index, row_data in enumerate(data_rows):
            if current_index != row_index:
                csv_writer.writerow(row_data)


def is_duplicate_row(file_path: str, row_data: list[str]) -> bool:
    """
    Check if a row already exists in the CSV file.

    Args:
        file_path: Path to the CSV file
        row_data: List of strings representing the row data

    Returns:
        True if the row exists, False otherwise

    >>> is_duplicate_row("test_hosts.csv", ['bigzhu', 'ssh.entube.app', 'digitalocean'])
    True
    """
    _, existing_rows = read_csv(file_path)
    return any(existing_row == row_data for existing_row in existing_rows)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
