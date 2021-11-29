import re
import sys

RE_EMAIL = re.compile(r'^([a-zA-Z.]+)[@]([a-zA-Z]+[.][a-zA-Z]+$)')


def email_parse(def_user_email):
    match_user_email = RE_EMAIL.match(user_email)
    def_dict = {}
    if match_user_email is not None:
        def_dict['username'] = match_user_email.group(1)
        def_dict['domain'] = match_user_email.group(2)
    else:
        raise ValueError(f'Введён некорректный адрес: {user_email}')
    return def_dict


user_email = input('Введите адрес электронной почты: ')
if len(user_email) > 0:
    result_dict = email_parse(user_email)
    print(f'Имя пользователя: {result_dict["username"]}')
    print(f'Почтовый домен: {result_dict["domain"]}')
else:
    sys.exit('Вы не ввели адрес электронной почты!')
