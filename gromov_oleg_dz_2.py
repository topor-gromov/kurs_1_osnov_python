numbers_list = []  # список для кубов нечётных чисел от 1 до 1000. Исходные данные.

for number in range(1, 1001, 2):
    numbers_list.append(number ** 3)


### Пункт A
amount = 0  # Переменная для записи суммы чисел.

for numbers in numbers_list:
    while_flag = True
    temp_amount = numbers % 10
    temp_number = numbers // 10
    if temp_number > 0:
        while while_flag:
            temp_amount = temp_amount + (temp_number % 10)
            temp_number = temp_number // 10
            if temp_number == 0:
                while_flag = False
    if temp_amount % 7 == 0:
        amount = amount + numbers

print('Сумма чисел списка, удовлетворяющих требованию пункта "a", равна: ',amount)
###