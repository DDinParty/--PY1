dict_ = {}
DEFAULT_COUNT = 0
def get_count_char(str_):
    str_ = str_.lower()
    for w in str_:
        if w.isalpha():
            dict_[w] = dict_.get(w, DEFAULT_COUNT) + 1
    return dict_

    # TODO посчитать количество каждой буквы в строке в аргументе str_



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def percentage_dict(dict_):
    dict_sum = sum(dict_.values())
    for w in dict_:
        if w.isalpha():
            dict_[w] = round((((dict_.get(w, DEFAULT_COUNT)) / dict_sum) * 100), 2)

    return dict_

print(get_count_char(main_str))
print(percentage_dict(dict_))
