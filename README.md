# NeoPika - Python Query Builder

[![Build Status](https://github.com/stainly/neopika/actions/workflows/ci.yml/badge.svg)](https://github.com/stainly/neopika/actions)
<!-- [![Docs](https://readthedocs.org/projects/neopika/badge/?version=latest)](http://neopika.readthedocs.io/en/latest/) -->
<!-- [![PyPi](https://img.shields.io/pypi/v/neopika.svg?style=flat)](https://pypi.python.org/pypi/neopika) -->
[![License](https://img.shields.io/hexpm/l/plug.svg?maxAge=2592000)](http://www.apache.org/licenses/LICENSE-2.0)

## Important Note

NeoPika is a fork of [PyPika](https://github.com/kayak/pypika), created to maintain and advance the project as the original repository has become unmaintained. While we maintain full compatibility with PyPika's core functionality, we are actively developing new features, fixing bugs, and improving the codebase. All modifications are made under the same Apache 2.0 license as the original project.

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

[Read the docs](http://neopika.readthedocs.io/en/latest/)

## Installation

NeoPika supports Python `3.6+`. It may also work on pypy, cython, and jython, but is not being tested for these versions.

To install NeoPika run the following command:

```bash
pip install neopika
```

## Tutorial

The main classes in neopika are `neopika.Query`, `neopika.Table`, and `neopika.Field`.

```python
from neopika import Query, Table, Field
```

For the complete tutorial and documentation, please visit our [documentation site](http://neopika.readthedocs.io/en/latest/).

## Contributing

We welcome community contributions to NeoPika. Please see our [contributing guide](CONTRIBUTING.md) for more info.

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
