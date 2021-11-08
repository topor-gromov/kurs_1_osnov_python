my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp_list =[]
for item in my_list:
    for letter in item:
        if letter != '-' and letter != '+':
            if letter.isnumeric():
                temp_list.append('"')
                temp_list.append(f'{int(item):02d}')
                temp_list.append('"')
            else:
                temp_list.append(item)
            break
        else:
            temp_list.append('"')
            temp_list.append(f'{letter}{abs(int(item)):02d}')
            temp_list.append('"')
            break

result_message = temp_list[0] + ' '
flag_marks = True
for item in temp_list[1:]:
    if item == '"':
        if flag_marks:
            result_message = result_message + item
            flag_marks = False
        else:
            result_message = result_message + item + ' '
            flag_marks = True
    elif item.isnumeric():
        result_message = result_message + item
    elif item[0] == '+' or item[0] == '-':
        result_message = result_message + item
    else:
        result_message = result_message + item + ' '


print(result_message)






