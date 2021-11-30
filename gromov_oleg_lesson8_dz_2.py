import re

RE_PARSE_GROUP_1 = '^([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)'
RE_PARSE_GROUP_2 = '\s[- ]+([\[]\d{2}[\/][a-zA-Z]{3}[\/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}[ ][+]\d{4}[\]])'
RE_PARSE_GROUP_3 = '\s["]([A-Z]{3})'
RE_PARSE_GROUP_4 = '\s([\/][a-z]+[\/][a-z]+[_]\d+)'
RE_PARSE_GROUP_5 = '\s[A-Z]+[\/]\d[.]\d["]\s(\d+)\s(\d+)'

# Слишком длинная строка регулярного выражения, поэтому разбил на несколько подстрок.
# ^([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)\s[- ]+([\[]\d{2}[\/][a-zA-Z]{3}[\/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}[ ][+]\d{4}[\]])\s["]([A-Z]{3})\s([\/][a-z]+[\/][a-z]+[_]\d+)\s[A-Z]+[\/]\d[.]\d["]\s(\d+)\s(\d+)

re_parse_result = RE_PARSE_GROUP_1 + RE_PARSE_GROUP_2 + RE_PARSE_GROUP_3 + RE_PARSE_GROUP_4 + RE_PARSE_GROUP_5

parse_s = re.compile(re_parse_result)
result_list = []

with open('nginx_logs.txt') as f:
    for line in f:
        res = parse_s.match(f.readline())
        if res is not None:
            temp_tuple = (res.group(1), res.group(2), res.group(3), res.group(4), res.group(5),res.group(6))
            result_list.append(temp_tuple)

count_string_for_write = 50 # количество строк для вывода в терминал
count_string_write = 0
for list_str in result_list:
    if count_string_write < count_string_for_write:
        print(list_str)
    else:
        break
    count_string_write = count_string_write + 1

