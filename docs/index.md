# NeoPika - Python Query Builder

[![Build Status](https://travis-ci.org/kayak/neopika.svg?branch=master)](https://travis-ci.org/kayak/neopika)
[![Coverage Status](https://coveralls.io/repos/kayak/neopika/badge.svg?branch=master)](https://coveralls.io/r/kayak/neopika?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d7e44e5628b4839a23da0bd82eaafcf)](https://www.codacy.com/app/twheys/neopika)
[![Documentation Status](https://readthedocs.org/projects/neopika/badge/?version=latest)](http://neopika.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/neopika.svg)](https://badge.fury.io/py/neopika)
[![License](https://img.shields.io/pypi/l/neopika.svg)](https://pypi.python.org/pypi/neopika/)

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