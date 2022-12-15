def func1(n):
    def func2(n, arg=25):
        #ptint("Парамметр =", parameter)
        return n + arg
    
    res = func2(n)
    return res
    

n = int(input("Введите число:\n"))
print("Параметр + введенное число =", func1(n))
