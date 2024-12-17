from math import *


def maclaurin_ln1_plus_x(x, iterations=4):
    """
    Функция, вычисляющая ln(1 + x) по ряду Маклорена
    Вычисляет приближенное значение ln(1 + x) с использованием разложения в ряд Маклорена
    :param x: значение, для которого вычисляется ln(1 + x) в пределе (-1, 1]
    :param iterations: количество итераций (по умолчанию 4)
    :return: приближенное значение ln(1 + x)
    :exceptions: x > 1 и x <= -1
    :usage example: Ввод 0.2
    Вывод 0.18226666666666666
    """
    if not (-1 < x <= 1):
        raise ValueError("Значение x должно быть в диапазоне (-1, 1].")
    result = 0
    for n in range(1, iterations + 1):
        maclaurin = (-1)**(n - 1) * (x**n) / n
        result += maclaurin
    return result


def maclaurin_ln_1_minus_x(x, iterations=4):
    """
    Функция, вычисляющая ln(1 - x) по ряду Маклорена
    Вычисляет приближенное значение ln(1 - x) с использованием разложения в ряд Маклорена
    :param x: значение, для которого вычисляется ln(1 - x) в пределе (-1, 1)
    :param iterations: количество итераций (по умолчанию 4)
    :return: приближенное значение ln(1 - x)
    :exceptions: x >= 1 и x <= -1
    :usage example: Ввод 0.2
    Вывод -0.22306666666666672
    """
    if not (-1 < x < 1):
        raise ValueError("Значение x должно быть в диапазоне (-1, 1).")
    result = 0
    for n in range(1, iterations + 1):
        maclaurin = (x ** n) / n
        result += maclaurin
    return -result


def f10(x, m, n):
    """Ряд Маклорена функции (1 - x)^m"""
    """
    Функция, реализующая разложение 
    математической функции (1 - x)^m в формате ряда Маклорена
    """
    """Аргументы:"""
    """ 
    x (принимается из функции menu), 
    m (принимается из функции menu), 
    n = 4 (задано в коде)
    """
    """Возвращаемое значение: float"""
    """Исключения не генерируются"""
    """Пример использования:"""
    """
    Ввод:  0.5
           3
    Вывод: 0.125
    """
    answer = 1
    for i in range(1, n+1):
        m_prod = m
        for j in range(1, i):
            m_prod *= (m - j)
        answer += (-1)**i * (m_prod * x**i) / factorial(i)
    return answer


def main():
    """
    Меню программы
    Выбор вычисления ln(1 + x) или ln(1 - x) с использованием разложения в ряд Маклорена.
    """
    while True:
        print("\nВыберите опцию:")
        print("1. Вычислить ln(1 + x) по формуле Маклорена")
        print("2. Вычислить ln(1 - x) по формуле Маклорена")
        print("3. Вычислить (1 - x)^m по формуле Маклорена")
        print("4. Выход")

        choice = input("Введите номер опции: ")

        if choice == '1':
            try:
                x = float(input("Введите значение x (в пределах (-1, 1]): "))
                result = maclaurin_ln1_plus_x(x)
                print(f"Результат ln(1 + {x}) по формуле Маклорена: {result}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            try:
                x = float(input("Введите значение x (в пределах (-1, 1)): "))
                result = maclaurin_ln_1_minus_x(x)
                print(f"Результат ln(1 - {x}) по формуле Маклорена: {result}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            n = 4
            try:
                x = float(input("Введите X: "))
                m = float(input("Введите M: "))
            except:
                print("Допустим только ввод чисел")
                continue
            if not -1 < x < 1:
                print("X должен быть больше -1 и меньше 1")
                continue
            if abs(m) > n:
                print("Программа не может работать корректно "
                        "при введённом значении m,\n"
                        f"превышающем по модулю "
                        f"установленное значение n (n = 4)")
                continue
            print("Ответ:", f10(x, m, n = 4))

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
