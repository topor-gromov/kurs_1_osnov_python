class Matrix:
    def __init__(self, list1):
        self.resultmatrix = list1

    def __str__(self):
        temp_list = self.resultmatrix
        result_string = ''
        for elem in temp_list:
            for el in elem:
                result_string = result_string + str(el) + ' '
            result_string = result_string + '\n'
        return result_string

    def __add__(self, other):
        matrix_result = []
        matrix_1 = self.resultmatrix
        matrix_2 = other.resultmatrix
        if len(matrix_1) == len(matrix_2):
            for indx in range(0, len(matrix_1)):
                temp_list = []
                if len(matrix_1[indx]) == len(matrix_2[indx]):
                    temp_list_matrix_1 = matrix_1[indx]
                    temp_list_matrix_2 = matrix_2[indx]
                    for i in range(0, len(temp_list_matrix_1)):
                        temp_list.append(temp_list_matrix_1[i] + temp_list_matrix_2[i])
                    matrix_result.append(temp_list)
                else:
                    return 'Размеры матриц не совпадают.'
        else:
            return 'Размеры матриц не совпадают.'
        return matrix_result


list_matrix_1 = [[2, 3, 8], [5, 6, 5], [8, 8, 6]]
list_matrix_2 = [[7, 9, 8], [5, 9, 4], [2, 7, 9]]

print('Матрица №1:')
matrix1 = Matrix(list_matrix_1)
print(matrix1)

print('Матрица №2:')
matrix2 = Matrix(list_matrix_2)
print(matrix2)

matrix3_list = matrix1 + matrix2
print('Результат сложения матриц:')
if type(matrix3_list) == list:
    matrix3 = Matrix(matrix3_list)
    print(matrix3)
else:
    print(matrix3_list)
