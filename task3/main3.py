def powers_of_two(N):
    power = 1
    while power <= N:
        print(power, end=' ')
        power *= 2

# Запрашиваем у пользователя число N
N = int(input("Введите число N: "))

print("Целые степени двойки, не превосходящие", N, ":", end=' ')
powers_of_two(N)