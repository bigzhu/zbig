# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`zbig` is a personal Python utility library by bigzhu containing various helper modules for common development tasks. The library is organized into focused modules under the `zbig/` package.

## Development Commands

### Quick Commands (using Makefile)
- **Setup development environment**: `make dev-setup`
- **Run all checks**: `make check` (lint + type-check + test)
- **Run tests with coverage**: `make test-cov`
- **Format code**: `make format`
- **Run doctests**: `make doctest`
- **Build and publish**: `make publish`

### Package Management
- **Install dependencies**: `poetry install`
- **Build package**: `poetry build`
- **Publish**: `poetry publish`

### Testing
- **Run tests**: `poetry run pytest`
- **Run tests with coverage**: `poetry run pytest --cov=zbig --cov-report=html`
- **Run doctests**: Each module can be executed directly to run its doctests:
  ```bash
  poetry run python zbig/zfile/zcsv.py
  poetry run python zbig/ztelegram/send.py
  poetry run python zbig/ztime/cn_now.py
  poetry run python zbig/zhash/args.py
  poetry run python zbig/zcache/json_cache.py
  ```

### Code Quality
- **Lint**: `poetry run ruff check zbig`
- **Format**: `poetry run ruff format zbig`
- **Type check**: `poetry run mypy zbig`
- **Pre-commit hooks**: `pre-commit run --all-files`

## Architecture

The project follows a modular structure with each utility grouped by purpose:

### Core Modules

- **`zbig.zfile`**: File operations, primarily CSV handling (`zcsv.py`)
  - Functions: `read_csv()`, `write_csv_append()`, `write_csv_delete()`, `is_duplicate()`
  
- **`zbig.ztelegram`**: Telegram bot integration (`send.py`, `define.py`)
  - Functions: `send_message()`, `send_photo()`
  - Requires environment variables for bot configuration
  
- **`zbig.zprint`**: Enhanced printing and table formatting (`table.py`, `json_print.py`)
  - Supports Unicode/CJK characters with proper width calculation
  - Functions: `table()`, `curses_table()` for real-time refreshing tables
  
- **`zbig.ztime`**: Time utilities (`cn_now.py`)
  - China timezone-aware datetime formatting
  
- **`zbig.zcache`**: JSON-based function caching (`json_cache.py`)
  - Decorator `@cache()` with configurable TTL (default 4 hours)
  
- **`zbig.zhash`**: Hashing utilities (`args.py`)
  - Function: `args_hash()` for generating consistent hashes from function arguments

### Key Patterns

- All modules use doctest for testing and documentation
- Each module can be run standalone to execute its doctests
- Functions use type hints where applicable
- Error handling with appropriate Python exceptions
- File operations default to UTF-8 encoding with Unix line endings

### Dependencies

- **Core**: `pyTelegramBotAPI`, `pytz`, `environs`, `schedule`
- **Dev**: `pytest`, `pytest-cov`, `ruff`, `mypy`, `pre-commit`
- **Python**: Requires 3.10+

### Code Quality Tools

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **Pre-commit**: Git hooks for code quality
- **GitHub Actions**: Automated CI/CD pipeline

### Testing Strategy

- **pytest**: Main testing framework with coverage reporting
- **doctests**: Embedded in each module for documentation and testing
- **Type checking**: Full mypy coverage with strict settings
- **CI/CD**: Tests run on Python 3.10, 3.11, 3.12

## Development Notes

- The project uses Poetry for dependency management
- All modules include standalone doctest execution
- CSV operations include duplicate detection and validation
- Table printing handles Unicode characters correctly for international text
- Telegram functionality requires proper environment variable configuration
- Caching system generates hash-based filenames for function memoization