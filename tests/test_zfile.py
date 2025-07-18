#!/usr/bin/env python3

import csv
import tempfile
import pytest
from pathlib import Path

from zbig.zfile.zcsv import read_csv, append_csv_row, delete_csv_row, is_duplicate_row


class TestZCSV:
    """Test suite for zcsv module."""

    def test_read_csv(self):
        """Test reading CSV files."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age", "City"])
            writer.writerow(["Alice", "25", "Beijing"])
            writer.writerow(["Bob", "30", "Shanghai"])
            temp_path = f.name

        try:
            header, rows = read_csv(temp_path)
            assert header == ["Name", "Age", "City"]
            assert len(rows) == 2
            assert rows[0] == ["Alice", "25", "Beijing"]
            assert rows[1] == ["Bob", "30", "Shanghai"]
        finally:
            Path(temp_path).unlink()

    def test_write_csv_append(self):
        """Test appending to CSV files."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", "25"])
            temp_path = f.name

        try:
            append_csv_row(temp_path, ["Bob", "30"])
            header, rows = read_csv(temp_path)
            assert len(rows) == 2
            assert rows[1] == ["Bob", "30"]
        finally:
            Path(temp_path).unlink()

    def test_write_csv_append_duplicate(self):
        """Test that duplicate data raises ValueError."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", "25"])
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Duplicate row data"):
                append_csv_row(temp_path, ["Alice", "25"])
        finally:
            Path(temp_path).unlink()

    def test_is_duplicate(self):
        """Test duplicate detection."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", "25"])
            temp_path = f.name

        try:
            assert is_duplicate_row(temp_path, ["Alice", "25"]) is True
            assert is_duplicate_row(temp_path, ["Bob", "30"]) is False
        finally:
            Path(temp_path).unlink()

    def test_write_csv_delete(self):
        """Test deleting rows from CSV."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", "25"])
            writer.writerow(["Bob", "30"])
            temp_path = f.name

        try:
            delete_csv_row(temp_path, 0)  # Delete first row (Alice)
            header, rows = read_csv(temp_path)
            assert len(rows) == 1
            assert rows[0] == ["Bob", "30"]
        finally:
            Path(temp_path).unlink()

    def test_write_csv_delete_invalid_index(self):
        """Test that invalid index raises ValueError."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", "25"])
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Row index .* out of range"):
                delete_csv_row(temp_path, 5)
        finally:
            Path(temp_path).unlink()
