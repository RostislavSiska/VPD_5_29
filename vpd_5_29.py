"vpd_5_29"

from math import factorial

def row_sin(x, end=1000):
    """
    Ищет значение ряда Маклорена для  sin(x).
    
    :param x: Значение x
    :param end: Заданное значение для цикла for
    :return: Значение sin(x)
    """
    summ = 0
    for i in range(end):
        summ = summ + (((-1)**i) * ((x**(2*i + 1))/(factorial(2*i + 1))))
    return summ

def row_ch(x, end=1000):
    """
    Ищет значение ряда Маклопена для ch(x).

    :param x: Значение x
    :param end: Заданное значения для цикла for
    :return: Значение ch(x)
    """
    summ = 0
    for i in range(end):
        summ = summ + ((x**(2*i))/(factorial(2*i)))
    return summ

def row_arctg(x, end=1000):
    "Тема сделяль"
    pass

def menu():
    """
    Пользовательское меню для выбора функций.
    """
    while True:
        print("0.Выход\n\
1.Функция sin(x)\n\
2.Функция ch(x)\n\
3.Функция arctg(x)")
        try:
            n = input("Введите номер операции: ")
            if n.isdigit() is False or int(n)>4:
                raise ValueError
        except ValueError:
            print("Некоректный ввод")
        if n == "0":
            print("Пока.")
            break
        if n == "1":
            try:
                print(f"Значение sin(x): {row_sin(x=int(input("Введите значение x: ")))}")
            except ValueError:
                print("Некоректный ввод")
        if n == "2":
            try:
                print(f"Значение ch(x): {row_ch(x=int(input("Введите значение x: ")))}")
            except ValueError:
                print("Некоректный ввод")
        if n == "3":
            try:
                x = float(input("Введите значение x: "))
                if x < -1 or x > 1:
                    raise ValueError
                print(f"Значение arctg(x): {row_arctg(x)}")
            except ValueError:
                print("Некоректный ввод")

menu()
