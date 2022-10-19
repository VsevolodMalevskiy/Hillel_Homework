"""Реализовать код, который выведет следующие наборы данных.

1) Прибыль по таблице invoice_items. Сумма по заказу = UnitPrice * Quantity (если через sql, то нужно использовать sum).
В итоге через функцию print() выводим 1 цифру общей прибыли.

2) Считаем кол-во повторений FirstName в таблице customers. Через функцию print() выводим имя и кол-во его повторений."""

import os
import sqlite3
from collections import Counter

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

# Задача 1

query1_sql = """
  SELECT UnitPrice, Quantity
    FROM invoice_items;
"""
rows1 = cur.execute(query1_sql).fetchall()

summa = 0
for row1 in rows1:
    summa += row1[0] * row1[1]
print("\n#1 task")
print(f"Общая прибыль по таблице Invoice_items = {'%.2f' % summa}\n")

# Задача 1 (SQL)

query11_sql = """
SELECT SUM(UnitPrice*Quantity)
  FROM invoice_items;
"""

rows11 = cur.execute(query11_sql).fetchall()
rows11 = rows11[0]

print("#1 task (SQL)")
print(f"Общая прибыль по таблице Invoice_items = {'%.2f' % (rows11)}\n")

# Задача 2

query2_sql = """
  SELECT FirstName
    FROM customers;
"""
rows2 = cur.execute(query2_sql).fetchall()
rows3 = Counter([item[0] for item in rows2])  # перевод в одноуровневый список

print("#2 task")
for key, value in rows3.items():
    if value > 1:
        print(f"Имя - {key}, количество повторений - {value}")

# Задача 2 (SQL)

query4_sql = """
  SELECT FirstName, COUNT(*)
    FROM customers
    GROUP BY
      FirstName
    HAVING 
      COUNT(*) > 1;
"""

rows4 = cur.execute(query4_sql).fetchall()
print("\n#2 task (SQL)")
for item in rows4:
    print(f"Имя - {item[0]}, количество повторений - {item[1]}")

connection.close()
