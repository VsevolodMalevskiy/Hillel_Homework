import datetime
import openpyxl
import re
import sqlite3 as sq

KEY_DATA = r'\d{1,4}(?:-|.|/| )\d*(?:-|.|/| )\d{2,4}'

# функция проверки существования даты до текущего момента
def foo(data_check):
    try:
        datetime.date(int(data_check[0:4]), int(data_check[5:7]), int(data_check[8:]))
        if int(data_check[0:4]) == datetime.datetime.now().year and\
            int(data_check[5:7]) <= datetime.datetime.now().month\
             and int(data_check[8:]) <= datetime.datetime.now().day:
             return data_check
        elif int(data_check[0:4]) < datetime.datetime.now().year:
            return data_check
    except:
        return None


# функция перевода дат в формат SQL с отсеиванием некорректных дат
def convert_data(data):
    try:
        z = data.replace(" ", ".").replace("/", ".").replace("-", ".")
        if z.index(".") == 1:
            if z[2:].index(".") == 1:
                z = "0" + z[0:2] + "0" + z[2:4] + z[4:]
            else:
                z = "0" + z[0:2] + z[2:4] + z[4:]
        if z.index(".") == 2 and z[3:].index(".") == 1:
            z = z[0:3] + "0" + z[3:4] + z[4:]
        if z.index(".") == 2:
            z = z[6:] + z[2:6] + z[0:2]
        z = foo(z)
        return z
    except:
        return []


# состоит ли строка из букв и если да, то перевод первой буквы в верхний регистр
def check_string(string_in):
    if not string_in:
        return
    elif string_in.strip().isalpha():
        string_in = string_in.lower()
        return string_in


# проверка строки и перевод в пол 'мужчина' или 'женщина'
def check_sex(cell_in):
    if not cell_in:
        return
    elif cell_in.strip().isalpha():
        if len(cell_in.lower().split("f")) == 2 or len(cell_in.lower().split("жен")) == 2:
            return 'женщина'
        elif len(cell_in.lower().split("m")) == 2 or len(cell_in.lower().split("муж")) == 2:
            return 'мужчина'


def load_fromfile(file_xlsx):
    try:
        book = openpyxl.load_workbook(filename=file_xlsx)
        sheet = book.active
    except:
        error_message = 'File not found'
        print(error_message)
        return

    massiv_add = []
    for row in range(1, 100):
        try:
            for col in range(0, 9):
                try:
                    c_3 = re.findall(KEY_DATA, str(sheet[row][col].value))
                    c_4 = re.findall(KEY_DATA, str(sheet[row][col + 1].value))

                    if c_3:
                        c_3 = convert_data(c_3[0])
                    if c_4:
                        c_4 = convert_data(c_4[0])
                    if c_3 and c_4 and c_3 > c_4:
                        c_3 = None
                        c_4 = None
                    c_0 = check_string(sheet[row][col - 3].value)
                    c_1 = check_string(sheet[row][col - 2].value)
                    c_2 = check_string(sheet[row][col - 1].value)
                    c_5 = check_sex(sheet[row][col + 2].value)

                    if c_0 and c_3 and c_5:
                        if not c_1:
                            c_1 = None
                        if not c_2:
                            c_2 = None
                        if not c_4:
                            c_4 = None
                        massiv_add.append((c_0, c_1, c_2, c_3, c_4, c_5))

                except IndexError:
                    pass
                finally:
                    continue
        except IndexError:
            break
        finally:
            continue
    return massiv_add


# открытие базы данных
def open_db():
    with sq.connect("residents.db") as data_base:
        cur = data_base.cursor()

        # создается таблица, если ранее не была создана, создается столбец users-id с уникальными ключами
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            LastName NVARCHAR(20) NOT NULL,
            FirstName NVARCHAR(20),            
            Patronymic NVARCHAR(20),
            Data_Birth DATE NOT NULL,
            Data_Death DATE,
            Sex NVARCHAR(4) NOT NULL
        )""")
        data_base.commit()


# Загрузка в базу данных списка из файла .xlsx
def insert_in_db(file_excel):
    with sq.connect("residents.db") as data_base:
        cur = data_base.cursor()

        # создается таблица, если ранее не была создана, создается столбец users-id с уникальными ключами
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            LastName NVARCHAR(20) NOT NULL,
            FirstName NVARCHAR(20),            
            Patronymic NVARCHAR(20),
            Data_Birth DATE NOT NULL,
            Data_Death DATE,
            Sex NVARCHAR(4) NOT NULL
        )""")
        data_base.commit()

        massiv_xlsx = load_fromfile(file_excel)

        # Добавление строк из файла xls
        table_insert = """INSERT INTO users(LastName, FirstName, Patronymic, Data_Birth, Data_Death, Sex)
              VALUES (?, ?, ?, ?, ?, ?);"""

        cur.executemany(table_insert, massiv_xlsx)
        data_base.commit()
    cur.close()
    return len(massiv_xlsx)


# добавление данных из панели в базу данных
def add_file_db(data_panel):
    with sq.connect("residents.db") as data_base:
        cur = data_base.cursor()

        # создается таблица, если ранее не была создана, создается столбец users-id с уникальными ключами
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            LastName NVARCHAR(20) NOT NULL,
            FirstName NVARCHAR(20),            
            Patronymic NVARCHAR(20),
            Data_Birth DATE NOT NULL,
            Data_Death DATE,
            Sex NVARCHAR(4) NOT NULL
        )""")
        data_base.commit()

    table_insert = """INSERT INTO users(LastName, FirstName, Patronymic, Data_Birth, Data_Death, Sex)
                  VALUES (?, ?, ?, ?, ?, ?);"""

    cur.executemany(table_insert, data_panel)
    data_base.commit()


# Поиск в базе данных по ключу
def db_check_out(part):
    with sq.connect("residents.db") as data_base:
        cur = data_base.cursor()
        search_sql_first = """
          SELECT *
            FROM users           
            WHERE FirstName LIKE ? 
            GROUP BY LastName, FirstName, Patronymic, Data_Birth, Data_Death, Sex
        """

        search_sql_last = """
              SELECT *
                FROM users           
                WHERE LastName LIKE ? 
                GROUP BY LastName, FirstName, Patronymic, Data_Birth, Data_Death, Sex
            """

        search_sql_petron = """
              SELECT *
                FROM users           
                WHERE Patronymic LIKE ? 
                GROUP BY LastName, FirstName, Patronymic, Data_Birth, Data_Death, Sex
            """

        x = r'%'+part.strip()+r'%'
        search_string = [x]

        db_1 = cur.execute(search_sql_first, search_string).fetchall()
        db_2 = cur.execute(search_sql_last, search_string).fetchall()
        db_3 = cur.execute(search_sql_petron, search_string).fetchall()
        db_all = db_1 + db_2 + db_3

        db_list = list(set(db_all))

    cur.close()
    return db_list


def convert_data_1(data):
    data_c = data[8:]+data[4:8]+data[:4]
    return data_c


def preparation(list_pr):
    out_1 = list_pr[1].title()
    if list_pr[2]:
        out_2 = list_pr[2].title()
    else:
        out_2 = ''
    if list_pr[3]:
        out_3 = list_pr[3].title()
    else:
        out_3 = ''
    out_4 = convert_data_1(list_pr[4])
    if list_pr[5]:
        out_5 = convert_data_1(list_pr[5])
        age = int(out_5[6:]) - int(out_4[6:])
        if int(out_5[3:5]) < int(out_4[3:5]):
            age -= 1
        elif int(out_5[3:5]) == int(out_4[3:5]) and int(out_5[:2]) < int(out_4[:2]):
            age -= 1
    else:
        out_5 = ''
        d_t = datetime.date.today()
        age = int(d_t.year) - int(out_4[6:])
        if int(d_t.month) < int(out_4[3:5]):
            age -= 1
        elif int(d_t.month) == int(out_4[3:5]) and int(d_t.day) < int(out_4[:2]):
            age -= 1
    out_6 = list_pr[6]
    if int(str(age)[-1]) == 1:
        let = 'год'
    elif int(str(age)[-1]) in [2, 3, 4]:
        let = 'года'
    else:
        let = 'лет'

    if out_6 == 'мужчина':
        rod = 'Родился'
        mer = "Умер"
    else:
        rod = "Родилась"
        mer = 'Умерла'
    if not out_5:
        mer = ''

    l_pr = f"{out_1} {out_2} {out_3} {age} {let}, {out_6}. {rod} {out_4}. {mer} {out_5}"
    return l_pr

if __name__ == '__main__':
    a = '1972-04-13'
    b = '2022-02-12'
    c = '12/45/2022'
    d = '12 12 2023'
    e = '2025-12-11'
    f = '1-9-2022'
    g = '02-9-2022'
    h = '2-09-2022'

    print(convert_data(a))
    print(convert_data(b))
    print(convert_data(c))
    print(convert_data(d))
    print(convert_data(e))
    print(convert_data(f))
    print(convert_data(g))
    print(convert_data(h))

# print(convert_data(f) > convert_data(c))

