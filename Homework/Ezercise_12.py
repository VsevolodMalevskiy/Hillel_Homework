# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()

import datetime


start_time = datetime.datetime.now()
end_time = datetime.datetime.now() - start_time

