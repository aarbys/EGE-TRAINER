import random


def question():
    type_of_problem = random.randint(1, 2)
    if type_of_problem == 1:
        return two_recursive_func()
    elif type_of_problem == 2:
        return one_recursive_func()



def two_recursive_func_solution(func_1, func_2, func_f,
                                func_g, multiplier_1_f, multiplier_2_f, multiplier_1_g, multiplier_2_g, component_1_f,
                                component_2_f,
                                component_1_g, component_2_g,what_we_need_found,f_or_g):
    def F(n):
        if n == 1:
            return func_1
        elif n == 2:
            return func_f
        elif n % 2 == 0:
            return multiplier_1_f * G(n - 1) + component_1_f
        elif n % 2 != 0:
            return multiplier_2_f * G(n - 2) + component_2_f

    def G(n):
        if n == 1:
            return func_2
        elif n == 2:
            return func_g
        elif n % 2 == 0:
            return multiplier_1_g * F(n - 2) + component_1_g
        elif n % 2 != 0:
            return multiplier_2_g * F(n - 1) + component_2_g
    if f_or_g == 'F':
        return F(what_we_need_found)
    else:
        return G(what_we_need_found)


def two_recursive_func():
    func_1, func_2 = random.randint(1, 14), random.randint(14, 20)
    func_f, func_g = random.randint(func_1, func_1 + 15), random.randint(func_2, func_2 + 15)
    multiplier_1_f, multiplier_2_f = random.randint(10, 19), random.randint(10, 19)
    component_1_f, component_2_f = random.randint(-10, 10), random.randint(-10, 10)
    multiplier_1_g, multiplier_2_g = random.randint(10, 19), random.randint(10, 19)
    component_1_g, component_2_g = random.randint(-10, 10), random.randint(-10, 10)
    what_we_need_found = random.randint(7, 15)
    f_or_g=random.choice('FG')
    correct_answer = two_recursive_func_solution(func_1, func_2, func_f, func_g, multiplier_1_f, multiplier_2_f,
                                                 multiplier_1_g, multiplier_2_g, component_1_f, component_2_f,
                                                 component_1_g, component_2_g,what_we_need_found,f_or_g)
    print(
        'Алгоритм вычисления значения функций F(n) и G(n),где n – натуральное число, заданы следующими соотношениями:')
    print('F(1) = {}'.format(func_1))
    print('F(2) = {}'.format(func_f))
    print('F(n) = {}*G(n-1)'.format(multiplier_1_f), '+{};   если n - четное'.format(component_1_f))
    print('F(n) = {}*G(n-2)'.format(multiplier_2_f), '+{};   если n - нечетное'.format(component_2_f), '\n')
    print('G(1) = {}'.format(func_1))
    print('G(2) = {}'.format(func_g))
    print('G(n) = {}*F(n-2)'.format(multiplier_1_g), '+{};   если n - четное'.format(component_1_g))
    print('G(n) = {}*F(n-1)'.format(multiplier_2_g), '+{};   если n - нечетное'.format(component_2_g), '\n')
    print('Найдите чему будет равно {}'.format(f_or_g),'({})'.format(what_we_need_found))
    return correct_answer



def one_recursive_func_solution(func_1,divider,remains,first, seconde,random_n):
    def f(n):
        if n == 1:
            return func_1
        elif n%2 == 0:
            return (f(n-1)//divider) + first
        elif n%2!=0:
            return (f(n-2)%remains) - seconde
    return f(random_n)



def one_recursive_func():
    func_1 = random.randint(1,19)
    divider = random.randint(1,9)
    remains = random.randint(1,9)
    first, seconde = random.randint(-10,10),random.randint(-10,10)
    random_n = random.randint(10, 25)
    correct_answer = one_recursive_func_solution(func_1,divider,remains,first, seconde,random_n)
    print('Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:')
    print('F(1) = {}'.format(func_1))
    print('F(n) = F(n-1) // {}'.format(divider), '+{};   если n - четное'.format(first))
    print('F(n) = F(n-2)%{}'.format(remains), '-{};   если n - нечетное'.format(seconde), '\n')
    print('Найдите значение F(n), при n = {}'.format(random_n))
    return correct_answer