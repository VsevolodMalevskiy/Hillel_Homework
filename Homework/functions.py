import datetime
import openpyxl
import re


# функция проверки существования даты до текущего момента
def foo(data_check):
    try:
        datetime.date(int(data_check[0:4]), int(data_check[5:7]), int(data_check[8:]))
        if int(data_check[0:4]) <= datetime.datetime.now().year and\
            int(data_check[5:7]) <= datetime.datetime.now().month\
             and int(data_check[8:]) <= datetime.datetime.now().day:
             return data_check
    except:
        return None


# функция перевода дат в формат SQL с отсеиванием некорректных дат
def convert_data(data):
    z = data.replace(" ", ".").replace("/", ".").replace("-", ".")
    if z.index(".") == 1:
        if z[2:].index(".") == 1:
            z = "0" + z[0:2] + "0" + z[2:4] + z[4:]
        else:
            z = "0" + z[0:2] + z[2:4] + z[4:]
    if z.index(".") == 2 and z[3:].index(".") == 1:
        z = z[0:3] + "0" + z[3:4] + z[4:]
    if z.index(".") == 2:
        z = z[6:]+z[2:6]+z[0:2]
    z = foo(z)
    return z

# состоит ли строка из букв и если да, то перевод первой буквы в верхний регистр
def check_string(string_in):
    if not string_in:
        return
    elif string_in.strip().isalpha():
        string_in = string_in.title()
        return string_in

# проверка строки и перевод в пол 'муж' или 'жен'
def check_sex(cell_in):
    if not cell_in:
        return
    elif cell_in.strip().isalpha():
        if len(cell_in.lower().split("female")) == 2 or len(cell_in.lower().split("жен")) == 2:
            return 'жен'
        elif len(cell_in.lower().split("male")) == 2 or len(cell_in.lower().split("муж")) == 2:
            return 'муж'


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
                    c_3 = re.findall(r'\d{1,4}(?:-|.|/| )\d*(?:-|.|/| )\d{2,4}', str(sheet[row][col].value))
                    c_4 = re.findall(r'\d{1,4}(?:-|.|/| )\d*(?:-|.|/| )\d{2,4}', str(sheet[row][col + 1].value))

                    if not c_3:
                        pass
                    else:
                        c_3 = convert_data(c_3[0])

                        if c_4:
                            c_4 = convert_data(c_4[0])

                            if c_3 > c_4:
                                c_3 = None
                                c_4 = None
                        else:
                            c_4 = None

                        c_0 = check_string(sheet[row][col - 3].value)
                        c_1 = check_string(sheet[row][col - 2].value)
                        c_2 = check_string(sheet[row][col - 1].value)
                        c_5 = check_sex(sheet[row][col + 2].value)

                        if c_0 and c_3 and c_5:
                            massiv_add.append((c_0, c_1, c_2, c_3, c_4, c_5))
                        continue
                except IndexError:
                    pass
                finally:
                    continue
        except IndexError:
            break
        finally:
            continue
    return massiv_add
    # print(massiv_add)
    # print(len(massiv_add))







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

