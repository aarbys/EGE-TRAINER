import random


def question():
    type_of_problem = random.randint(1, 2)
    if type_of_problem == 1:
        c_a=gather_then()
    else:
        c_a=less_then()
    return c_a
def gather_then_solution(first, seconde, amount_of_conditions, massif_of_value):
    def check_what_is_it(c, massif_of_value, i):
        if '+' in massif_of_value[i]:
            return c + int(massif_of_value[i][-1])
        elif '*' in massif_of_value[i]:
            return c * int(massif_of_value[i][-1])
        elif 'Сделать четное' in massif_of_value[i]:
            return 2 * c
        else:
            return 2 * c + 1

    if amount_of_conditions == 2:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first > seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde, massif_of_value)

        L = f(first, seconde, massif_of_value)
    elif amount_of_conditions == 3:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first > seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 2), seconde, massif_of_value)

        L = f(first, seconde, massif_of_value)
    elif amount_of_conditions == 4:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first > seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 2), seconde, massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 3), seconde, massif_of_value)

        L = f(first, seconde, massif_of_value)
    return L

def gather_then():
    variants_of_conditions = ['Умножить на', 'Прибавить', 'Сделать нечетное', 'Сделать четное']
    amount_of_conditions = random.randint(2, 4)
    massif_of_value = [0 for i in range(amount_of_conditions)]
    print('У некого исполнителя есть', amount_of_conditions, 'команд:')
    for i in range(amount_of_conditions):
        b = random.randint(2, 7)
        z = random.choice(variants_of_conditions)
        if z == 'Сделать нечетное':
            print(i + 1, ')', z)
            massif_of_value[i] = 'Сделать нечетное'
        elif z == 'Сделать четное':
            print(i + 1, ')', z)
            massif_of_value[i] = 'Сделать четное'
        elif z == 'Прибавить':
            print(i + 1, ')', z + ' ' + str(b))
            massif_of_value[i] = '+ ' + str(b)
        else:
            print(i + 1, ')', z + ' ' + str(b))
            massif_of_value[i] = '*' + str(b)
    first, seconde = random.randint(1, 15), random.randint(40, 79)
    print('Сколько существует программ, которые число', first, 'преобразуют в число', seconde, '?')
    correct_answer = gather_then_solution(first, seconde, amount_of_conditions, massif_of_value)
    return correct_answer

def less_then_solution(first, seconde, amount_of_conditions, massif_of_value):
    def check_what_is_it(c, massif_of_value, i):
        if 'Вычти' in massif_of_value[i]:
            return c - int(massif_of_value[i][-1])
        elif 'Подели на' in massif_of_value[i]:
            return c // int(massif_of_value[i][-1])
    if amount_of_conditions == 2:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first < seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde,massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde,massif_of_value)
        L = f(first,seconde,massif_of_value)
    elif amount_of_conditions == 3:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first < seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde,massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde,massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 2), seconde,massif_of_value)
        L = f(first,seconde,massif_of_value)
    elif amount_of_conditions == 4:
        def f(first, seconde, massif_of_value):
            if first == seconde:
                return 1
            elif first < seconde:
                return 0
            else:
                return f(check_what_is_it(first, massif_of_value, 0), seconde,massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 1), seconde,massif_of_value) + f(
                    check_what_is_it(first, massif_of_value, 2), seconde,massif_of_value)+ f(
                    check_what_is_it(first, massif_of_value, 3), seconde,massif_of_value)
        L = f(first,seconde,massif_of_value)

def less_then():
    variants_of_conditions = ['Подели на', 'Вычти']
    amount_of_conditions = random.randint(2, 4)
    massif_of_value = [0 for i in range(amount_of_conditions)]
    print('У некого исполнителя есть', amount_of_conditions, 'команд:')
    for i in range(amount_of_conditions):
        b = random.randint(2, 7)
        z = random.choice(variants_of_conditions)
        if z == 'Подели на':
            print(i + 1, ')', z+' ' +str(b))
            massif_of_value[i] = 'Подели на' + ' ' + str(b)
        elif z == 'Вычти':
            print(i + 1, ')', z+' ' +str(b))
            massif_of_value[i] = 'Вычти' + ' ' + str(b)
    first, seconde = random.randint(40, 79), random.randint(1, 25)
    print('Сколько существует программ, которые число', first, 'преобразуют в число', seconde, '?')
    correct_answer = less_then_solution(first, seconde, amount_of_conditions, massif_of_value)
    return correct_answer
