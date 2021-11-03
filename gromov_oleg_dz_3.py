
for index in range(1,101):

    if index % 10 == 1 and (index == 1 or index >= 21):
        print(index, 'процент')
    elif index % 10 >= 2 and index % 10 <= 4 and (index <= 5 or index >= 22):
        print(index, 'процента')
    else:
        print(index,'процентов')

