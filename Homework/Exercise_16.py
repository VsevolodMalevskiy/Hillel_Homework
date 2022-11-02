# При помощи PIP установить такие пакеты:
# requests (версии 2.26.0);
# lxml (последней версии).
# Записать установленные зависимости в файл requirements.txt.
# Удалить эти зависимости и затем установить их из файла requirements.txt.
# Для проверки прислать файл requirements.txt и скриншот выполненных действий

# Выполненные действия:
# pip freeze (pip list) - просмотр установленных пакетов
# certifi==2022.9.24
# charset-normalizer==2.0.12
# idna==3.4
# urllib3==1.26.12
#
# pip install requests==2.26.0 lxml (результат в файле)
# pip freeze (pip list) - просмотр установленных пакетов
# certifi==2022.9.24
# charset-normalizer==2.0.12
# idna==3.4
# lxml==4.9.1
# requests==2.26.0
# urllib3==1.26.12
#
# pip freeze > requirements.txt   записывает в requirements.txt все зависимости и удаляю вручную оставляя только требуемые:
# lxml==4.9.1
# requests==2.26.0
#
# pip uninstall requests==2.26.0 lxml удаление пакетов
# pip freeze (pip list) - просмотр установленных пакетов
# pip install -r requirements.txt устанавливаю требуемые пакеты (результат в файле)
# pip list - просмотр установленных пакетов
