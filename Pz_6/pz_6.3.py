#Дан список размера N, все элементы которого, кроме последнего, упорядочены повозрастанию. Сделать список упорядоченным, переместив последний элемент на новую позицию.
import random
while True:
    try:
        N = int(input('Введите размер списка: '))
        break
    except ValueError:
        print("Введите целое число!")

# Генерация случайного списка
numbers = random.sample(range(1, 100), N)
print(f'Список перед упорядочиванием: {numbers}')

# Вставка последнего элемента на правильную позицию
last_element = numbers[-1]
sorted_numbers = []

#Строим новый отсортированный список
for i in range(N - 1):
    if numbers[i] <= last_element:
        sorted_numbers.append(numbers[i])
    else:
        sorted_numbers.append(last_element)
        last_element = numbers[i]

#Добавляем оставшийся элемент, если он еще не добавлен
sorted_numbers.append(last_element)

print(f'Упорядоченный список: {sorted_numbers}')
