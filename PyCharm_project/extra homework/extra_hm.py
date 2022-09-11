class OpenFile:
    def __init__(self, file):
        self.file = file

    def open_func(self):  # 1. Прочитать все файлы
        f = open(f'{self.file}', 'r')
        my_file = f.read()
        f.close()
        my_file = my_file.lower()
        return my_file


class Counter:
    def __init__(self, file):
        self.file = file
        self.count_letter = 0
        self.count_digit = 0
        self.count_symbol = 0
        self.count_sum_digit = 0
        self.my_dictionary = {}
        self.symbol_list = []
        self.punctuation_list = []
        self.other_symbol_list = []

    def my_counter(self):  # 2. Вывести на экран сколько букв, цифр и спецсимволов в каждом из файлов
        for i in self.file:
            if i.isalpha():
                self.count_letter += 1
                counter = self.file.count(i)
                self.my_dictionary[i] = counter

            elif i.isdigit():
                self.count_digit += 1
                self.count_sum_digit += int(i)
            else:
                self.count_symbol += 1
                self.symbol_list.append(i)
        for i in self.symbol_list:
            if i in {'!', '-', '(', ')', ',', '.', ':', ';', '?'}:
                self.punctuation_list.append(i)
            else:
                self.other_symbol_list.append(i)

        return f'LETTERs = {self.count_letter}, DIGITs = {self.count_digit}, SYMBOLs = {self.count_symbol}'

    def average_digit(self):  # 3. Вывести на экран среднее арифметическое всех цифр для каждого из файлов
        average = self.count_sum_digit / self.count_digit

        return average

    def top_3_letter(self):  # 4. Вывести на экран Топ 3 букв для каждого файла (Топ 3 по количеству)
        sort_dictionary = sorted(self.my_dictionary, key=self.my_dictionary.get)
        top_1 = sort_dictionary[-1]
        top_2 = sort_dictionary[-2]
        top_3 = sort_dictionary[-3]

        return f'Топ 3 букв: \n' \
               f'{top_1.upper()} - количество: {self.my_dictionary.get(top_1)} \n' \
               f'{top_2.upper()} - количество: {self.my_dictionary.get(top_2)} \n' \
               f'{top_3.upper()} - количество: {self.my_dictionary.get(top_3)}'

    @staticmethod
    def unique_letters():  # 5. Сравнить количество уникальных букв в каждом файле
        len_7 = len(count_7.my_dictionary)
        len_8 = len(count_8.my_dictionary)
        len_9 = len(count_9.my_dictionary)
        if len_7 > len_8 and len_7 > len_9:
            return f'В файле <File 7> больше всего уникальных букв <{len_7}>'
        elif len_8 > len_7 and len_8 > len_9:
            return f'В файле <File 8> больше всего уникальных букв <{len_8}>'
        elif len_9 > len_8 and len_9 > len_8:
            return f'В файле <File 9> больше всего уникальных букв <{len_9}>'

    @staticmethod
    def Sum_all_digit():  # 6. Вывести на экран сумму чисел из всех трех файлов
        result = count_7.count_sum_digit + count_8.count_sum_digit + count_9.count_sum_digit

        return result

    @staticmethod
    def punctuation():  # 7. Вывести на экран сколько во всех файлах среди спецсимволов знаков препинания
        result_punc = len(count_7.punctuation_list) + len(count_8.punctuation_list) + len(count_9.punctuation_list)
        result_other_symbol = len(count_7.other_symbol_list) + len(count_8.other_symbol_list) + len(
            count_9.other_symbol_list)

        return f'Всего в файлах <{result_punc}> знаков препинания и <{result_other_symbol}> прочих спецсимволов'


file_7 = OpenFile('file7.txt')
file_8 = OpenFile('file8.txt')
file_9 = OpenFile('file9.txt')

count_7 = Counter(file_7.open_func())
count_8 = Counter(file_8.open_func())
count_9 = Counter(file_9.open_func())

print(f'File: {file_7.file}')
print(count_7.my_counter())
print(f"Среднее арифметическое = {count_7.average_digit()}")
print(count_7.top_3_letter())
print()
print(f'File: {file_8.file}')
print(count_8.my_counter())
print(f"Среднее арифметическое = {count_8.average_digit()}")
print(count_8.top_3_letter())
print()
print(f'File: {file_9.file}')
print(count_9.my_counter())
print(f"Среднее арифметическое = {count_9.average_digit()}")
print(count_9.top_3_letter())
print()
print(Counter.unique_letters())
print(f'Сумма всех чисел = {Counter.Sum_all_digit()}')
print(Counter.punctuation())
