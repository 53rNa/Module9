# Задача "Вызов разом"

# функцию apply_all_func(int_list, *functions) в которая принимает параметры:
#     int_list - список из чисел (int, float)
#     *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
def apply_all_func(int_list, *functions):

    # Создаем пустой словарь results
    result = {}

    # Вызваем каждую функцию к переданному списку int_list
    for func in functions:

        # Ключом будет имя функции, а значением - её результат работы
        result[func.__name__] = func(int_list)

    # Возвращаем результат, полученный в виде словаря
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))