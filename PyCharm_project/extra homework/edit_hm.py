def open_func(file):
    f_1 = open(f'{file}', 'r')
    f_2 = f_1.read()
    f_1.close()
    f_2 = f_2.lower()
    return f_2


def my_counter(file):  # Вывести на экран сколько букв, цифр и спецсимволов в каждом из файлов
    count_letter = 0
    count_digit = 0
    count_symbol = 0
    for letter in file:
        if letter.isalpha():
            count_letter += 1
        elif letter.isdigit():
            count_digit += 1
        else:
            count_symbol += 1

    return f'LETTERs = {count_letter}, DIGITs = {count_digit}, SYMBOLs = {count_symbol}'


def average_digit(file):  # Вывести на экран среднее арифметическое всех цифр для каждого из файлов
    count_digit = 0
    count_sum = 0
    for digit in file:
        if digit.isdigit():
            count_digit += 1
            count_sum += int(digit)
            average = count_sum / count_digit

    return average


def top_3_letter(file):  # Вывести на экран Топ 3 букв для каждого файла (Топ 3 по количеству)
    my_dictionary = {}
    for i in file:
        if i.isalpha():
            counter = file.count(i)
            my_dictionary[i] = counter
    sort_dictionary = sorted(my_dictionary, key=my_dictionary.get)
    top_1 = sort_dictionary[-1]
    top_2 = sort_dictionary[-2]
    top_3 = sort_dictionary[-3]
    return f'{top_1.upper()} - количество: {my_dictionary.get(top_1)} \n' \
           f'{top_2.upper()} - количество: {my_dictionary.get(top_2)} \n' \
           f'{top_3.upper()} - количество: {my_dictionary.get(top_3)}'


def task_5_preparation(file):  # Сравнить количество уникальных букв в каждом файле
    my_dictionary = {}
    for i in file:
        if i.isalpha():
            counter = file.count(i)
            my_dictionary[i] = counter
    return len(my_dictionary)


def task_5():
    len_7 = task_5_preparation(open_func('file7.txt'))
    len_8 = task_5_preparation(open_func('file8.txt'))
    len_9 = task_5_preparation(open_func('file9.txt'))
    if len_7 > len_8 and len_7 > len_9:
        total = f'В файле <File 7> больше всего уникальных букв <{len_7}>'
    elif len_8 > len_7 and len_8 > len_9:
        total = f'В файле <File 8> больше всего уникальных букв <{len_8}>'
    elif len_9 > len_8 and len_9 > len_8:
        total = f'В файле <File 9> больше всего уникальных букв <{len_9}>'
    return total


def task_6_preparation(file):  # Вывести на экран сумму чисел из всех трех файлов
    count_sum = 0
    for digit in file:
        if digit.isdigit():
            count_sum += int(digit)

    return count_sum


def task_6():
    sum_7 = task_6_preparation(open_func('file7.txt'))
    sum_8 = task_6_preparation(open_func('file8.txt'))
    sum_9 = task_6_preparation(open_func('file9.txt'))
    result = sum_7 + sum_8 + sum_9

    return result


def task_7_preparation(file):  # Вывести на экран сколько во всех файлах среди спецсимволов знаков препинания
    start_set = {'!', '-', '(', ')', ',', '.', ':', ';', '?'}
    symbol_list = []
    punctuation_list = []
    other_symbol_list = []
    for i in file:
        if i.isalpha():
            continue
        elif i.isdigit():
            continue
        else:
            symbol_list.append(i)
    for i in symbol_list:
        if i in start_set:
            punctuation_list.append(i)
        else:
            other_symbol_list.append(i)

    return len(punctuation_list), len(other_symbol_list)


def task_7():
    punc_7 = task_7_preparation(open_func('file7.txt'))
    punc_8 = task_7_preparation(open_func('file8.txt'))
    punc_9 = task_7_preparation(open_func('file9.txt'))
    result_punc = punc_7[0] + punc_8[0] + punc_9[0]
    result_other_symbol = punc_7[1] + punc_8[1] + punc_9[1]
    return f'Всего в файлах <{result_punc}> знаков препинания и <{result_other_symbol}> прочих спецсимволов'


print('File 7:')
print(f"{my_counter(open_func('file7.txt'))}")
print(f"Среднее арифметическое = {average_digit(open_func('file7.txt'))}")
print(f"{top_3_letter(open_func('file7.txt'))}")
print()
print('File 8:')
print(f"{my_counter(open_func('file8.txt'))}")
print(f"Среднее арифметическое = {average_digit(open_func('file8.txt'))}")
print(f"{top_3_letter(open_func('file8.txt'))}")
print()
print('File 9:')
print(f"{my_counter(open_func('file9.txt'))}")
print(f"Среднее арифметическое = {average_digit(open_func('file9.txt'))}")
print(f"{top_3_letter(open_func('file9.txt'))}")
print()
print(task_5())
print(f'Сумма всех чисел = {task_6()}')
print(task_7())
