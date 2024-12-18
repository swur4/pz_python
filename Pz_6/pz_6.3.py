#Дан список размера N, все элементы которого, кроме последнего, упорядочены повозрастанию. Сделать список упорядоченным, переместив последний элемент на новую позицию.

import random

def insert_last_element(sorted_list):
    #Извлекаем последний элемент
    last_element = sorted_list[-1]

    #Перемещаем его влево, пока не найдем правильное место
    i = len(sorted_list) - 2  # Начинаем с предпоследнего элемента
    while i >= 0 and sorted_list[i] > last_element:
        i -= 1

    #Вставляем элемент на правильное место
    sorted_list[i + 1:] = [last_element] + sorted_list[i + 1:-1]

#Генерируем случайный список размера N
while True:
    try:
        N = int(input('Введите размер списка: '))
        break
    except ValueError:
        print("Введите целое число!")
sorted_list = sorted(random.sample(range(1, 100), N - 1))  #Генерируем N-1 уникальных случайных чисел и сортируем
last_element = random.randint(1, 100)  # енерируем последний элемент
sorted_list.append(last_element)  #Добавляем последний элемент

print("Исходный список:", sorted_list)
insert_last_element(sorted_list)
print("Упорядоченный список:", sorted_list)

