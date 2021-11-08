my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

result_message = ''

for item in my_list:
    for letter in item:
        if letter != '-' and letter != '+':
            if letter.isnumeric():
                result_message = result_message + '"'
                result_message = result_message + (f'{int(item):02d}')
                result_message = result_message + '" '
            else:
                result_message = result_message + item + ' '
            break
        else:
            result_message = result_message + '"'
            result_message = result_message + (f'{letter}{abs(int(item)):02d}')
            result_message = result_message + '" '
            break

print(result_message)