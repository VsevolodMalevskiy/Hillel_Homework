# Прочитать сохранённый json-файл из задания №16 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.

import json
import csv



title_string = ("id", "Name", "old", "phone")
phone = ["+380672352625", "+380958526584", "+380632568475", "+380662356985", "+380502375894", "+380732586535"]

with open('data.json', "r") as data_json:
    data_out = json.load(data_json)
print(data_out)

for item, key in enumerate(data_out):
    data_out[key].append(phone[item])

# не мог понять почему в CSV записывает через строку, нашел, что нужно дописывать newline=''
with open('data.csv', "w", encoding='utf-8', newline='') as data_csv:
    file_writer = csv.writer(data_csv)
    file_writer.writerow(title_string)
    for key, value in data_out.items():
        value.insert(0, key)
        file_writer.writerow(value)





