# Задача "Функциональное разнообразие"

from random import choice

# 1. Lambda-функция: реализация lambda-функции для следующего выражения - list(map(?, first, second))
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

# 2. Замыкание: Функция, принимающая название файла file_name для записи.
def get_advanced_writer(file_name):

    # Добавляем в файл file_name все данные из data_set (параметр, принимающий неограниченное количество данных
    # любого типа) в том же виде, какими они были переданы в функцию
    def write_everything(*data_set):
        # Открываем файл для дозаписи
        with open(file_name, 'a', encoding="utf-8") as file:
            for data in data_set:
                # Преобразуем данные в строку и записываем ее в файл
                file.write(str(data) + '\n')

    # Функция get_advanced_writer возвращает функцию write_everything
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print (result)

# 3. Реализация метода __call__: объекты класса MysticBall обладают атрибутом words, хранящий коллекцию строк.
#    Метод __call__ случайным образом выбирает слово из words и возвращать его
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



