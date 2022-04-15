cost_list = [57.8, 12.63, 23.01, 9.45, 15, 17.34, 30.02, 94.12, 8.11, 5.99]

# Пункт А
result_message = ''
flag_begin = True
for cost in cost_list:
    if flag_begin == False:
        result_message = result_message + ', '
    cost_string = str(cost)
    if cost != int(cost):
        dot_index = cost_string.index('.')
        cost_1 = cost_string[0:dot_index]
        cost_2 = cost_string[dot_index+1:]
        if len(cost_2) == 1:
            cost_2 = cost_2 + '0'
        result_message = result_message + f'{cost_1} руб {cost_2} коп'
        flag_begin = False
    else:
        result_message = result_message + f'{cost} руб 00 коп'
        flag_begin = False

print('-----------------------------------------Пункт А--------------------------------------------')
print(result_message)
print('--------------------------------------------------------------------------------------------')

# Пункт В
print('-----------------------------------------Пункт B--------------------------------------------')
print(f'ID cписка до сортировки: {id(cost_list)}. Список до сортировки: {cost_list}')
cost_list.sort()
print(f'ID cписка после сортировки: {id(cost_list)}. Список после сортировки(по возрастанию): {cost_list}')
print('--------------------------------------------------------------------------------------------')

# Пункт С
print('-----------------------------------------Пункт C--------------------------------------------')
new_cost_list = cost_list.copy()
new_cost_list.sort(reverse=True)
print(f'ID исходного списка: {id(cost_list)}.')
print(f'ID нового списка: {id(new_cost_list)}.')
print(f'Новый список, отсортированный по убыванию: {new_cost_list}')
print('--------------------------------------------------------------------------------------------')

# Пункт D
print('-----------------------------------------Пункт D--------------------------------------------')
print('5 самых дорогих товаров:')
for cost in new_cost_list[:5]:
    print(cost)

print('--------------------------------------------------------------------------------------------')