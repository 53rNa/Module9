# Задание: Декораторы в Python

# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1-ой функции будет простым числом
# и "Составное" в противном случае
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

# Обертываем декоратором (is_prime) функцию (sum_three), которая складывает 3 числа
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
