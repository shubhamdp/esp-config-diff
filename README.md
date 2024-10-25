# esp-config-diff

`esp-config-diff` is a Python command-line tool for comparing two configuration
files and displaying differences. It highlights added, removed, and modified
configuration values, making it easy to track changes between versions. 

## Features

- Compare two configuration files and output the differences.
- Color-coded output to distinguish between added, removed, and modified entries.
- Option to disable colors for plain-text output.
- Can be used as a standalone command-line tool or within a Python script.

---

## Installation

```
python3 -m pip install esp-config-diff
```

## Usage

### Basic Usage
```
esp-config-diff --conf sdkconfig --old-conf sdkconfig.old
```

### Disabling Color Output
```
esp-config-diff --conf sdkconfig --old-conf sdkconfig.old --no-color
```

### Example output
```
CONFIG                       Old Value    New Value
===================================================
CONFIG_FEATURE_ENABLED       ABSENT       true
CONFIG_MAX_CONNECTIONS       10           20
CONFIG_TIMEOUT               300          ABSENT
```
