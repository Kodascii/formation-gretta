<link rel="stylesheet" href="../../stylesheet.css">

# SQL Syntax

## RDBMS
**RDBMS** stands for *Relational Database Management System*. **RDBMS** is the basis for **SQL**, and for all modern database systems such as **MS SQL Server**, **IBM DB2**, **Oracle**, **MySQL**, and **Microsoft Access**.

## DATA TYPES
### STRINGS
| Data type                       | Description                                            |
|---------------------------------|--------------------------------------------------------|
| `CHAR(size)`                    | *A FIXED length string;* `size[0-255](default=1)`      |
| `VARCHAR(size)`                 | *A VARIABLE length string;* `size[0-65535]`            |
| `TEXT(size)`                    | *Holds a string with a maximum length of 65,535 bytes* |
| `ENUM(val1, val2, val3, ...)`   | *A string object that can have only one value, chosen from a list of possible values.* |
| `SET(val1, val2, val3, ...)`    | *A string object that can have 0 or more values, chosen from a lis²t of possible values. You can list up to 64 values in a SET list.* |

### NUMERICS
| Data type               | Description                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------|
| `BIT(size)`             | *A bit-value type.* `size[1-64](default=1)`                                                |
| `BOOL` / `BOOLEAN`      | *Zero is considered as false, nonzero values are considered as true.*                      |
| `INT` / `INTEGER(size)` | `size` *- specifies the maximum display width (which is 255)*                              |
| `FLOAT(p)`              | `p` *- value to determine whether to use `FLOAT` or `DOUBLE` for the resulting data type.* |



## OPERATIONS

### SEARCHING
```sql
SELECT column1, column2, ...
FROM table_name;
```

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```


### INSERTIONS
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### CONDITIONS
```sql
SELECT column1, column2, ...
FROM table_name
WHERE predicate;
```

> The following operators can be used in the `WHERE` clause:

| Operator  | Description                          |
|-----------|--------------------------------------|
| `=`       | Equal                                |
| `>`, `>=` | Greater (equal) than                 |
| `<`, `<=` | Less (equal) than                    |
| `<>`      | Not equal                            |
| `BETWEEN` | Range                                |
| `LIKE`    | Search for a pattern                 |
| `IN`      | List of possible values for a column |

### NEW TABLE
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```

### CLONE
```sql
CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....;
```