# Обязательные задачи в презентации.
# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

max_differ = 1
lst = (1, 5, 3, 4, 1, 7, 8 , 15 , 9 )
lst_result = []
print(lst)
for i in range(0,len(lst)):
    min_number = lst[i]
    sum_of_step = 1
    j = 0
    while j < len(lst):
        if lst[j] == lst[i]+sum_of_step:
            sum_of_step+=1
            j=0
        else:
            j+=1
    if sum_of_step > max_differ:
        max_differ = sum_of_step
        lst_result.clear()
        lst_result.append([min_number , min_number+max_differ-1])
    elif sum_of_step == max_differ:
        lst_result.append([min_number , min_number+max_differ-1])
            
print(lst_result)