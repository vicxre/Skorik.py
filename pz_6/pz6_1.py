#Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и
#нечетные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый
#номер первого элемента, нарушающего закономерность.

def check_alternating_even_odd(lst):

    #проверка что список не пустой
    if not lst:
        return "список пуст"

    my_list = [1, 4, 3, 6]
    result = check_alternating_even_odd(my_list)

    #с первого элемента списка
    is_even = lst[0] % 2 == 0

    for i in range(1, len(lst)):
        # Если текущий элемент должен быть четным, но он нечетный (или наоборот)
        if (lst[i] % 2 == 0) != is_even:
            return i + 1

        #четность на нечетность
        is_even = not is_even

    #если ошибок нет, возвращаем 0
    return 0

    print(result)


