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


#      Флаги:
# -n   сортировка по NAME
# -nr  обратная сортировка по NAME
# -p   сортировка по PID
# -pr  обратная сортировка по имени
# -m   сортировка по MEMORY
# -mr  обратная сортировка по MEMORY
# -s   сортировка по Session name
# -sr  обратная сортировка по Session name

import sys, os, psutil, time, datetime

# приемка флага (sys.argv[0] - имя файла)
key = sys.argv[1] if len(sys.argv) > 1 else 0


def input_processes():
    value_tasklist = 0
    massiv = []
    for line in os.popen('tasklist /NH /FO CSV /FI "memusage gt 50000"'): #  с размером больше 50 МБ
          massiv.append(line.rstrip().encode('cp1251').decode('cp866').replace('"', '').split(",")) # перекодировка
          massiv[value_tasklist][4] = massiv[value_tasklist][4][:-3].replace('\xa0', '') # удаление лишнего в Memory
          value_tasklist += 1
          # количество процессов для записи
          if value_tasklist == 100:
              break

    cpu = str(psutil.cpu_percent(interval=0.2))
    ram_total = psutil.virtual_memory().total
    ram_isp = str((psutil.virtual_memory().used * 100 / psutil.virtual_memory().total))
    ram_neisp = psutil.virtual_memory().available
    ram_dost = str((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
    current_time = datetime.datetime.now()

    return float(ram_total), round(float(ram_isp),1), float(ram_neisp), ram_dost, float(cpu), current_time, massiv


def mass_sorted(flag, d_massiv):
    if flag == "-m":
        d_massiv = sorted(d_massiv, reverse=True, key=lambda x: int(x[4]))
    elif flag == "-mr":
        d_massiv = sorted(d_massiv, key=lambda x: int(x[4]))
    elif flag == "-n":
        d_massiv = sorted(d_massiv, key=lambda x: x[0])
    elif key == "-nr":
        d_massiv = sorted(d_massiv, reverse=True, key=lambda x: x[0])
    elif flag == "-p":
        d_massiv = sorted(d_massiv, key=lambda x: int(x[1]))
    elif flag == "-pr":
        d_massiv = sorted(d_massiv, reverse=True, key=lambda x: int(x[1]))
    elif flag == "-s":
        d_massiv = sorted(d_massiv, key=lambda x: x[2])
    elif flag == "-sr":
        d_massiv = sorted(d_massiv, reverse=True, key=lambda x: x[2])
    return d_massiv


while True:
    ram_total, ram_isp, ram_neisp, ram_dost, cpu, current_time, data_massiv = input_processes()

    data_massiv = mass_sorted(key, data_massiv)

    print()
    print(f"\033[37mCPU (%)  [\033[31m{'|'*int(cpu)}\033[37m{'|'*(100-int(cpu))}\033[37m{']    '+str(cpu)+' %':>5}")
    print(f"FREQ (%) [\033[31m{'|'*int(ram_isp)}\033[37m{'|'*(100-int(ram_isp))}\033[37m{']    '+str(ram_isp)+' %':>5}")
    print(f"MEM (GB) [\033[37m{'|'*int(100*ram_neisp/ram_total)}\033[31m{'|'*(100-int(100*ram_neisp/ram_total))}"
          f"\033[37m{']    '+str(round(ram_neisp/1000000000, 2))+' GB/ '+str(round(ram_total/1000000000, 2))+' GB':>5}")
    print()
    print(f"\033[34m{'NAME':^20}{'PID':^10}{'Session name':^15}{'# Session':^20}{'MEMORY':^15}{'TIME':^20}")
    print(f"\033[34m{'='*20+' '}{'='*8+' '}{'='*14+' '}{'='*19+' '}{'='*14+' '}{'='*20}")
    # ограничение по выводу 20 строк
    for item in range(20):
        print(f"\033[34m{data_massiv[item][0][:20]:<20}{data_massiv[item][1]:>9}{data_massiv[item][2]:>9}"
              f"{data_massiv[item][3]:>26}{data_massiv[item][4]+' KB':>15}{str(current_time)[5:-5]:>21}")
    time.sleep(2)

# запуск python Homework\exercise_spez.py