import random
import termcolor


class LotoCard():

    def __init__(self, name_gamer):
        self.name = name_gamer


    def create_lotocard(self):
        lotocard = []
        list_all_number = []
        for row in range(0, 3):
            temp_list = []
            for col in range(0, 5):
                flag_exit = False
                flag_find_elem = False
                while not flag_exit:
                    val_cell = random.randint(1, 90)
                    if list_all_number.count(val_cell) == 0:
                        for el in temp_list:
                            if str(val_cell)[:1] == str(el)[:1]:
                                flag_find_elem = True
                                break
                            elif len(str(val_cell)) == 1 and len(str(el)) == 1:
                                flag_find_elem = True
                                break

                        # условие чтобы в карточке было не более 2 значений одного порядка. Для более "гладкой" карты.
                        if len([el for elem in list_all_number if elem // 10 == val_cell // 10]) >= 2:
                            flag_find_elem = True

                        if not flag_find_elem:
                            temp_list.append(val_cell)
                            list_all_number.append(val_cell)
                            flag_exit = True
                        else:
                            flag_find_elem = False

            temp_list_row = []
            # расставляем числа в карточке согласно их порядку (1-9 в первый столбец, 10-19 во второй и тд.)
            for elem in sorted(temp_list):
                if elem > 9:
                    for i in range(len(temp_list_row), elem // 10):
                        temp_list_row.append('')
                    temp_list_row.append(elem)
                else:
                    temp_list_row.append(elem)
            if len(temp_list_row) <  9:
                for i in range(len(temp_list_row), 9):
                    temp_list_row.append('')

            lotocard.append(temp_list_row)

        return lotocard


    @staticmethod
    def print_card(self, is_user):
        result_string = ''
        for list1 in self:
            for list2 in list1:
                result_string = result_string + str(list2) + '\t'
            result_string = result_string + '\n'

        if is_user:
            print(termcolor.colored('----------------------------------------', 'green'))
            print(termcolor.colored(result_string[:len(result_string) - 2], 'red'))
            print(termcolor.colored('----------------------------------------', 'green'))
        else:
            print(termcolor.colored('----------------------------------------', 'green'))
            print(termcolor.colored(result_string[:len(result_string) - 2], 'blue'))
            print(termcolor.colored('----------------------------------------', 'green'))

class LotoGame(LotoCard):
    def __init__(self, human, human_name, computer, comp_name):
        self.computercard = computer
        self.humancard = human
        self.humanname = human_name
        self.compname = comp_name
        self.delitem = False
        self.humancountnumber = 15
        self.compcountnumber = 15

    def start(self):
        bank_number = [elem for elem in range(1, 91)]
        print('----------Старт игры--------------')
        flag_exit = False
        while not flag_exit:
            current_number = random.choice(bank_number)
            bank_number.pop(bank_number.index(current_number))
            print(f'Карточка игрока: {self.humanname}')
            self.print_card(self.humancard, True)
            print(f'Карточка игрока: {self.compname}')
            self.print_card(self.computercard, False)
            print(f'Новый бочонок: {current_number}. Осталось бочонков {len(bank_number)}.')
            answer_user = input('Хотите зачеркнуть? y/n ')
            if answer_user == 'y':
                self.check_number(current_number)
                if not self.delitem:
                    flag_exit = True
                    print('Вы проиграли!')
                if self.humancountnumber == 0:
                    print(f'Победа игрока: {self.humanname}')
                    flag_exit = True
            elif answer_user == 'n':
                self.check_number(current_number)
                if self.delitem:
                    flag_exit = True
                    print('Вы проиграли!')
            else:
                print('Вы ввели недопустимый символ! Игра прекращена!')
                flag_exit = True

            if self.compcountnumber == 0:
                print(f'Победа игрока: {self.compname}')
                flag_exit = True

    def check_number(self, number):
        indx = 0
        self.delitem = False
        for elem in self.humancard:
            if elem.count(number) > 0:
                elem[elem.index(number)] = 'X'
                self.delitem = True
                self.humancard[indx] = elem
                self.humancountnumber = self.humancountnumber - 1
                break
            else:
                LotoGame.delitem = False
            indx = indx + 1

        indx = 0
        for elem in self.computercard:
            if elem.count(number) > 0:
                elem[elem.index(number)] = 'X'
                self.computercard[indx] = elem
                self.compcountnumber = self.compcountnumber - 1
                break
            indx = indx + 1




user_card = LotoCard(input('Введите имя игрока: '))
comp_card = LotoCard('Компьютер')

game1 = LotoGame(user_card.create_lotocard(), user_card.name, comp_card.create_lotocard(), comp_card.name)
game1.start()
