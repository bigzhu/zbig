#!/usr/bin/env python
import unicodedata
import curses
from collections.abc import Callable
from schedule import Job
import schedule

# 算出有几个非英文字符


def count_wide_characters(text: str) -> int:
    """Count the number of wide (CJK) characters in text."""
    return sum(unicodedata.east_asian_width(char) == "W" for char in text)


# 非英文字符都算2个长度, 加上去
def calculate_display_width(text: str) -> int:
    """Calculate the display width of text including wide characters."""
    return len(text) + count_wide_characters(text)


# 获取最长
def get_column_max_widths(table_rows: list) -> list[int]:
    """Calculate the maximum width for each column in the table."""
    column_widths = [0] * len(table_rows[0])
    for row_data in table_rows:
        for column_index in range(len(row_data)):
            cell_content = str(row_data[column_index])
            cell_width = calculate_display_width(cell_content)
            if cell_width > column_widths[column_index]:
                column_widths[column_index] = cell_width
    return column_widths


# 格式化并修复 ljust bug
def format_table_rows(table_rows: list, column_separator: str) -> list[str]:
    """Format table rows with proper alignment for wide characters."""
    column_widths = get_column_max_widths(table_rows)
    formatted_rows = []

    for row_data in table_rows:
        # Handle wide characters by adjusting padding
        formatted_cells = []
        for column_index in range(len(row_data)):
            cell_content = str(row_data[column_index])
            # Adjust padding to account for wide characters
            padding_width = column_widths[column_index] - count_wide_characters(
                cell_content
            )
            padded_cell = cell_content.ljust(padding_width)
            formatted_cells.append(padded_cell)

        formatted_rows.append(column_separator.join(formatted_cells))
    return formatted_rows


def print_table(table_data: list, column_separator: str = "  ") -> None:
    """
    Print a formatted table to stdout.

    Args:
        table_data: List of rows, where each row is a list of cell values
        column_separator: String to separate columns

    >>> data = [
    ...     ["User", "Host", "Descriptions"],
    ...     ["bigzhu", "ssh.entube.app", "digitalocean"],
    ... ]
    >>> print_table(data, "~")
    User  ~Host          ~Descriptions
    bigzhu~ssh.entube.app~digitalocean
    """
    formatted_rows = format_table_rows(table_data, column_separator)
    for formatted_row in formatted_rows:
        print(formatted_row)


# 刷新绘制, 不会重复输出表格内容
def display_live_table(
    data_provider: Callable, refresh_schedule: Job, column_separator: str = "    "
) -> None:
    """
    Display a table that refreshes automatically using curses.

    Args:
        data_provider: Function that returns table data
        refresh_schedule: Schedule object defining refresh interval
        column_separator: String to separate columns
    """
    screen = curses.initscr()

    def refresh_display():
        screen.clear()
        current_data = data_provider()
        formatted_rows = format_table_rows(current_data, column_separator)
        for formatted_row in formatted_rows:
            screen.addstr(formatted_row + "\n")
        screen.refresh()

    refresh_schedule.do(refresh_display)
    refresh_display()  # Initial display

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
