# zbig - Big Zhu Python Utility Library

[![Test](https://github.com/bigzhu/zbig/actions/workflows/test.yml/badge.svg)](https://github.com/bigzhu/zbig/actions/workflows/test.yml)
[![Lint](https://github.com/bigzhu/zbig/actions/workflows/lint.yml/badge.svg)](https://github.com/bigzhu/zbig/actions/workflows/lint.yml)
[![PyPI version](https://badge.fury.io/py/zbig.svg)](https://badge.fury.io/py/zbig)
[![Python versions](https://img.shields.io/pypi/pyversions/zbig.svg)](https://pypi.org/project/zbig/)

一个包含各种实用工具的 Python 库，主要用于个人开发项目。

## 安装

```bash
pip install zbig
```

## 功能模块

### zfile - 文件操作
- CSV 文件读写操作
- 支持重复数据检测
- 批量数据处理

### ztelegram - Telegram 集成
- 消息发送
- 图片发送
- 支持中国时区时间戳

### zprint - 增强打印
- 表格格式化输出
- 支持中文字符宽度计算
- 实时刷新表格显示

### ztime - 时间工具
- 中国时区时间格式化
- 统一的时间戳格式

### zcache - 缓存工具
- JSON 文件缓存装饰器
- 可配置缓存生命周期
- 自动缓存清理
- UTF-8 支持与性能优化

### zhash - 哈希工具
- 函数参数哈希计算
- 一致性哈希生成

### zlog - 日志系统
- 统一的日志配置
- 多级别日志支持
- 灵活的格式化配置

### zconfig - 配置管理
- 环境变量管理
- .env 文件支持
- 配置验证机制

## 使用示例

```python
# CSV 操作
from zbig.zfile.zcsv import read_csv, write_csv_append

header, rows = read_csv("data.csv")
write_csv_append("data.csv", ["new", "row", "data"])

# 缓存装饰器
from zbig.zcache.json_cache import cache

@cache(life_second=3600)  # 1小时缓存
def expensive_function(param):
    # 耗时操作
    return result

# 时间格式化
from zbig.ztime.cn_now import cn_now
print(cn_now())  # 2024-01-01 12:00:00

# 表格打印
from zbig.zprint.table import table
table([['Name', 'Age'], ['Alice', '25']], "  ")
```

## 开发

### 环境设置

```bash
# 安装依赖
poetry install

# 安装预提交钩子
pre-commit install

# 运行测试
poetry run pytest

# 代码格式化
poetry run ruff format zbig

# 类型检查
poetry run mypy zbig
```

## 更新日志

### 0.1.20
- 添加完整的测试套件
- 改进类型注解
- 添加开发工具配置
- 修复拼写错误

### 0.1.14
- curses_table 自动刷新功能

### 0.1.13
- 增加 curses_table

### 0.1.9
- 支持非英文的 table print

## test

```bash
pytest
```
