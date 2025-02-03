"""
NeoPika is divided into a couple of modules, primarily the ``queries`` and ``terms`` modules.

neopika.analytics
----------------

Wrappers for SQL analytic functions

neopika.dialects
---------------

This contains all of the dialect specific implementations of the ``Query`` class.

neopika.enums
------------

Enumerated values are kept in this package which are used as options for Queries and Terms.

neopika.functions
----------------

Wrappers for common SQL functions are stored in this package.

neopika.pseudocolumns
--------------------

Wrappers for common SQL pseudocolumns are stored in this package.

neopika.queries
--------------

This is where the ``Query`` class can be found which is the core class in NeoPika.  Also, other top level classes such
as ``Table`` can be found here.  ``Query`` is a container that holds all of the ``Term`` types together and also
serializes the builder to a string.

neopika.terms
------------

This module contains the classes which represent individual parts of queries that extend the ``Term`` base class.

neopika.utils
------------

This contains all of the utility classes such as exceptions and decorators.
"""

# noinspection PyUnresolvedReferences
from neopika.dialects import (
    ClickHouseQuery,
    Dialects,
    MSSQLQuery,
    MySQLQuery,
    OracleQuery,
    PostgreSQLQuery,
    RedshiftQuery,
    SQLLiteQuery,
    VerticaQuery,
)

# noinspection PyUnresolvedReferences
from neopika.enums import (
    DatePart,
    JoinType,
    Order,
)

# noinspection PyUnresolvedReferences
from neopika.queries import (
    AliasedQuery,
    Query,
    Schema,
    Table,
    Column,
    Database,
    make_tables as Tables,
    make_columns as Columns,
)

# noinspection PyUnresolvedReferences
from neopika.terms import (
    Array,
    Bracket,
    Case,
    Criterion,
    EmptyCriterion,
    Field,
    Index,
    Interval,
    JSON,
    Not,
    NullValue,
    SystemTimeValue,
    Parameter,
    QmarkParameter,
    NumericParameter,
    NamedParameter,
    FormatParameter,
    PyformatParameter,
    Rollup,
    Tuple,
    CustomFunction,
)

# noinspection PyUnresolvedReferences
from neopika.utils import (
    CaseException,
    GroupingException,
    JoinException,
    QueryException,
    RollupException,
    SetOperationException,
    FunctionException,
)


__author__ = "Timothy Heys"
__email__ = "theys@kayak.com"
__version__ = "0.48.9"

NULL = NullValue()
SYSTEM_TIME = SystemTimeValue()

__all__ = (
    'ClickHouseQuery',
    'Dialects',
    'MSSQLQuery',
    'MySQLQuery',
    'OracleQuery',
    'PostgreSQLQuery',
    'RedshiftQuery',
    'SQLLiteQuery',
    'VerticaQuery',
    'DatePart',
    'JoinType',
    'Order',
    'AliasedQuery',
    'Query',
    'Schema',
    'Table',
    'Column',
    'Database',
    'Tables',
    'Columns',
    'Array',
    'Bracket',
    'Case',
    'Criterion',
    'EmptyCriterion',
    'Field',
    'Index',
    'Interval',
    'JSON',
    'Not',
    'NullValue',
    'SystemTimeValue',
    'Parameter',
    'QmarkParameter',
    'NumericParameter',
    'NamedParameter',
    'FormatParameter',
    'PyformatParameter',
    'Rollup',
    'Tuple',
    'CustomFunction',
    'CaseException',
    'GroupingException',
    'JoinException',
    'QueryException',
    'RollupException',
    'SetOperationException',
    'FunctionException',
    'NULL',
    'SYSTEM_TIME',
)
