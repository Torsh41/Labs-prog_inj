# как декоратор?
def func1(function):
    # вызываем вторую функцию
    print(function())

def func2():
    return "Я вторая функция"

func1(func2)

