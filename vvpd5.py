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





