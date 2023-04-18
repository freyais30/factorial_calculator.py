def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Введите число для расчета факториала: "))
result = factorial(n)
print(f"Факториал числа {n} равен {result}")
