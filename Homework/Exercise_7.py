"""Дан словарь, создать новый словарь при помощи конструкции генератора словаря, поменяв местами ключ и значение."""


dictionary_start = {"beaf": 200, "pork": 170, "chiken": 110, "duck": 130}
dictionary_modified = {dictionary_start[key]: key for key in dictionary_start}

print("Искодный словарь:", dictionary_start, type(dictionary_start),"\n")
print("Трансформированный словарь:", dictionary_modified, type(dictionary_modified), )