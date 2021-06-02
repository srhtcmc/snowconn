# SNOWCONN

SNOWCONN is a script for dealing with a connecting snowflake to python.

## Requirements
Install snowsql

Install snowflake.connector first from the link below

https://docs.snowflake.com/en/user-guide/python-connector-pandas.html#requirements

Put config.py and snowconn.py files in the same directory where your python file existing.

## Usage

```python
import snowconn as sc

  s1 = sc.snow()
  my_basic =  'select * from TABLE_A LIMIT 5'
  df = s1.PULL(my_basic)
    
```

