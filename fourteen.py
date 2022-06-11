import random


def question():
    x = random.randint(3, 3)
    if x == 1:
        how_many_numbers()
    elif x == 2:
        dominant_number()
    else:
        guess_the_melody()


def gen_num():
    base_of_system = random.randint(2, 9)
    number_we_finding = random.randint(0, base_of_system - 1)
    first_n, seconde_n, third_n = random.randint(2, 9), random.randint(2, 9), random.randint(2, 9)
    first_degree, seconde_degree = random.randint(1000, 5000), random.randint(400, 999)
    f_sign, s_sign = random.choice('+-'), random.choice('+-')
    return base_of_system, number_we_finding, first_n, seconde_n, third_n, first_degree, seconde_degree, f_sign, s_sign


def check_answer(correct_answer):
    print('Введите ответ: ')
    answer = int(input())
    if answer == correct_answer:
        print('Молодец, всё верно!')
    else:
        print('К сожалению, это неправильный ответ')
        print('Хотите узнать правильный ответ? (Да/Нет)')
        y_n = input()
        if y_n == 'Да':
            print(correct_answer)
        elif y_n != 'Нет':
            print('Что? Надеюсь Вы хотели узнать ответ)')
            print('Всё равно покажу, на всякий случай.\n', correct_answer)
    exit()


def conv_number(first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign):
    if f_sign == '+' and s_sign == '+':
        number = first_n ** f_degree + second_n ** s_degree + third_n
    elif f_sign == '+' and s_sign == '-':
        number = first_n ** f_degree + second_n ** s_degree - third_n
    elif f_sign == '-' and s_sign == '+':
        number = first_n ** f_degree - second_n ** s_degree + third_n
    else:
        number = first_n ** f_degree - second_n ** s_degree - third_n
    return number


def how_many_numbers_solution(b_o_s, n_w_f, first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign):
    number = conv_number(first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign)
    amount_number_we_finding = 0
    while number > 0:
        if number % b_o_s == n_w_f:
            amount_number_we_finding += 1
        number //= b_o_s
    return amount_number_we_finding


def how_many_numbers():
    # b_o_s - Base of system
    # n_w_f - Number we finding
    # letters: 'f', 's' and 'n' means first, second, number
    b_o_s, n_w_f, first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign = gen_num()
    correct_answer = how_many_numbers_solution(b_o_s, n_w_f, first_n, second_n, third_n, f_degree, s_degree, f_sign,
                                               s_sign)
    print('Определите сколько {} содержится в {} записи выражение:'.format(n_w_f, b_o_s))
    print('{}^{} {} {}^{} {} {}'.format(first_n, f_degree, f_sign, second_n, s_degree, s_sign, third_n))
    check_answer(correct_answer)


def dominant_number_solution(b_o_s, first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign):
    number = conv_number(first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign)
    a = [0] * b_o_s
    while number > 0:
        p = number % b_o_s
        a[p] += 1
        number //= b_o_s
    return a.index(max(a))


def dominant_number():
    gen_num()
    # b_o_s - Base of system
    # n_w_f - Number we finding
    # letters: 'f', 's' and 'n' means first, second, number
    b_o_s, useless_variable, first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign = gen_num()
    correct_answer = dominant_number_solution(b_o_s, first_n, second_n, third_n, f_degree, s_degree, f_sign, s_sign)
    print('Определите какое число чаще всего встречается в {} записи числа:'.format(b_o_s))
    print('{}^{} {} {}^{} {} {}'.format(first_n, f_degree, f_sign, second_n, s_degree, s_sign, third_n))
    print('Если несколько чисел встречаются с одинаковой частотой, то выберите меньшее из них')
    check_answer(correct_answer)


def guess_the_melody_solution(start_number):
    system = random.randint(2, 9)
    how_its_look = ''
    while start_number > 0:
        how_its_look += str(start_number % system)
        start_number //= system
    how_its_look = how_its_look[::-1]
    return how_its_look,system


def guess_the_melody():
    start_number = random.randint(30, 876)
    end_number, correct_answer = guess_the_melody_solution(start_number)
    print('Число {} записывается как {} в некотрой системе счисления.'.format(start_number, end_number))
    print('Укажите эту систему счисления.')
    check_answer(correct_answer)
