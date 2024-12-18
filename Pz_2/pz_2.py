#Дано трехзначное число.в нем зачеркнули первую справа цифру и прописали ее слева.
#вывести полученное число.

number = input("Введите число: ")
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Введите целое число")
        number = input("Введите число: ")
if 100 <= number <= 999: #проверка на трехзначность числа
    print("Изначальное число:", number)
    number2 = number % 10 #получаем число справа
    print("Первая цифра справа:", number2)
    result = (number // 10) + (number2 * 100) #переносим правое число налево
    print("Конечное число:", result)
else:
    print("Введите трехзначное число!!")
