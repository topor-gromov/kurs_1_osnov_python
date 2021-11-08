my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in my_list:
    user_name = ''
    string_len = len(item) - 1
    while item[string_len] != ' ':
        user_name = item[string_len] + user_name
        string_len = string_len - 1

    print(f'Привет, {user_name.title()}!')
