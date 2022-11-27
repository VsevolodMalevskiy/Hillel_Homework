import openpyxl


def load_fromfile(file_xlsx):
    try:
        book = openpyxl.load_workbook(filename=file_xlsx)
        sheet = book.active
    except:
        error_message = 'Нет файла'
        print(error_message)
        return

    massiv_add = []
    for row in range(1, 100):  # количество строк для перебора
        # нужно знать где находятся какие данные, например начинается все с колонки 0
        # (фамилия и дальше колонка 1 имя, колонка 2 отче ...), если с другого столбца,
        # то поменяй цифры в квадратных скобках в sheet[row][0].value
        fam = sheet[row][0].value
        last = sheet[row][1].value
        otch = sheet[row][2].value
        data_b = sheet[row][3].value
        data_s = sheet[row][4].value
        sex = sheet[row][5].value
        # нужно проверить что данные есть теми функциями, которые вчера писались
        # если данных к примеру в otch нет, то нужно присвоить ему значение None

        # теперь нужно проверить, что введены обязательные данный - фамилия, год рождения и пол
        # и все записать как вчера в списко в виде [(,,,,,), (,,,,), ...]

        if fam and data_b and sex:
             massiv_add.append((fam, last, otch, data_b, data_s, sex))

    return massiv_add


x = load_fromfile("имя твоего файла с расширением .xlsx")

print(x)