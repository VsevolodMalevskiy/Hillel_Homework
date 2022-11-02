# Написать программу аналог команды top или htop для Linux-систем.
# Программу написать на основе данных полученных из утилиты psutil.
# Вывод необходимо сделать по возможности красивым и максимально
# приближенным к выводу команд top или htop.
# В начале необходимо в графическом виде и виде процентов вывести информацию
# о частоте и загрузке процессоре, а атк же о памяти: используемая/доступная.
# После этого необходимо в табличном виде вывести информацию о первых 30 -
# 35 процессах разбитой по столбцам: pid, username, cpu, memory, time, command.
# В каждой новой строке информация о новом процессе, на подобии как в top.
# Желательно, чтобы как по аналогии с командами top или htop информация
# постоянно обновлялась, где-то через каждые 2-3 секунды.
# Предусмотреть возможность сортировки процессов по любому из параметров.
# Как вариант, это можно сделать при помощи аргументов при запуске скрипта (argparse).
# Ссылка как вывод сделать цветным: https://egorovegor.ru/python-color-printing/



# запуск python Homework\exercise_spez.py

import os
import psutil
import time
import datetime


current_time = datetime.datetime.now()
print(current_time)

def input_processes():
    value_tasklist = 0
    massiv = []
    for line in os.popen('tasklist /NH /FO CSV /FI "memusage gt 50000"'): #  с размером больше 100 МБ
          massiv.append(line.rstrip().encode('cp1251').decode('cp866').replace('"', '').split(","))
          massiv[value_tasklist][4] = massiv[value_tasklist][4][:-3].replace('\xa0', '') # удаление последних трех символов Кб
          value_tasklist += 1
          # количество процессов для записи
          if value_tasklist == 20:
              break

    cpu = str(psutil.cpu_percent(interval=0.2))
    ram_total = psutil.virtual_memory().total
    ram_isp = str((psutil.virtual_memory().used * 100 / psutil.virtual_memory().total))
    ram_neisp = psutil.virtual_memory().available
    ram_dost = str((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
    current_time = datetime.datetime.now()

    return float(ram_total), round(float(ram_isp),1), float(ram_neisp), ram_dost, float(cpu), current_time, massiv


while True:
    ram_total, ram_isp, ram_neisp, ram_dost, cpu, current_time, data_massiv = input_processes()

    print()
    print(f"CPU (%)  [\033[31m{'|'*int(cpu)}\033[37m{'|'*(100-int(cpu))}\033[37m{']    '+str(cpu)+' %':>5}")
    print(f"FREQ (%) [\033[31m{'|'*int(ram_isp)}\033[37m{'|'*(100-int(ram_isp))}\033[37m{']    '+str(ram_isp)+' %':>5}")
    print(f"MEN (GB) [\033[37m{'|'*int(100*ram_neisp/ram_total)}\033[31m{'|'*(100-int(100*ram_neisp/ram_total))}"
          f"\033[37m{']    '+str(round(ram_neisp/1000000000, 2))+' GB/ '+str(round(ram_total/1000000000, 2))+' GB':>5}")
    print()
    print(f"\033[34m{'NAME':^20}{'PID':^10}{'Session name':^15}{'# Session':^20}{'MEMORY':^15}{'TIME':^20}")
    print(f"\033[34m{'='*20+' '}{'='*8+' '}{'='*14+' '}{'='*19+' '}{'='*14+' '}{'='*20}")
    for item in range(20):
        print(f"\033[34m{data_massiv[item][0][:20]:<20}{data_massiv[item][1]:>9}{data_massiv[item][2]:>9}"
              f"{data_massiv[item][3]:>26}{data_massiv[item][4]+' KB':>15}{str(current_time)[5:-5]:>21}")
    time.sleep(2)


# import os
# import subprocess
#
#
# import subprocess as sp
#
# tasks=sp.getoutput('tasklist');
#
# from subprocess import Popen, PIPE
#
# print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])

# ram_inform = psutil.virtual_memory()
# #  Информация по дискам [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255,
# #  maxpath=260), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]
# d = psutil.disk_partitions()[0][0][0:2]  #!!! ПОРАБОТАТЬ
# # sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
# x = psutil.disk_usage("C:/").total #!!! ПОРАБОТАТЬ
#
#
# print(f"Загрузка процессора (%): {float(cpu):.2f}")
# print(f"Всего памяти (Бт): {ram_total:,}")
# print(f"Доступная (Бт): {ram_neisp:,}")
# print(f"Используемая (%): {float(ram_isp):.2f}")
# print(f"Доступная (%): {float(ram_dost):.2f}")
# print(ram_inform)
# print(d)
# print(f"{x:,}")

# Запущенные процессы
# for proc in psutil.process_iter():
#     try:
#         pinfo = proc.as_dict(attrs=['pid', 'name'])
#     except psutil.NoSuchProcess:
#         pass
#     else:
#         print(pinfo)




