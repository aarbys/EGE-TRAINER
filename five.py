import random
import random as veins


def question():
    print('1) Движение по координатной плоскости.')
    print('2) Число N -> Число R')
    x = int(input())
    if x == 1:
        if veins.randint(1, 2) == 1:
            mooving_by_xOy()
        else:
            how_many_moves_needs_with_sol()
    elif x == 2:
        if veins.randint(1, 2) == 1:
            n_to_r_both_two_bites()
        elif veins.randint(1, 2) == 1:
            n_to_r_two_random_bites()
        else:
            n_to_r_both_sides()

def check_answer(correct_answer):
    print('Вводите ответ:')
    x = int(input())
    if x == correct_answer:
        print('Поздравляю, верно!')
    else:
        print('Вы не правы(')
        print('Хотите узнать верный ответ? (Да/Нет)')
        y_n = input().lower()
        if y_n == 'да':
            print(correct_answer)
        elif y_n != 'нет':
            print('Что?')
            print('Надеюсь, Вы хотели узнать ответ')
            print(correct_answer)


def mooving_by_xOy_solution(start_coord, all_vectors):
    final_result = start_coord  # Can be another output
    for i in range(len(all_vectors)):
        final_result[0] += all_vectors[i][0]
        final_result[1] += all_vectors[i][1]
    answer = int(final_result[0] ** 2 + final_result[1] ** 2)
    return answer


def mooving_by_xOy():
    print('Исполнитель Чертежник имеет перо, которое можно поднимать, опускать и перемещать.')
    print('При перемещении опущенного пера за ним остается след в виде прямой линии.')
    print('У исполнителя существуют следующие команды:')
    print(
        'Сместиться на вектор (а, b) – исполнитель перемещается в точку, в которую можно попасть из данной, пройдя а единиц по горизонтали и b – по вертикали.')
    print(
        'Запись: Повторить 5[Команда 1 Команда 2] означает, что последовательность команд в квадратных скобках повторяется 5 раз.')
    start_x, start_y = veins.randint(-10, -10), veins.randint(-10, -10)
    start_coord = [start_x, start_y]
    print('Чертежник находится в {}'.format(tuple(start_coord)))
    print('Чертежнику дан для исполнения следующий алгоритм:')
    how_many_move_to_diff = veins.randint(3, 5)
    how_many_move_same = veins.randint(2, 4)
    all_vectors = []
    for i in range(how_many_move_to_diff - 1):
        vector = [veins.randint(-10, 10), veins.randint(-10, 10)]
        all_vectors.append(vector)
        print('Сместиться на вектор {}'.format(tuple(vector)))
    vector = [veins.randint(-10, 10), veins.randint(-10, 10)]
    print('Повторить {}[Сместиться на вектор {}]'.format(how_many_move_same, tuple(vector)))
    vector *= how_many_move_same
    all_vectors.append(vector)
    vector = [veins.randint(-10, 10), veins.randint(-10, 10)]
    print('Сместиться на вектор {}'.format(tuple(vector)))
    all_vectors.append(vector)
    print(
        'На каком расстоянии от начала координат будет находиться исполнитель Чертежник в результате выполнения данного алгоритма?')
    correct_answer = mooving_by_xOy_solution(start_coord, all_vectors)
    check_answer(correct_answer)


def how_many_moves_needs_with_sol():
    print('Исполнитель Робот действует на клетчатой доске.')
    print(
        'Робот передвигается по клеткам доски и может выполнять команды \n1 (вверх), 2 (вниз), 3 (вправо) и 4 (влево),переходя на соседнюю клетку в направлении, указанном в скобках.')
    x = veins.randint(4, 10)
    a = [0, 0, 0, 0]
    prob = '1234'
    string = ''
    for i in range(x):
        k = veins.choice(prob)
        a[int(k) - 1] += 1
        string += k
    print('Робот выполнил программу: {}'.format(string))
    print(
        'Укажите наименьшее возможное число команд, которое необходимо для того, чтобы Робот вернулся в ту же клетку, из которой начал движение.')
    correct_answer = abs(a[0] - a[1]) + abs(a[2] - a[3])
    check_answer(correct_answer)


def special_smth(answer, what_we_will_find):
    if what_we_will_find == 'R':
        ans = int(answer, 2)
        return ans
    else:
        ans = int(answer[:-2], 2)
        return ans


def n_to_r_both_two_bites_solution(what_we_will_find, more_less, this_is_number):
    answer = 0
    while answer == 0 and this_is_number > 0:
        if more_less == ['минимальное', 'превышает']:
            this_is_number += 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[-2:] == '00' and (st[:-2].count('1') % 2 == 0)) or (
                    st[-2:] == '10' and (st[:-2].count('1') % 2 != 0)):
                answer = st
        else:
            this_is_number -= 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[-2:] == '00' and (st[:-2].count('1') % 2 == 0)) or (
                    st[-2:] == '10' and (st[:-2].count('1') % 2 != 0)):
                answer = st
    if answer == 0:
        return 0
    else:
        k = special_smth(answer, what_we_will_find)
        return k


def n_to_r_both_two_bites():
    flag = True
    while flag:
        this_is_number = veins.randint(50, 765)
        what_we_will_find = veins.choice('NR')
        more_less = veins.choice(['минимальное', 'превышает'], ['максимальное', 'меньше'])
        correct_answer = n_to_r_both_two_bites_solution(what_we_will_find, more_less, this_is_number)
        if correct_answer != 0:
            flag = False
    print('На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.')
    print('1) Строится двоичная запись числа N.')
    print('2) К этой записи дописываются справа ещё два разряда по следующему правилу:')
    print(
        'а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). \nНапример, запись 11100 преобразуется в запись 111001;')
    print('б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы цифр на 2.')
    print(
        'Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.')
    print(
        'Укажите {} число {}, которое {} {} и может являться результатом работы алгоритма. В ответе это число запишите в десятичной системе.'.format(
            more_less[0], what_we_will_find, more_less[1], this_is_number))
    check_answer(correct_answer)


def n_to_r_two_random_bites_solution(what_we_will_find, more_less, this_is_number, usable_rest):
    answer = 0
    while answer == 0 and this_is_number > 0:
        if more_less == ['минимальное', 'превышает']:
            this_is_number += 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[-2:] == usable_rest[0] and (int(st[:-2], 2) % 2 == 0)) or (
                    st[-2:] == usable_rest[1] and (int(st[:-2], 2) % 2 != 0)):
                answer = st
        else:
            this_is_number -= 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[-2:] == usable_rest[0] and (int(st[:-2], 2) % 2 == 0)) or (
                    st[-2:] == usable_rest[1] and (int(st[:-2], 2) % 2 != 0)):
                answer = st
    if answer == 0:
        return 0
    else:
        k = special_smth(answer, what_we_will_find)
        return k


def n_to_r_two_random_bites():
    flag = True
    while flag:
        this_is_number = veins.randint(50, 765)
        what_we_will_find = veins.choice('NR')
        smth = [['минимальное', 'превышает'], ['максимальное', 'меньше']]
        more_less = veins.choice(smth)
        probably = ['00', '01', '10', '11']
        usable_rest = []
        for i in range(2):
            asd = veins.choice(probably)
            usable_rest.append(asd)
            probably.remove(asd)

        correct_answer = n_to_r_two_random_bites_solution(what_we_will_find, more_less, this_is_number, usable_rest)
        if correct_answer !=0:
            flag = False

    print('На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.')
    print('1) Строится двоичная запись числа N.')
    print('2) К этой записи дописываются справа ещё два разряда по следующему правилу:')
    print('а) если N чётное, в конец числа (справа) дописывается {}.'.format(usable_rest[0]))
    print('б) если N нечётное, справа дописывается {}.'.format(usable_rest[1]))
    print(
        'Например, двоичная запись 100 числа 4 будет преобразована в 10001, а двоичная запись 111 числа 7 будет преобразована в 11110.')
    print(
        'Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)\nявляется двоичной записью числа R — результата работы данного алгоритма.')
    print(
        'Укажите {} число {}, которое {} {} и может являться результатом работы алгоритма. В ответе это число запишите в десятичной системе.'.format(
            more_less[0], what_we_will_find, more_less[1], this_is_number))
    check_answer(correct_answer)



def n_to_r_both_sides_solution(what_we_will_find, more_less, this_is_number, cht_build, nch_build):
    answer = 0
    while answer == 0 and this_is_number > 0 and this_is_number<1000:
        if more_less == ['минимальное', 'превышает']:
            this_is_number += 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[:2] == cht_build[0] and st[-2:] == cht_build[1]):
                answer = st
            elif (st[:2] == nch_build[0] and st[-2:] == nch_build[1]):
                answer = st
        else:
            this_is_number -= 1
            st = bin(this_is_number)
            st = st[2:]
            if (st[2] != '0' and st[:2] == cht_build[0] and st[-2:] == cht_build[1]):
                answer = st
            elif (st[2] != '0' and st[:2] == nch_build[0] and st[-2:] == nch_build[1]):
                answer = st
    if answer == 0:
        return 0
    else:
        return int(answer, 2)


def n_to_r_both_sides():
    what_we_will_find = 'R'
    flag = True
    while flag:
        this_is_number = veins.randint(50, 765)
        add_left = ['10', '11']
        add_right = ['10', '01', '11', '00']
        smth = [['минимальное', 'превышает'], ['максимальное', 'меньше']]
        this_is_number = veins.randint(50, 765)
        more_less = veins.choice(smth)
        cht_build, nch_build = [], []
        cht_build.append(veins.choice(add_left))
        cht_build.append(veins.choice(add_right))
        k = veins.choice(add_left)
        x = veins.choice(add_right)
        while k in cht_build or x in cht_build:
            if k in x:
                k = veins.choice(add_left)
            else:
                x = veins.choice(add_right)
        nch_build.append(k)
        nch_build.append(x)
        correct_answer = n_to_r_both_sides_solution(what_we_will_find, more_less, this_is_number, cht_build, nch_build)
        if correct_answer != 0 :
            flag = False
    print('На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.')
    print('1) Строится двоичная запись числа N.')
    print('2) К этой записи дописываются справа ещё два разряда по следующему правилу:')
    print('а) если N чётное, в конец числа (справа) дописывается {}.'.format(cht_build[1]))
    print('А слева дописывается {}'.format(cht_build[0]))
    print('б) если N нечётное, справа дописывается {}.'.format(nch_build[1]))
    print('И слева - {}'.format(nch_build[0]))
    print(
        'Например, двоичная запись 100 числа 4 будет преобразована в {}100{}, а двоичная запись 111 числа 7 будет преобразована в {}111{}.'.format(
            cht_build[0], cht_build[1], nch_build[0], nch_build[1]))
    print(
        'Укажите {} число {}, которое {} {} и может являться результатом работы алгоритма. В ответе это число запишите в десятичной системе.'.format(
            more_less[0], what_we_will_find, more_less[1], this_is_number))
    check_answer(correct_answer)
