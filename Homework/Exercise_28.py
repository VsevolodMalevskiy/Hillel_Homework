# Создать генератор геометрической прогрессии


def gen_geom(start, n, denom):
    for item in range(n):
        yield start*denom**item


x = gen_geom(1, 5, 2)

print("_" * 40)
print(x)

for item in x:
    print(item)

print("_" * 40)

# print(next(x))  # проверка окончания итерации, исключение StopIteration


