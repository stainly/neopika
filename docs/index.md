# NeoPika - Python Query Builder

[![Build Status](https://github.com/stainly/neopika/actions/workflows/ci.yml/badge.svg)](https://github.com/stainly/neopika/actions)
[![PyPI version](https://badge.fury.io/py/neopika.svg)](https://badge.fury.io/py/neopika)
[![License](https://img.shields.io/pypi/l/neopika.svg)](https://pypi.python.org/pypi/neopika/)

## Important Note

NeoPika is a fork of [PyPika](https://github.com/kayak/pypika), developed by the incredible poeple at Kayak! NeoPika was created to maintain and advance the project as the original repository has become unmaintained. While we maintain full compatibility with PyPika's core functionality, we are actively developing new features, fixing bugs, and improving the codebase. All modifications are made under the same Apache 2.0 license as the original project.

If you're coming from PyPika, you'll find all the functionality you're familiar with, plus additional improvements and modern tooling support (like `uv` for dependency management and `mkdocs` for documentation).

## Abstract

### What is NeoPika?

NeoPika is a Python API for building SQL queries. The motivation behind NeoPika is to provide a simple interface for
building SQL queries without limiting the flexibility of handwritten SQL. Designed with data analysis in mind, NeoPika
leverages the builder design pattern to construct queries to avoid messy string formatting and concatenation. It is also
easily extended to take full advantage of specific features of SQL database vendors.

### What are the design goals for NeoPika?

NeoPika is a fast, expressive and flexible way to replace handwritten SQL (or even ORM for the courageous souls amongst you).
Validation of SQL correctness is not an explicit goal of NeoPika. With such a large number of
SQL database vendors providing a robust validation of input data is difficult. Instead you are encouraged to check inputs you provide to NeoPika or appropriately handle errors raised from
your SQL database - just as you would have if you were writing SQL yourself.
