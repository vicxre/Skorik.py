#Даны числа х, у. Проверить истинность высказывания: «Точка с координатами (х, у) лежит во второй координатной четверти.

#ввод перменных
X = int(input("Введите значение переменной x:"))
Y = int(input("Введите значение переменной y:"))

#вторая координатная четверть
if X < 0 < Y:
    print("находится во второй координатной четверти")

else:
    print("не находится во второй координатной четверти")