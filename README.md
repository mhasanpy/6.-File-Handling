# 6.-File-Handling
# 📁 File Handling in Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Beginner%20Friendly-brightgreen.svg)]()

A comprehensive guide to reading from and writing to files in Python. Learn how to persist data beyond program execution, work with different file modes, and handle common file operations safely.

## 📋 Overview

File handling allows your programs to save data permanently, read configuration files, process large datasets, and interact with external files. This repository provides hands-on examples demonstrating various file operations, from basic text file handling to working with CSV and JSON formats.

## 🎯 Topics Covered

### 📝 File Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| **Opening files** | Access files with different modes | `open("file.txt", "r")` |
| **Reading files** | Read entire file or line by line | `read()`, `readline()`, `readlines()` |
| **Writing files** | Write new content to files | `write()`, `writelines()` |
| **Appending files** | Add content to existing files | `open("file.txt", "a")` |
| **Closing files** | Free system resources | `file.close()` |
| **With statement** | Auto-close files (best practice) | `with open() as file:` |
| **File paths** | Work with absolute/relative paths | `./data/file.txt` |

### 🔧 File Modes

| Mode | Description | File Behavior |
|------|-------------|---------------|
| `"r"` | Read (default) | File must exist |
| `"w"` | Write | Creates new file, overwrites existing |
| `"a"` | Append | Creates new file, adds to existing |
| `"x"` | Exclusive creation | Fails if file exists |
| `"r+"` | Read and write | File must exist |
| `"w+"` | Write and read | Creates/overwrites file |
| `"b"` | Binary mode | For non-text files (e.g., `"rb"`, `"wb"`) |

### 📄 File Types Covered

- **Text files** (`.txt`) - Basic reading and writing
- **CSV files** (`.csv`) - Tabular data with `csv` module
- **JSON files** (`.json`) - Structured data with `json` module

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mhasanpy/6.-File-Handling.git
