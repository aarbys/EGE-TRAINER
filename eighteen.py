import pandas as pd
import random
from openpyxl.styles import Border, Side
import openpyxl


def question():
    type_of_problem = random.randint(1, 1)
    if type_of_problem == 1:
        if random.randint(1, 2) == 1:
            top_right_hard()
        else:
            top_right_hard()
    elif type_of_problem == 2:
        if random.randint(1, 2) == 1:
            top_right()
        else:
            top_right_M()


def maximum_func(sol_tab, table, a_o_l):
    for i in range(1, a_o_l):
        for j in range(1, a_o_l):
            sol_tab[i][j] = max(sol_tab[i - 1][j], sol_tab[i][j - 1]) + table[i][j]
    return sol_tab


def minimum_func(sol_tab, table, a_o_l):
    for i in range(1, a_o_l):
        for j in range(1, a_o_l):
            sol_tab[i][j] = min(sol_tab[i - 1][j], sol_tab[i][j - 1]) + table[i][j]
    return sol_tab


def start(amount_of_lines):
    print('Квадрат разлинован на {}*{} клеток.'.format(amount_of_lines, amount_of_lines))
    print(
        'Исполнитель Робот может перемещаться по клеткам, выполняя за одно перемещение одну из двух команд: вправо или вниз.')
    print('По команде вправо Робот перемещается в соседнюю правую клетку, по команде вниз — в соседнюю нижнюю.')
    print('При попытке выхода за границу квадрата Робот разрушается.')
    print('Перед каждым запуском Робота в каждой клетке квадрата лежит монета достоинством от 1 до 550.')
    print('Так же в файле могут встречаться стенки, ударяясь об которые робот ломается')


def gen_file():
    x = random.randint(11, 11)
    first_table = []
    sex_after_siggarets = ''
    for i in range(x):  # Number
        string = ''
        for j in range(x):  # Letter
            smth = random.randint(1, 550)
            while str(smth) in sex_after_siggarets:
                smth = random.randint(1, 550)
            string += str(smth) + ' '
            sex_after_siggarets += str(smth) + ' '
        strings = string.split()
        strings = list(map(int, strings))
        first_table.append(strings)
    dictionary = dict()
    for i in range(x):  # Number
        for j in range(x):  # Letter
            i_hate_my_life = first_table[i][j]
            key_from_dict = first_table[0][j]
            if i == 0:
                dictionary[i_hate_my_life] = [i_hate_my_life]
            else:
                dictionary[key_from_dict].append(i_hate_my_life)
    df = pd.DataFrame(dictionary)
    df.to_excel('18.xlsx', index=False, header=False)
    wb = openpyxl.load_workbook('18.xlsx')
    ws = wb['Sheet1']
    type_and_color_borders = Side(border_style='thick', color='000000')

    b_b = Border(bottom=type_and_color_borders)
    b_r = Border(right=type_and_color_borders)
    letter = chr(64+x)
    number = x
    start_cell = letter+str(number)
    for smth in range(1,x+1):
        cell_m_n = letter + str(smth)
        cell_m_L = chr(64+smth) + str(number)
        ws[cell_m_n].border = b_r
        ws[cell_m_L].border = b_b
    ws[start_cell].border = Border(right=type_and_color_borders,bottom=type_and_color_borders)
    wb.save('18.xlsx')
    return first_table, x


def example():
    print('Пример входных данных:')
    a = [[1, 8, 8, 4], [10, 1, 1, 3], [1, 3, 12, 2], [2, 3, 5, 6]]
    for i in a:
        print(*i)


def example_solution(psih, type_position):
    a = [[1, 8, 8, 4], [10, 1, 1, 3], [1, 3, 12, 2], [2, 3, 5, 6]]
    if type_position == 1:  # bottom left
        a.reverse()
    elif type_position == 2:  # bottom right
        a.reverse()
        for smth in range(len(a)):
            a[smth].reverse()
    elif type_position == 3:  # top right
        for smth in range(len(a)):
            a[smth].reverse()
    answer = []
    solution_table = []
    for i in range(4):
        line = []
        for j in range(4): line.append(0)
        solution_table.append(line)
    if a[0][0] % psih == 0:
        solution_table[0][0] = a
    else:
        solution_table[0][0] = 0
    for i in range(1, 4):
        if a[i][0] % psih == 0:
            solution_table[i][0] = solution_table[i - 1][0] + a[i][0]
        else:
            solution_table[i][0] = solution_table[i - 1][0]
        if a[0][i] % psih == 0:
            solution_table[0][i] = solution_table[0][i - 1] + a[0][i]
        else:
            solution_table[0][i] = solution_table[0][i - 1]

    for i in range(1, 4):
        for j in range(1, 4):
            if a[i][j] % psih == 0:
                solution_table[i][j] = max(solution_table[i - 1][j], solution_table[i][j - 1]) + a[i][j]
            else:
                solution_table[i][j] = max(solution_table[i - 1][j], solution_table[i][j - 1])
    answer.append(solution_table[-1][-1])
    for i in range(1, 4):
        for j in range(1, 4):
            if a[i][j] % psih == 0:
                solution_table[i][j] = min(solution_table[i - 1][j], solution_table[i][j - 1]) + a[i][j]
            else:
                solution_table[i][j] = min(solution_table[i - 1][j], solution_table[i][j - 1])
    answer.append(solution_table[-1][-1])
    return answer


def check_answer(correct_answer):
    x = input().split()  # User's input
    x = list(map(int, x))
    if x[0] == correct_answer[0] and x[1] == correct_answer[1]:
        print('Да,Вы верны!')
    else:
        print('Вы не правы(')
        print('Хотите узнать верный ответ? (Да/Нет)')
        y_n = input()  # Variable for answer question upper
        if y_n == 'Да':
            print(correct_answer)
        elif y_n != 'Нет':
            print('Что?')
            print('Надеюсь, Вы хотели узнать ответ')
            print(*correct_answer)
    exit()


def solution_easy(table: 'input table from EXCEL', a_o_l: 'Amount of lines'):
    solution_table = []  # Table with full solution of this problem like a solution table[NUMBER][LETTER]
    for i in range(a_o_l):
        line = []  # Auxyliary variable will not usable
        for j in range(a_o_l):
            line.append(0)
        solution_table.append(line)
    solution_table[0][0] = table[0][0]

    for i in range(1, a_o_l):
        solution_table[i][0] = solution_table[i - 1][0] + table[i][0]
        solution_table[0][i] = solution_table[0][i - 1] + table[0][i]

    solution_table = maximum_func(solution_table, table, a_o_l)

    maximum = solution_table[a_o_l - 1][a_o_l - 1]  # First answer in our problem
    solution_table = minimum_func(solution_table, table, a_o_l)

    minimum = solution_table[a_o_l - 1][a_o_l - 1]  # Seconde answer in our problem
    answer = [maximum, minimum]  # Full answer in one variable(probably changed)
    return answer


def top_left_easy():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    correct_answer = solution_easy(table, amount_of_lines)  # Correct answer taken from solution
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой верхней клетки в правую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 41 и 22.')
    check_answer(correct_answer)


def solution_medium(table: ' Excel table', a_o_l, psih: ' Variable divider'):
    answer = []
    solution_table = []  # Table with full solution of this problem like a solution table[NUMBER][LETTER]
    for i in range(a_o_l):
        line = []  # Auxyliary variable will not usable
        for j in range(a_o_l): line.append(0)
        solution_table.append(line)
    if table[0][0] % psih == 0:
        solution_table[0][0] = table[0][0]
    else:
        solution_table[0][0] = 0
    for i in range(1, a_o_l):
        if table[i][0] % psih == 0:
            solution_table[i][0] = solution_table[i - 1][0] + table[i][0]
        else:
            solution_table[i][0] = solution_table[i - 1][0]
        if table[0][i] % psih == 0:
            solution_table[0][i] = solution_table[0][i - 1] + table[0][i]
        else:
            solution_table[0][i] = solution_table[0][i - 1]

    for i in range(1, a_o_l):
        for j in range(1, a_o_l):
            if table[i][j] % psih == 0:
                solution_table[i][j] = max(solution_table[i - 1][j], solution_table[i][j - 1]) + table[i][j]
            else:
                solution_table[i][j] = max(solution_table[i - 1][j], solution_table[i][j - 1])

    answer.append(solution_table[-1][-1])  # Adding to correct answer first value for this problem
    for i in range(1, a_o_l):
        for j in range(1, a_o_l):
            if table[i][j] % psih == 0:
                solution_table[i][j] = min(solution_table[i - 1][j], solution_table[i][j - 1]) + table[i][j]
            else:
                solution_table[i][j] = min(solution_table[i - 1][j], solution_table[i][j - 1])

    answer.append(solution_table[-1][-1])  # Adding to correct answer seconde value for this problem
    return answer


def top_left_medium():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    psih = random.randint(2, 10)  # Random number that will be divider
    correct_answer = solution_medium(table, amount_of_lines, psih)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой,если её достоинство кратно {};\n это также относится к начальной и конечной клетке маршрута Робота.'.format(
            psih))
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой верхней клетки в правую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    c_e_1, c_e_2 = example_solution(psih)  # Automatic answer for a table from funcution example
    print('Для указанных входных данных ответом должна быть пара чисел {} и {}.'.format(c_e_1, c_e_2))
    check_answer(correct_answer)


def top_right_solution(table: 'input table from EXCEL', a_o_l: 'Amount of lines'):
    for x in range(len(table)):
        table[x].reverse()
    answer = solution_easy(table, a_o_l)
    return answer


def top_right():
    table, amount_of_lines = gen_file()
    correct_answer = top_right_solution(table, amount_of_lines)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из правой верхней в левую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 35 и 15.')
    check_answer(correct_answer)


def top_right_M_solution(table: ' Excel table', a_o_l, psih: ' Variable divider'):
    for x in range(len(table)):
        table[x].reverse()
    return solution_medium(table, a_o_l, psih)


def top_right_M():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    psih = random.randint(2, 10)  # Random number that will be divider
    correct_answer = top_right_M_solution(table, amount_of_lines, psih)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой,если её достоинство кратно {};\n это также относится к начальной и конечной клетке маршрута Робота.'.format(
            psih))
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из правой верхней клетки в левую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    c_e_1, c_e_2 = example_solution(psih, 3)  # Automatic answer for a table from funcution example
    print('Для указанных входных данных ответом должна быть пара чисел {} и {}.'.format(c_e_1, c_e_2))
    check_answer(correct_answer)


def bottom_left_soliution(table: 'input table from EXCEL', a_o_l: 'Amount of lines'):
    table.reverse()
    answer = solution_easy(table, a_o_l)
    return answer


def bottom_left():
    table, amount_of_lines = gen_file()
    correct_answer = bottom_left_soliution(table, amount_of_lines)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой нижней в правую верхнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 35 и 15.')
    check_answer(correct_answer)

def bottom_left_M_solution(table: ' Excel table', a_o_l, psih: ' Variable divider'):
    table.reverse()
    return solution_medium(table, a_o_l, psih)

def bottom_left_M():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    psih = random.randint(2, 10)  # Random number that will be divider
    correct_answer = bottom_left_M_soliution(table, amount_of_lines, psih)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой,если её достоинство кратно {};\n это также относится к начальной и конечной клетке маршрута Робота.'.format(
            psih))
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой нижней клетки в правую верхнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    c_e_1, c_e_2 = example_solution(psih, 1)  # Automatic answer for a table from funcution example
    print('Для указанных входных данных ответом должна быть пара чисел {} и {}.'.format(c_e_1, c_e_2))
    check_answer(correct_answer)

def bottom_right_solution(table: 'input table from EXCEL', a_o_l: 'Amount of lines'):
    table.reverse()
    for x in range(len(table)): table[x].reverse()
    return solution_easy(table, a_o_l)

def bottom_right():
    table, amount_of_lines = gen_file()
    correct_answer = bottom_right_solution(table, amount_of_lines)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из правой нижней в левую верхнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 41 и 22.')
    check_answer(correct_answer)

def bottom_right_M_solution(table: ' Excel table', a_o_l, psih: ' Variable divider'):
    table.reverse()
    for x in range(len(table)): table[x].reverse()
    return solution_medium(table, a_o_l, psih)

def bottom_right_M():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    psih = random.randint(2, 10)  # Random number that will be divider
    correct_answer = bottom_right_M_soliution(table, amount_of_lines, psih)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой,если её достоинство кратно {};\n это также относится к начальной и конечной клетке маршрута Робота.'.format(
            psih))
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из правой нижней клетки в левую верхнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    c_e_1, c_e_2 = example_solution(psih, 2)  # Automatic answer for a table from funcution example
    print('Для указанных входных данных ответом должна быть пара чисел {} и {}.'.format(c_e_1, c_e_2))
    check_answer(correct_answer)

def gen_borders(L:str,corner_N, corner_L,len_N, len_L):
    top = bottom = right = left = Side(border_style='thick',color='000000')
    wb =openpyxl.load_workbook('18.xlsx')
    ws = wb['Sheet1']
    letter = chr(65+corner_L)
    number = str(corner_N)
    corner = letter + number
    if L == 'TL':
        ws[corner].border = Border(bottom=bottom, right=right)
        for i in range(1,len_N): # Moving by numbers
            cell = letter + str(int(number) - i)
            ws[cell].border = Border(right=right)
        for i in range(1,len_L): # Moving by letters
            cell = chr(ord(letter) - i) + number
            ws[cell].border = Border(bottom=bottom)
    elif L == 'TR':
        ws[corner].border = Border(left=left,bottom=bottom)
        for i in range(1,len_N):# Moving by numbers
            cell = letter + str(int(number) - i)
            ws[cell].border = Border(left=left)
        for i in range(1,len_L):# Moving by letters
            cell = chr(ord(letter) + i) + number
            ws[cell].border = Border(bottom=bottom)
    elif L == 'BL':
        ws[corner].border = Border(right=right,top=top)
        for i in range(1,len_N):# Moving by numbers
            cell = letter + str(int(number) + i)
            ws[cell].border = Border(right=right)
        for i in range(1,len_L):# Moving by letters
            cell = chr(ord(letter) - i) + number
            ws[cell].border = Border(top=top)
    else:
        ws[corner].border = Border(left=left,top=top)
        for i in range(1,len_N):# Moving by numbers
            cell = letter + str(int(number) + i)
            ws[cell].border = Border(left=left)
        for i in range(1,len_L):# Moving by letters
            cell = chr(ord(letter) + i) + number
            ws[cell].border = Border(top=top)

    wb.save('18.xlsx')

def top_left_hard_solution(table, a_o_l, corner_N, corner_L, len_N, len_L):
    def max_func_special(sol_tab, table, a_o_l):
        for i in range(1, a_o_l):
            for j in range(1, a_o_l):
                if sol_tab[i][j] != -1:
                    sol_tab[i][j] = max(sol_tab[i - 1][j], sol_tab[i][j - 1]) + table[i][j]
        return sol_tab

    def min_func_special(sol_tab, table, a_o_l):
        for i in range(1, a_o_l):
            for j in range(1, a_o_l):
                if sol_tab[i][j] != sum_table_1:
                    sol_tab[i][j] = min(sol_tab[i - 1][j], sol_tab[i][j - 1]) + table[i][j]
        return sol_tab

    def nullifier(corner_N, len_N, corner_L, len_L, sol_tab, what):
        for NUMBER in range(corner_N - len_N, corner_N):
            for LETTER in range(corner_L - len_L+1, corner_L+1):
                sol_tab[NUMBER][LETTER] = what
        return sol_tab

    sum_table_1 = 1
    for i in table:
        sum_table_1+=sum(i)

    sol_tab = []  # Table with full solution of this problem like a solution table[NUMBER][LETTER]

    for i in range(a_o_l):
        line = []  # Auxyliary variable will not usable
        for j in range(a_o_l):
            line.append(0)
        sol_tab.append(line)

    sol_tab[0][0] = table[0][0]
    for i in range(1, a_o_l):
        sol_tab[i][0] = sol_tab[i - 1][0] + table[i][0]
        sol_tab[0][i] = sol_tab[0][i - 1] + table[0][i]

    sol_tab = maximum_func(sol_tab, table, a_o_l)

    sol_tab = nullifier(corner_N, len_N, corner_L, len_L, sol_tab, -1)
    sol_tab = max_func_special(sol_tab, table, a_o_l)

    maximum = sol_tab[a_o_l - 1][a_o_l - 1]  # First answer in our problem

    sol_tab = minimum_func(sol_tab, table, a_o_l)

    sol_tab = nullifier(corner_N, len_N, corner_L, len_L, sol_tab, sum_table_1)

    sol_tab = min_func_special(sol_tab, table, a_o_l)

    minimum = sol_tab[a_o_l - 1][a_o_l - 1]  # Seconde answer in our problem
    answer = [maximum, minimum]  # Full answer in one variable(probably changed)
    return answer

def top_left_hard():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    corner_N, corner_L = random.randint(5, amount_of_lines - 5), random.randint(5, amount_of_lines - 5)
    len_N, len_L = random.randint(2, 4), random.randint(2, 4)
    gen_borders('TL',corner_N, corner_L,len_N, len_L)
    correct_answer = top_left_hard_solution(table, amount_of_lines, corner_N, corner_L, len_N, len_L)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой верхней клетки в правую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 41 и 22.')
    check_answer(correct_answer)

def top_right_hard_solution(table, a_o_l, corner_N, corner_L, len_N, len_L):
    answer =[]

    def nullifier(corner_N, len_N, corner_L, len_L, sol_tab, what):
        for NUMBER in range(corner_N-len_N,corner_N):
            for LETETER in range(corner_L-len_L+2,corner_L+2):
                sol_tab[NUMBER][LETETER] = what
        return sol_tab

    sum_table = 1
    for i in table:
        sum_table+=sum(i)

    sol_tab =[] # solution table two-dimensional massif [NUMBER][LETTER]
    for i in range(a_o_l):
        line =[]
        for j in range(a_o_l):
            line.append(0)
        sol_tab.append(line)

    sol_tab[0][-1] = table[0][-1]
    for NUMBER in range(1,a_o_l):
        sol_tab[NUMBER][-1] = sol_tab[NUMBER-1][-1] + table[NUMBER][-1]
        sol_tab[0][a_o_l - NUMBER - 1] = sol_tab[0][a_o_l - NUMBER] + table[0][a_o_l - NUMBER - 1] # There is NUMBER like a LETTER
        # I wanted to unite two cilce FOR

    for NUMBER in range(1, a_o_l):
        for LETTER in range(1, a_o_l):
            n_l = a_o_l - 1 - LETTER # new letter
            n = NUMBER
            sol_tab[n][n_l] = max(sol_tab[n - 1][n_l], sol_tab[n][n_l + 1]) + table[n][n_l]

    sol_tab = nullifier(corner_N, len_N, corner_L+1, len_L, sol_tab, -1)

    for NUMBER in range(1, a_o_l):
        for LETTER in range(1, a_o_l):
            n_l = a_o_l - 1 - LETTER  # new letter
            n = NUMBER
            if sol_tab[n][n_l] != -1:
                sol_tab[n][n_l] = max(sol_tab[n - 1][n_l], sol_tab[n][n_l + 1]) + table[n][n_l]
            else:
                continue


    answer.append(sol_tab[-1][0])
    sol_tab = nullifier(corner_N, len_N, corner_L+1, len_L, sol_tab, sum_table)

    for NUMBER in range(1, a_o_l):
        for LETTER in range(1, a_o_l):
            n_l = a_o_l - 1 - LETTER  # new letter
            n = NUMBER
            if sol_tab[n][n_l] != sum_table:
                sol_tab[n][n_l] = min(sol_tab[n - 1][n_l], sol_tab[n][n_l + 1]) + table[n][n_l]
            else:
                continue
    answer.append(sol_tab[-1][0])
    return answer

def top_right_hard():
    table, amount_of_lines = gen_file()  # Excel table, amount of lines and values in lines
    corner_N, corner_L = random.randint(5, amount_of_lines - 5), random.randint(5, amount_of_lines - 5)
    len_N, len_L = random.randint(2, 4), random.randint(2, 4)
    gen_borders('TR',corner_N, corner_L,len_N, len_L)
    correct_answer = top_right_hard_solution(table, amount_of_lines, corner_N, corner_L, len_N, len_L)
    start(amount_of_lines)
    print(
        'Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.')
    print(
        'Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из правой верхней клетки в левую нижнюю.')
    print(
        'В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.')
    print(
        'Исходные данные представляют собой электронную таблицу размером {}*{}, каждая ячейка которой соответствует клетке квадрата.'.format(
            amount_of_lines, amount_of_lines))
    example()
    print('Для указанных входных данных ответом должна быть пара чисел 35 и 15.')
    check_answer(correct_answer)

