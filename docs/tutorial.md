# Tutorial

The main classes in NeoPika are `neopika.Query`, `neopika.Table`, and `neopika.Field`.

```python
from neopika import Query, Table, Field
```

## Selecting Data

The entry point for building queries is `neopika.Query`. In order to select columns from a table, the table must
first be added to the query. For simple queries with only one table, tables and columns can be referenced using
strings. For more sophisticated queries a `neopika.Table` must be used.

```python
q = Query.from_('customers').select('id', 'fname', 'lname', 'phone')
```

To convert the query into raw SQL, it can be cast to a string.

```python
str(q)
```

Alternatively, you can use the `Query.get_sql()` function:

```python
q.get_sql()
```

## Tables, Columns, Schemas, and Databases

In simple queries like the above example, columns in the "from" table can be referenced by passing string names into
the `select` query builder function. In more complex examples, the `neopika.Table` class should be used. Columns can be
referenced as attributes on instances of `neopika.Table`.

```python
from neopika import Table, Query

customers = Table('customers')
q = Query.from_(customers).select(customers.id, customers.fname, customers.lname, customers.phone)
```

Both of the above examples result in the following SQL:

```sql
SELECT id,fname,lname,phone FROM customers
```

An alias for the table can be given using the `.as_` function on `neopika.Table`

```python
customers = Table('x_view_customers').as_('customers')
q = Query.from_(customers).select(customers.id, customers.phone)
```

```sql
SELECT id,phone FROM x_view_customers customers
```

A schema can also be specified. Tables can be referenced as attributes on the schema.

```python
from neopika import Table, Query, Schema

views = Schema('views')
q = Query.from_(views.customers).select(customers.id, customers.phone)
```

```sql
SELECT id,phone FROM views.customers
```

Also references to databases can be used. Schemas can be referenced as attributes on the database.

```python
from neopika import Table, Query, Database

my_db = Database('my_db')
q = Query.from_(my_db.analytics.customers).select(customers.id, customers.phone)
```

```sql
SELECT id,phone FROM my_db.analytics.customers
```

Results can be ordered by using the following syntax:

```python
from neopika import Order
Query.from_('customers').select('id', 'fname', 'lname', 'phone').orderby('id', order=Order.desc)
```

This results in the following SQL:

```sql
SELECT "id","fname","lname","phone" FROM "customers" ORDER BY "id" DESC
```

### Arithmetic

Arithmetic expressions can also be constructed using NeoPika. Operators such as `+`, `-`, `*`, and `/` are implemented
by `neopika.Field` which can be used simply with a `neopika.Table` or directly.

```python
from neopika import Field

q = Query.from_('account').select(
    Field('revenue') - Field('cost')
)
```

```sql
SELECT revenue-cost FROM accounts
```

Using `neopika.Table`:

```python
accounts = Table('accounts')
q = Query.from_(accounts).select(
    accounts.revenue - accounts.cost
)
```

```sql
SELECT revenue-cost FROM accounts
```

An alias can also be used for fields and expressions.

```python
q = Query.from_(accounts).select(
    (accounts.revenue - accounts.cost).as_('profit')
)
```

```sql
SELECT revenue-cost profit FROM accounts
```

More arithmetic examples:

```python
table = Table('table')
q = Query.from_(table).select(
    table.foo + table.bar,
    table.foo - table.bar,
    table.foo * table.bar,
    table.foo / table.bar,
    (table.foo+table.bar) / table.fiz,
)
```

```sql
SELECT foo+bar,foo-bar,foo*bar,foo/bar,(foo+bar)/fiz FROM table
```

### Filtering

Queries can be filtered with `neopika.Criterion` by using equality or inequality operators

```python
customers = Table('customers')
q = Query.from_(customers).select(
    customers.id, customers.fname, customers.lname, customers.phone
).where(
    customers.lname == 'Mustermann'
)
```

```sql
SELECT id,fname,lname,phone FROM customers WHERE lname='Mustermann'
```

Query methods such as select, where, groupby, and orderby can be called multiple times. Multiple calls to the where
method will add additional conditions as:

```python
customers = Table('customers')
q = Query.from_(customers).select(
    customers.id, customers.fname, customers.lname, customers.phone
).where(
    customers.fname == 'Max'
).where(
    customers.lname == 'Mustermann'
)
```

```sql
SELECT id,fname,lname,phone FROM customers WHERE fname='Max' AND lname='Mustermann'
``` 