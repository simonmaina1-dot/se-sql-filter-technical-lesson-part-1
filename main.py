import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employees =  pd.read_sql("""
                         SELECT * FROM employees;
                         """, conn)
print (employees)

patterson_employees = pd.read_sql("""
SELECT *
  FROM employees
 WHERE lastName = "Patterson";
""", conn)
print(patterson_employees)


name_length_5 = pd.read_sql("""
SELECT *, length(firstName) AS name_length
  FROM employees
 WHERE length(firstName) = 5;
""", conn)
print(name_length_5)

first_initial_L = pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE substr(firstName, 1, 1) = 'L';
""", conn)
print(first_initial_L)

rounded_price_30 = pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails
 WHERE CAST(round(priceEach) AS INTEGER) = 30;
""", conn)
print(rounded_price_30)

late_orders = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE julianday(shippedDate) - julianday(requiredDate) > 0;
""", conn)
print(late_orders)


conn.close()