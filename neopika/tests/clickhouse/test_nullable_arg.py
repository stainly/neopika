import unittest

from parameterized import parameterized

from neopika import Field
from neopika.clickhouse.nullable_arg import IfNull
from neopika.clickhouse.type_conversion import ToFixedString


class TestSearchString(unittest.TestCase):
    @parameterized.expand(
        [
            (
                IfNull(Field("name"), Field("login")),
                "ifNull(name,login)",
            ),
            (
                IfNull(Field("builder"), ToFixedString("neopika", 100)),
                "ifNull(builder,toFixedString('neopika',100))",
            ),
        ]
    )
    def test_get_sql(self, func, expected):
        self.assertEqual(func.get_sql(), expected)
