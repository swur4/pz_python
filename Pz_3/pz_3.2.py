#2 задача:Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.
while True:
    try:
        A = int(input('Введите значение переменной A: '))
        B = int(input('Введите значение переменной B: '))
        break
    except ValueError:
        print("Число должно быть целым")
if A != B:
    A = A + B
    B = A
else:
    A = 0
    B = 0
print(f'Новое значение A: {A}')
print(f'Новое значение B: {B}')