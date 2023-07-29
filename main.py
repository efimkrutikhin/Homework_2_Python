import random

def generate_random_coins(n):
    # Генерация случайных значений монеток (H - герб, T - решка)
    return ''.join(random.choice(['H', 'T']) for _ in range(n))

def min_flips(coins):
    num_heads = coins.count("H")
    num_tails = len(coins) - num_heads
    return min(num_heads, num_tails)

# Генерируем случайные значения монеток
num_coins = 10  # Задайте здесь количество монеток, которые хотите сгенерировать
coins_on_table = generate_random_coins(num_coins)

# Выводим сгенерированные монетки и результат
print("Сгенерированные монетки:", coins_on_table)
result = min_flips(coins_on_table)
print("Минимальное количество переворотов:", result)