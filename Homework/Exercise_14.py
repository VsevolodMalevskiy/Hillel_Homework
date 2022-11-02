# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’
# И на конец результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).

string_b = b'r\xc3\xa9sum\xc3\xa9'

string_dec = string_b.decode()
print(string_dec)

string_lat = string_dec.encode('Latin1')
print(string_lat)

string_end = string_lat.decode('Latin1')
print(string_end)

