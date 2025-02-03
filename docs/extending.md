# Extending NeoPika

## SQL Functions not included in NeoPika

NeoPika includes a couple of the most common SQL functions, but due to many differences between different SQL databases,
many are not included. Any SQL function can be implemented in NeoPika by extending the `neopika.terms.Function` class.

When defining SQL function wrappers, it is necessary to define the name of the SQL function as well as the arguments it
requires.

```python
from neopika.terms import Function

class CurDate(Function):
    def __init__(self, alias=None):
        super(CurDate, self).__init__('CURRENT_DATE', alias=alias)

q = Query.select(CurDate())
```

```python
from neopika.terms import Function

class DateDiff(Function):
    def __init__(self, interval, start_date, end_date, alias=None):
        super(DateDiff, self).__init__('DATEDIFF', interval, start_date, end_date, alias=alias)
```

There is also a helper function `neopika.CustomFunction` which enables 1-line creation of a SQL function wrapper.

```python
from neopika import CustomFunction

customers = Tables('customers')
DateDiff = CustomFunction('DATE_DIFF', ['interval', 'start_date', 'end_date'])

q = Query.from_(customers).select(
    customers.id,
    customers.fname,
    customers.lname,
    DateDiff('day', customers.created_date, customers.updated_date)
)
```

Similarly analytic functions can be defined by extending `neopika.terms.AnalyticFunction`.

```python
from neopika.terms import AnalyticFunction

class RowNumber(AnalyticFunction):
    def __init__(self, **kwargs):
        super(RowNumber, self).__init__('ROW_NUMBER', **kwargs)


q = Query.from_(self.table_abc) \
        .select(an.RowNumber()
                    .over(self.table_abc.foo)
                    .orderby(self.table_abc.date))
```

```sql
SELECT ROW_NUMBER() OVER(PARTITION BY "foo" ORDER BY "date") FROM "abc"
``` 