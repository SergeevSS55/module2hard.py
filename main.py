def password(n):
    result = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if (i + j) % n == 0:
                result = result + str(i) + str(j)
    return result
number = int(input("Введите число для пароля от 3 до 20: "))
result = password(number)
print(f"Пароль для числа {number}: {result}")