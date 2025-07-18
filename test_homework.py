
def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    from string import Template
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    # output = "Привет, " + name + "! Тебе " + str(age) + " лет."
    # print(output)
    # output = "Привет, {name}! Тебе {age} лет.".format(name=name, age=age)
    # print(output)
    # output = "Привет, %s! Тебе %s лет." % (name, age)
    # print(output)
    # output = Template("Привет, $a! Тебе $b лет.")
    # print(output.substitute({"a": name, "b": age}))
    # + t - строки из Python 3.14
    output = f"\nПривет, {name}! Тебе {age} лет."
    print(output)

    # Проверяем результат
    # assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    import math
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r ** 2
    print(f"\nПлощадь круга: {area}")

    assert area == 1661.9025137490005, "Проверьте правильность расчета площади"

    # TODO сосчитайте длину окружности
    length = 2 * math.pi * r
    print(f"\nДлина окружности: {length}")

    assert length == 144.51326206513048, "Проверьте правильность расчета длины окружности"


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    import random
    # import numpy
    # TODO создайте список
    # l = numpy.random.randint(1, 101, size=10).tolist() # Если нужна более быстрая генерация больших списков
    l = [random.randint(1, 100) for _ in range(10)]
    # l = sorted(l) # sorted() возвращает новый отсортированный список
    l.sort() # l = l.sort() - использовать нельзя, вернет None

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    # from itertools import groupby
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    # l = list(dict.fromkeys(l)) # сохраняет порядок элементов
    # l = [key for key, _ in groupby(sorted(l))]
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    # d = {first[i]: second[i] for i in range(len(first))}
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
