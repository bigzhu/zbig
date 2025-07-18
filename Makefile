.PHONY: install test lint format type-check clean build publish dev-setup

# 安装依赖
install:
	poetry install

# 开发环境设置
dev-setup: install
	poetry run pre-commit install

# 运行测试
test:
	poetry run pytest

# 运行测试并生成覆盖率报告
test-cov:
	poetry run pytest --cov=zbig --cov-report=html --cov-report=term

# 代码检查
lint:
	poetry run ruff check zbig

# 代码格式化
format:
	poetry run ruff format zbig

# 类型检查
type-check:
	poetry run mypy zbig

# 运行所有检查
check: lint type-check test

# 清理缓存文件
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/

# 构建包
build: clean
	poetry build

# 发布到 PyPI
publish: build
	poetry publish

# 运行 doctests
doctest:
	poetry run python zbig/zfile/zcsv.py
	poetry run python zbig/ztelegram/send.py
	poetry run python zbig/ztime/cn_now.py
	poetry run python zbig/zhash/args.py
	poetry run python zbig/zcache/json_cache.py

# 开发模式：监听文件变化并运行测试
watch:
	poetry run ptw --runner "python -m pytest"