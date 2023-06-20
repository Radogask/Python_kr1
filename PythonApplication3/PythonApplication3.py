def factorials_sum(n):
    factorial = 1 
    sum = 0 
    for i in range(1, n+1):
        factorial *= i 
        sum += factorial 
    return sum

n = int(input("Введите n: "))
print("Сумма факториалов:", factorials_sum(n))
