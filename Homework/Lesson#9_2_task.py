# Написать программу для поиска в списке определённого слова
# При этом список может состоять из разного типа данных
# и иметь не ограниченное число вложенных друг в друга списков или кортежей
# поиск произвести по всем списка и кортежам, в том числе и вложенным

INPUT_LIST = [
    1, '2', 'cat', 99, 'dog',
    (4, 44, ['red', 'green', ('mother', 'father',)]),
    ['one', 'two', '55', {1, 4, ('bik', 'big', 'def')}, True, ['milk', 0, 'bred']],
    'End'
]


def search_word(in_word: str, in_list):
    if type(in_word) != str or in_word.isdigit():
        return f"Введенное {in_word} является цифрой"
    elif in_word in in_list:
        return f"Слово {in_word} найдено"
    for item in in_list:
       if type(item) in (list, tuple, set):
           word_search = search_word(in_word, item)
           if word_search is not None:
               return word_search


print(search_word("cat", INPUT_LIST))
