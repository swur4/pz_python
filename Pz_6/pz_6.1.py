#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L включительно.
import random

while True:
    try:
        N = int(input('Введите размер списка: '))
        break
    except ValueError:
        print("Введите целое число!")

lst = []  #Инициализируем список

# енерация N случайных целых чисел от 1 до 100
for i in range(N):
    lst.append(random.randint(1, 100))

print(f'Сгенерированный список: {lst}')

#Ввод K и L
while True:
    try:
        K = int(input('Введите K: '))
        L = int(input('Введите L: '))
        if 1 <= K <= N and 1 <= L <= N and K <= L:
            break
        else:
            print(f"K и L должны быть в пределах от 1 до {N} и K должно быть меньше или равно L.")
    except ValueError:
        print("Введите целое число!")

#Вычисление суммы элементов с номерами от K до L
result_sum = sum(lst[K-1:L])  # Суммируем элементы от K до L (включительно)

print(f'Сумма элементов с номерами от {K} до {L}: {result_sum}')


