import sqlite3 as sq

with sq.connect("super.db") as con:
    cur = con.cursor()
                                                     # удаляется таблица, если существует
    cur.execute("DROP TABLE IF EXISTS users")
                                                     # создается таблица, если ранее не была создана
                                                     # создается столбец users-id с уникальными ключами
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (   
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,                 
        name TEXT NOT NULL,
        sex INTEGER DEFAULT 1,
        ld INTEGER,
        score INTEGER
    )""")

con.close()

