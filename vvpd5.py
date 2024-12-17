def maclaurin_ln1_plus_x(x, iterations=4):
    """
    Вычисляет приближенное значение ln(1 + x) с использованием разложения в ряд Маклорена
    :param x: значение, для которого вычисляется ln(1 + x) в пределе (-1, 1]
    :param iterations: количество итераций (по умолчанию 4)
    :return: приближенное значение ln(1 + x)
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
    Вычисляет приближенное значение ln(1 - x) с использованием разложения в ряд Маклорена
    :param x: значение, для которого вычисляется ln(1 - x) в пределе (-1, 1)
    :param iterations: количество итераций (по умолчанию 4)
    :return: приближенное значение ln(1 - x)
    """
    if not (-1 < x < 1):
        raise ValueError("Значение x должно быть в диапазоне (-1, 1).")
    result = 0
    for n in range(1, iterations + 1):
        maclaurin = (x ** n) / n
        result += maclaurin
    return -result


def main():
    """
    Меню программы
    Выбор вычисления ln(1 + x) или ln(1 - x) с использованием разложения в ряд Маклорена.
    """
    while True:
        print("\nВыберите опцию:")
        print("1. Вычислить ln(1 + x) по формуле Маклорена")
        print("2. Вычислить ln(1 - x) по формуле Маклорена")
        print("3. Выход")

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
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()

