import random as r

all_symbols = ('˄', '˅', '⟶', '≡', '¬')
list_of_letters_1 = ('x', 'y', 'z')
list_of_letters_2 = ('a', 'b', 'c', 'd')


def swap_positions(massif_answer: list, usable_vars: list):
    len_line = len(massif_answer) - 1
    amount_swaps = r.randint(2, len_line)

    for i in range(amount_swaps):
        row_1, row_2 = r.randint(0, len_line), r.randint(0, len_line)
        while row_1 == row_2:
            row_1, row_2 = r.randint(0, len_line), r.randint(0, len_line)
        massif_answer[row_1], massif_answer[row_2] = massif_answer[row_2], massif_answer[row_1]

    for i in range(amount_swaps):
        c_1, c_2 = r.randint(0, len(massif_answer) - 1), r.randint(0, len(massif_answer) - 1)
        while c_1 == c_2:
            c_1, c_2 = r.randint(0, len(massif_answer) - 1), r.randint(0, len(massif_answer) - 1)
        for k in range(len(massif_answer)):
            massif_answer[k][c_1], massif_answer[k][c_2] = massif_answer[k][c_2], massif_answer[k][c_1]
            usable_vars[c_1], usable_vars[c_2] = usable_vars[c_2], usable_vars[c_1]

    return massif_answer, usable_vars


def adding_bracket(problem: str):
    c_s = 0
    return_problem = ''
    asd = problem.replace('˄', ' ˄ ')
    asd = asd.replace('˅', ' ˅ ')
    asd = asd.replace('⟶', ' ⟶ ')
    asd = asd.replace('≡', ' ≡ ')
    asd = asd.split(' ')
    for i in range(len(asd)):
        if asd[i] in all_symbols and c_s % 2 == 0:
            c_s += 1
            return_problem += '( ' + asd[i - 1] + ' ' + asd[i] + ' ' + asd[i + 1] + ' )'

        elif asd[i] in all_symbols:
            c_s += 1
            return_problem += ' ' + asd[i] + ' '

        elif (i == (len(asd) - 1)) and c_s % 2 == 0:
            return_problem += ' ' + asd[i]

    return return_problem


def checking_string(problem_string: str):
    return_string = ''
    for i in range(len(problem_string)):
        if problem_string[i] == '¬':
            add_symbol = r.choice(all_symbols)
            while add_symbol == '¬':
                add_symbol = r.choice(all_symbols)
            return_string += add_symbol
        return_string += problem_string[i]

    return return_string


def replacing_a_character_with_an_argument(first_value: int, argument: str, second_value: int):
    if argument == '˄':
        return int(first_value and second_value)
    elif argument == '˅':
        return int(first_value or second_value)
    elif argument == '⟶':
        return int(first_value <= second_value)
    else:
        return int(first_value == second_value)


def generate_string(amount_var: int, usable_variables: tuple):
    amount_symbols = r.randint(amount_var + 1, 10)
    usable_symbols = [r.choice(all_symbols) for _ in range(amount_symbols)]
    string_problem = ''
    for i in range(len(usable_symbols)):
        var = r.choice(usable_variables)
        if i != len(usable_symbols) - 1:
            string_problem += var + usable_symbols[i]
        else:
            string_problem += var
    return string_problem


def checking_for_all_var_uses(problem_string: str, usable_variables: tuple):
    usable_variables_duplicate = list(usable_variables)
    for i in problem_string:
        if i in usable_variables_duplicate:
            usable_variables_duplicate.remove(i)
    if len(usable_variables_duplicate) != 0:
        return False
    return True


def check_for_repetition(problem: str):
    string = ''
    flag = False
    need_to_add = False
    for i in problem:
        if i == ')':
            flag = True
            need_to_add = False
        elif i == '(':
            flag = False
            need_to_add = True
        if flag:
            massif = string.split(' ')
            if (massif[1] == massif[3]) or ('¬' + massif[1] == massif[3]) or ('¬' + massif[3] == massif[1]):
                return False
            string = ''
            flag = False
        elif not flag and need_to_add:
            string += i
    return True


def problem_gen():
    while True:
        amount_var = r.randint(3, 4)

        if amount_var == 3:
            string_problem = generate_string(amount_var, list_of_letters_1)
            string_correctness = checking_for_all_var_uses(string_problem, list_of_letters_1)
            usable_vars = list(list_of_letters_1)

        else:
            string_problem = generate_string(amount_var, list_of_letters_2)
            string_correctness = checking_for_all_var_uses(string_problem, list_of_letters_2)
            usable_vars = list(list_of_letters_2)

        if string_correctness:
            string_problem = checking_string(string_problem)
        else:
            continue

        string_problem_with_bracket = adding_bracket(string_problem)
        if not check_for_repetition(string_problem_with_bracket):
            continue

        if amount_var == 4:
            massif = solution_4(string_problem_with_bracket)
        else:
            massif = solution_3(string_problem_with_bracket)
        questions = ['?'] * amount_var

        if isinstance(massif, list):
            massif, answer = swap_positions(massif, usable_vars)
            print(f'Логическая функция F задается выражением {string_problem_with_bracket}\n'
                  f'Ниже приведён фрагмент таблицы истинности функции F\n'
                  f'Определите какому столбцу таблицы истинности функции F\n'
                  f'соответствует каждая из переменных {" ".join(usable_vars)}')

            print(*questions, 'F')
            for i in massif:
                print(*i)
            return answer
        else:
            continue


def solution_3(string_problem: str):
    massif_answer_0 = []
    massif_answer_1 = []
    for x in range(2):
        for y in range(2):
            for z in range(2):
                string = string_problem
                string = string.replace('x', f'{x}')
                string = string.replace('y', f'{y}')
                string = string.replace('z', f'{z}')
                func = replacer_letter_to_number_brackets(string)
                if func == 0:
                    massif_answer_0.append([x, y, z, func])
                else:
                    massif_answer_1.append([x, y, z, func])
    if len(massif_answer_0) == 3:

        return massif_answer_0
    elif len(massif_answer_1) == 3:

        return massif_answer_1

    return False


def solution_4(string_problem: str):
    massif_answer_0 = []
    massif_answer_1 = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    string = string_problem
                    string = string.replace('a', f'{a}')
                    string = string.replace('b', f'{b}')
                    string = string.replace('c', f'{c}')
                    string = string.replace('d', f'{d}')
                    func = replacer_letter_to_number_brackets(string)
                    if func == 0:
                        massif_answer_0.append([a, b, c, d, func])
                    else:
                        massif_answer_1.append([a, b, c, d, func])
    if len(massif_answer_0) == 4:
        return massif_answer_0
    elif len(massif_answer_1) == 4:
        return massif_answer_1

    return False


def trying(val_massif, index_k):
    try:
        val_1 = int(val_massif[index_k - 1])
    except ValueError:
        val_1 = not int(val_massif[index_k - 1][-1])

    try:
        val_2 = int(val_massif[index_k + 1])
    except ValueError:
        val_2 = not int(val_massif[index_k + 1][-1])
    return val_1, val_2


def popper(val_massif, index_k):
    for i in range(2):
        val_massif.pop(index_k)
    return val_massif


def while_main_cycle_in_the_replacer(mark: str, values: list):
    k = values.index(mark)
    v_1, v_2 = trying(values, k)

    value = replacing_a_character_with_an_argument(v_1, mark, v_2)
    values[k - 1] = value
    values = popper(values, k)
    return values


def replacer_letter_to_number_brackets(string_problem: str):
    values = []
    string = ''
    flag = False
    start_adding_items = False
    for i in string_problem:
        if i == ')':
            flag = True
        elif i == '(':
            flag = False
            start_adding_items = False

        if start_adding_items:
            values.append(i)

        if flag:
            massif = string.split(' ')
            try:
                v_1 = int(massif[1])
            except ValueError:
                v_1 = not (int(massif[1][-1]))

            try:
                v_2 = int(massif[3])
            except ValueError:
                v_2 = not (int(massif[3][-1]))
            value = replacing_a_character_with_an_argument(v_1, massif[2], v_2)
            values.append(value)
            string = ''
            flag, start_adding_items = False, True

            del massif, v_1, v_2, value

        if not flag and not start_adding_items:
            string += i

    del flag, start_adding_items, string, i

    values = replacer_letter_to_number_without_brackets(values)
    return values[0]


def replacer_letter_to_number_without_brackets(values: list):
    while ' ' in values:
        values.remove(' ')

    for i in range(len(values)):
        values[i] = str(values[i])

    while '¬' in values:
        k = values.index('¬')
        values[k + 1] = '¬' + values[k + 1]
        values.pop(k)

    while '˄' in values:
        values = while_main_cycle_in_the_replacer('˄', values)

    while '˅' in values:
        values = while_main_cycle_in_the_replacer('˅', values)

    while '⟶' in values:
        values = while_main_cycle_in_the_replacer('⟶', values)

    while '≡' in values:
        values = while_main_cycle_in_the_replacer('≡', values)

    return values


def question():
    c_a = problem_gen()
    return c_a
