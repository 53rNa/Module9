# Задача: закрепить знания о списочных и словарных сборках, решив несколько небольших задач

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишисываем список, созданный при помощи словарной сборки, состоящий из длин строк
# списка first_strings, при условии, что длина строк не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# В переменную second_result запишисываем список, созданный при помощи словарной сборки, состоящий из пар слов(кортежей)
# одинаковой длины. Каждое слово из списка first_strings сравнивается с каждым из second_strings
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# В переменную third_result запишисывается словарь, созданный при помощи словарной сборки, где парой ключ-значение
# будет строка - длина строки. Значения строк перебираются из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
