# Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка, которая высчитывает разницу длин строк из списков first и second, если их длины не равны.
# Для перебора строк попарно из двух списков используем функцию zip.
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторную сборка, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second.
# Используем функции range и len.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
