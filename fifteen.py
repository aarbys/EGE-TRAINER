import random as r
import numpy as np
import psutil
from collections import Counter
from time import sleep, time


def check_process(process_name) -> bool:
    for proc in psutil.process_iter():
        if process_name == proc.name():
            return True
    return False


def question(rng_seed=897630):
    c_a = None
    print('1) Побитовая конъюнкция')
    print('2) Числовые отрезки')
    print('3) Координатная плоскость')
    type_of_problem = int(input())
    if type_of_problem == 1:
        bc = BitwiseConjunction(rng_seed=rng_seed)
        c_a = bc.print_text_problem()
    elif type_of_problem == 2:
        ns = NumericalSegments()
        c_a = ns.print_to_user()
    elif type_of_problem == 3:
        cp = CoordinatePlane()
        c_a = cp.output_users()
    elif type_of_problem == 4:
        dh = DivisionHere()
        c_a = dh.print_to_user()
    return c_a


def main_cycle_while(values: list, sign: str) -> list:
    if sign in values:
        new_sing = sign.replace(' ', '')
        while sign in values:
            k = values.index(sign)
            values[k - 1] = replace_two_boolean_and_sign_to_boolean(values[k - 1], values[k + 1], new_sing)
            popper(values, k)
    return values


def replace_two_boolean_and_sign_to_boolean(b_1: bool, b_2: bool, sign: " Must be a string") -> bool:
    if sign == '˄':
        return b_1 and b_2
    elif sign == '˅':
        return b_1 or b_2
    elif sign == '⟶':
        return b_1 <= b_2
    else:
        return b_1 == b_2


def popper(values: list, m: int) -> None:
    for i in range(2):
        values.pop(m)


# переписал на внутренние функции
# 897630
class BitwiseConjunction:

    def __init__(self, rng_seed=None):
        if rng_seed is None:
            rng_seed = r.randint(1, 1000000)
        self.rng: np.random.Generator = np.random.default_rng(rng_seed)
        self.usable_signs = (' ˄ ', ' ˅ ', ' ⟶ ')
        self.equality = ('≠', '=')
        self.type_answer = self.rng.integers(0, 2)
        self.number_of_expression_with_bracket_open = self.rng.integers(0, 2)

    def re_init(self, rng_seed=None):
        self.__init__(rng_seed)

    def gen_bitwise_conjunction(self):
        item_1, item_2 = self.rng.choice(range(1, 100), size=2, replace=False)

        assert item_2 != item_1

        items = ['A', str(item_1), str(item_2)]
        massif_with_problem = []
        # massif len == 5
        # 0,2,4 indices of expressions
        # 1 and 3 for signs between expressions

        for i in range(2):
            item = self.rng.choice(items)
            massif_with_problem.append(f'x&{item}{self.rng.choice(self.equality)}0')
            massif_with_problem.append(self.rng.choice(self.usable_signs))
            items.remove(item)

        massif_with_problem.append(f'x&{items[0]}{self.rng.choice(self.equality)}0')
        self.adding_brackets_bites(massif_with_problem)
        return ''.join(massif_with_problem), massif_with_problem

    def solution_bits(self, massif_problem: list):
        for i in range(len(massif_problem)):
            if massif_problem[i] not in self.usable_signs:
                massif_problem[i] = '(' + massif_problem[i] + ')'
        string = ''.join(massif_problem)
        string = string.replace('=', '==')
        string = string.replace('˄', 'and')
        string = string.replace('˅', 'or')
        string = string.replace('⟶', '<=')
        string = string.replace('≠', '!=')
        prob_answer = 0
        for A in range(1000):
            flag = True
            for x in range(1000):
                if bool(eval(string)) != self.type_answer:
                    flag = False
                    break

            if flag:
                prob_answer = max(prob_answer, A)

        if prob_answer == 0 or prob_answer == 999:
            prob_answer = -1

        return prob_answer

    def print_text_problem(self):
        problem, easy_massif_program = self.gen_bitwise_conjunction()
        answer = self.solution_bits(easy_massif_program)
        while answer == -1:
            self.re_init()
            problem, easy_massif_program = self.gen_bitwise_conjunction()
            answer = self.solution_bits(easy_massif_program)

        print('Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.\n'
              'Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4.\n'
              'Для какого наибольшего неотрицательного целого числа А формула:\n'
              f'{problem}')

        if self.type_answer == 1:
            print('тождественно истинна (т.е. принимает значение 1 при любом\n'
                  'неотрицательном целом значении переменной x)?')
        else:
            print('тождественно ложна (т.е. принимает значение 0 при любом\n'
                  'неотрицательном целом значении переменной x)?')

        return answer

    def adding_brackets_bites(self, massif_with_problem: list):
        k = self.number_of_expression_with_bracket_open
        if k == 0:
            massif_with_problem[0] = '(' + massif_with_problem[0]
            massif_with_problem[2] = massif_with_problem[2] + ')'
        else:
            massif_with_problem[2] = '(' + massif_with_problem[2]
            massif_with_problem[4] += ')'


#
#
#
# Бывает странное поведение и не заменяет часто повторяющуюся переменную на ту, которой нет вообще!!!
#
#
# 395783

class NumericalSegments:

    # initialization
    # logging debug
    def __init__(self, rng_seed: int = None):
        if rng_seed is None:
            rng_seed = r.randint(0, 100000000)
        # print('rng_seed =', rng_seed)
        self.rng = np.random.default_rng(seed=rng_seed)
        self.type_answer = self.rng.choice(['наибольшую', 'наименьшую'])
        self.values = self.rng.choice(a=range(1, 190), size=4, replace=False)
        self.values.sort()
        self.usable_signs = (' ˄ ', ' ˅ ', ' ⟶ ', ' ≡ ')
        self.inhere = ('∈', '∉')
        self.amount_expressions = self.rng.integers(3, 5)
        self.items = ['A', 'P', 'Q']
        self.P = [self.values[0], self.values[2]]
        self.Q = [self.values[1], self.values[3]]

        self.P_min = self.P[0] * 10
        self.P_max = self.P[1] * 10
        self.Q_min = self.Q[0] * 10
        self.Q_max = self.Q[1] * 10

    def re_init(self, rng_seed=None):
        self.__init__(rng_seed)

    # block with generating expression
    def code_to_generate_numerical_segments(self) -> "Two lists":
        massif_with_problem = []
        usable_indices = []

        for i in range(self.amount_expressions - 1):
            item = self.rng.choice(self.items)
            usable_indices.append(self.items.index(item))
            massif_with_problem.append(f'x{self.rng.choice(self.inhere)}{item}')

            massif_with_problem.append(self.rng.choice(self.usable_signs))

        item = self.rng.choice(self.items)
        massif_with_problem.append(f'x{self.rng.choice(self.inhere)}{item}')
        usable_indices.append(self.items.index(item))
        return usable_indices, massif_with_problem

    def gen_numerical_segments(self) -> "List ,string, integer":

        usable_indices, massif_with_problem = self.code_to_generate_numerical_segments()

        while len(set(usable_indices)) == 1:
            usable_indices, massif_with_problem = self.code_to_generate_numerical_segments()

        c = Counter()
        for i in range(0, self.amount_expressions):
            c[usable_indices[i]] += 1

        usable_indices = list(set(usable_indices))

        if len(usable_indices) == 2:
            index_not_usable_v = -1
            for i in range(0, 3):
                if i not in usable_indices:
                    index_not_usable_v = i
                    break

            assert index_not_usable_v != -1

            ind_of_maximum_repeated_var, repeated_time = 0, 0

            all_keys = list(c.keys())
            for key in all_keys:
                if repeated_time <= c[key]:
                    repeated_time = c[key]
                    ind_of_maximum_repeated_var = key

            letter_to_change = self.items[ind_of_maximum_repeated_var]

            for i in range(len(massif_with_problem)):
                if letter_to_change in massif_with_problem[i]:
                    massif_with_problem[i] = massif_with_problem[i].replace(letter_to_change,
                                                                            self.items[index_not_usable_v])
                    break

        output_string, open_bracket = self.adding_brackets(massif_with_problem)

        return massif_with_problem, output_string, open_bracket

    def adding_brackets(self, massif_with_problem: list) -> "string and integer":
        open_bracket_index = self.rng.integers(0, self.amount_expressions - 1)  # 0-2

        if open_bracket_index == 0:
            massif_with_problem[0] = '(' + massif_with_problem[0]
            massif_with_problem[2] += ')'

        elif open_bracket_index == 1:
            massif_with_problem[2] = '(' + massif_with_problem[2]
            massif_with_problem[4] += ')'

        else:
            massif_with_problem[4] = '(' + massif_with_problem[4]
            massif_with_problem[6] += ')'
        return ''.join(massif_with_problem), open_bracket_index

    # Output block and start this program
    def print_to_user(self):
        easy_massif, output_string, open_bracket = self.gen_numerical_segments()
        # easy_massif intended to make solution a few faster and easier

        answer = self.solution(easy_massif, open_bracket)
        while answer == 0:
            self.re_init()
            easy_massif, output_string, open_bracket = self.gen_numerical_segments()
            answer = self.solution(easy_massif, open_bracket)

        print('На числовой прямой даны два отрезка:\n'
              f'P = {self.P} и Q = {self.Q}.\n'
              f'Укажите {self.type_answer} возможную длину промежутка A, для которого формула:\n'
              f'{output_string}\n'
              f'тождественно истина.')
        print(answer)
        return answer

    # Block with full solution

    def solution(self, massif: list, open_bracket: int) -> int:
        def return_brackets(item, n_e):
            if n_e == open_bracket:
                item = '(' + item
            elif n_e - 1 == open_bracket:
                item += ')'
            n_e += 1
            return item, n_e

        numb_exp = 0
        for i in range(len(massif)):
            if massif[i] not in self.usable_signs:
                flag_in = True
                if '∉' in massif[i]:
                    flag_in = False
                if 'A' in massif[i]:
                    massif[i] = f'(self.changeable_range(x, a_1, a_2, {flag_in}))'
                elif 'Q' in massif[i]:
                    massif[i] = f'(self.q(x, {flag_in}))'
                else:
                    massif[i] = f'(self.p(x, {flag_in}))'

                massif[i], numb_exp = return_brackets(massif[i], numb_exp)
            else:
                massif[i] = massif[i].replace('⟶', ' <= ')
                massif[i] = massif[i].replace('≡', ' == ')
                massif[i] = massif[i].replace('˄', ' and ')
                massif[i] = massif[i].replace('˅', ' or ')

        string = ''.join(massif)

        def f(x: int, a_1: int, a_2: int) -> int:
            values = []
            numb_of_exp = 1
            for exp in massif:
                if exp in self.usable_signs:
                    values.append(exp)
                elif exp not in self.usable_signs:
                    if numb_of_exp == open_bracket:
                        exp = exp[1:]
                    elif numb_of_exp - 1 == open_bracket:
                        exp = exp[0:-1]
                    values.append(exp)
                    numb_of_exp += 1

            return int(bool(eval(string)))

        indices = [all(f(x, self.P_min, self.Q_min) for x in range(self.P_min, self.Q_max + 1)),
                   all(f(x, self.Q_min, self.P_max) for x in range(self.P_min, self.Q_max + 1)),
                   all(f(x, self.P_max, self.Q_max) for x in range(self.P_min, self.Q_max + 1))]

        if self.type_answer == 'наибольшую':
            m = 0
        else:
            m = 10 ** 5

        if indices[0] == 1:
            m = self.func_min_max(self.P_min, self.Q_min, m)
        if indices[1] == 1:
            m = self.func_min_max(self.Q_min, self.P_max, m)
        if indices[2] == 1:
            m = self.func_min_max(self.P_max, self.Q_max, m)

        if self.type_answer == 'наибольшую':
            if all(indices) == 1:
                return 0
            elif (indices[0] and indices[1]) == 1:
                m = max(m, self.P_max - self.P_min)
            elif (indices[1] and indices[2]) == 1:
                m = max(m, self.Q_max - self.Q_min)

        if m % 10 == 9:
            m += 1
        return m // 10

    def p(self, n, type_answer: str) -> str:
        if not bool(type_answer):
            bool_val = not (self.P_min <= int(n) <= self.P_max)
        else:
            bool_val = (self.P_min <= int(n) <= self.P_max)
        return str(bool_val)

    def q(self, n, type_answer: str) -> str:
        if not bool(type_answer):
            bool_val = not (self.Q_min <= int(n) <= self.Q_max)
        else:
            bool_val = (self.Q_min <= int(n) <= self.Q_max)
        return str(bool_val)

    def func_min_max(self, left_border, right_border, ans):
        if self.type_answer == 'наибольшую':
            return max(ans, right_border - left_border)
        else:
            return min(ans, right_border - left_border)

    @staticmethod
    def changeable_range(n, a_1, a_2, type_answer: str) -> str:
        if not bool(type_answer):
            bool_val = not (int(a_1) <= int(n) <= int(a_2))
        else:
            bool_val = (int(a_1) <= int(n) <= int(a_2))
        return str(bool_val)


# seed 356240
# переписал на внутренние функции
class CoordinatePlane:
    def __init__(self, rng_seed=None):
        if rng_seed is None:
            rng_seed = r.randint(1, 1000000)

        print(f'rng_seed is {rng_seed}')
        self.rng = np.random.default_rng(seed=rng_seed)
        self.number = self.rng.integers(1, 13)
        self.items = (' ≤ ', ' < ')

        # тут для 3кх скобок
        self.numbers_for_3_branches = self.rng.choice(a=range(10, 100), size=2, replace=False)
        self.letters = ['x', 'y']
        self.rng.shuffle(self.letters)
        self.multiplier = self.rng.integers(1, 5)
        self.items_and_ne = (' ≤ ', ' < ', ' ≠ ')

        # тут для 2ух скобочек
        # (2x + 3y > 30) ∨ (x + y ≤ A)
        self.multipliers = [self.multiplier, self.rng.integers(1, 5)]
        self.number_two_brackets = self.number * 10

    def re_init(self, rng_seed=None):
        self.__init__(rng_seed)

    def selecting_problem(self):
        if self.rng.integers(0, 2) == 1:
            string = self.generate_4_branches()  # 16 вариантов всего
            answer = self.branches_4_sol(string)
        elif self.rng.integers(0, 2) == 1:
            string = self.generate_3_branches()  # 6 вариантов
            answer = self.sol_3_branches(string)
        else:
            string = self.generate_2_branches()
            answer = self.sol_2_branches(string)

        # (2x + 3y > 30) ∨ (x + y ≤ A)
        return string, answer

    def output_users(self):
        string, answer = self.selecting_problem()

        while answer == 0:
            self.re_init()  # Задача с новым сидом
            string, answer = self.selecting_problem()

        print('Для какого наибольшего целого числа А формула')
        print(string)
        print('тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных переменных?')
        print(f'Answer is {answer}')
        return answer

    # Тут у нас 4 скобочки и 2 главные скобки
    def generate_4_branches(self):
        string = '((x {} {})' \
                 ' → ' \
                 '(x {} A))' \
                 ' ∧ ' \
                 '((y {} A)' \
                 ' → ' \
                 '(y {} {}))'
        signs = [self.rng.choice(self.items),
                 self.number,
                 self.rng.choice(self.items),
                 self.rng.choice(self.items),
                 self.rng.choice(self.items),
                 self.number]
        string = string.format(*signs)
        return string

    def branches_4_sol(self, string):

        m = 0
        for A in range(1, self.number ** 2 + 1):
            flag = True
            for x in range(1, self.number ** 2 + 1):
                for y in range(1, self.number ** 2 + 1):
                    string = string.replace('→', '<=')
                    string = string.replace('∧', 'and')
                    string = string.replace('≤', '<=')
                    if eval(string) == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                m = A
            sleep(0.001)
        return m

    # 3 скобки
    def generate_3_branches(self):
        string = '({} + {}*{} {} A)' \
                 ' ∨ ' \
                 '({} > {})' \
                 ' ∨ ' \
                 '({} > {})'
        if self.rng.integers(0, 2) == 1:
            signs = [self.letters[0], self.multiplier, self.letters[1], self.rng.choice(self.items),
                     self.letters[0], self.numbers_for_3_branches[0],
                     self.letters[1], self.numbers_for_3_branches[1]
                     ]
        else:
            signs = [self.letters[0],
                     self.multiplier,
                     self.letters[1],
                     self.rng.choice(self.items_and_ne),
                     self.letters[0],
                     self.numbers_for_3_branches[0],
                     self.letters[1],
                     self.letters[0]
                     ]
        string = string.format(*signs)
        return string

    def sol_3_branches(self, string):
        m = 0
        for A in range(1, max(self.numbers_for_3_branches) * 2 + 1):
            flag = True
            for x in range(1, max(self.numbers_for_3_branches) * 2 + 1):
                for y in range(1, max(self.numbers_for_3_branches) * 2 + 1):
                    string = string.replace('∨', 'or')
                    string = string.replace('≠', '!=')
                    if eval(string) == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                m = max(m, A)
            sleep(0.001)
        return m

    # 2 скобки
    def generate_2_branches(self):
        string = '({} {} {}*{} + {}*{})' \
                 ' ∨ ' \
                 '(x + y {} A)'
        signs = [self.number_two_brackets,
                 self.rng.choice(self.items),
                 self.multipliers[0],
                 self.letters[0],
                 self.multipliers[1],
                 self.letters[1],
                 self.rng.choice(self.items)
                 ]
        string = string.format(*signs)
        return string

    def sol_2_branches(self, string):
        m = 0
        for A in range(1, self.number_two_brackets * 2):
            flag = True
            for x in range(1, self.number_two_brackets * 2):
                for y in range(1, self.number_two_brackets * 2):
                    string = string.replace('∨', 'or')
                    string = string.replace('≤', '<=')

                    if eval(string) == 0:
                        flag = False
                        break

                if not flag:
                    break
            if flag:
                m = A
            sleep(0.001)
        return m


# переписал на внутренние функции
class DivisionHere:
    # Инициализация
    def __init__(self, rng_seed=None):
        if rng_seed is None:
            rng_seed = r.randint(1, 10000000)
        self.rng = np.random.default_rng(rng_seed)
        print(f'rng seed is {rng_seed}')

        self.all_signs = [' ∧ ', ' → ', ' ∨ ']
        self.amount_of_exp = self.rng.integers(3, 5)
        self.numbers_for_exp = []
        for i in range(self.amount_of_exp - (self.rng.integers(0, 2))):
            self.numbers_for_exp.append(str(self.rng.integers(2, 800)))
        while len(self.numbers_for_exp) != self.amount_of_exp:
            self.numbers_for_exp.append('A')

    def re_init(self, rng_seed=None):
        self.__init__(rng_seed)

    # Создание задания
    def generate_problem(self):
        massif_type_n_m = []
        temporary_values = self.numbers_for_exp.copy()
        for i in range(self.amount_of_exp):

            item = self.rng.choice(temporary_values)

            bool_val_for_negative = False

            if self.rng.integers(0, 2) == 1:
                bool_val_for_negative = True

            if self.rng.integers(0, 2) == 1:
                temporary = [item, 'x', bool_val_for_negative]
            else:
                temporary = ['x', item, bool_val_for_negative]
            temporary_values.remove(item)

            massif_type_n_m.append(temporary)

        massif_to_user = []
        for i in massif_type_n_m:
            pattern = f'ДЕЛ({i[0]},{i[1]})'
            if not i[-1]:
                pattern = '¬' + pattern
            massif_to_user.append(pattern)

        string_to_user, indices, symbols = self.adding_some_brackets_and_signs(massif_to_user)
        string_to_user, massif_type_n_m = self.replace_x_to_a(string_to_user, massif_type_n_m)
        return massif_type_n_m, string_to_user, indices, symbols

    def adding_some_brackets_and_signs(self, massif_n_m):
        massif_n_m_copy = massif_n_m.copy()
        amount_brackets = self.rng.integers(1, 3)
        indices_of_start_brackets = []

        if self.amount_of_exp == 3:
            amount_brackets = 1
        if amount_brackets == 1:
            indices_of_start_brackets.append(self.rng.integers(0, len(massif_n_m_copy) - 1))
        else:
            indices_of_start_brackets = [0, 2]

        for index in indices_of_start_brackets:
            massif_n_m_copy[index] = '(' + massif_n_m[index]
            massif_n_m_copy[index + 1] += ')'
        string_to_user = ''
        symbols = []
        for i in range(len(massif_n_m)):
            symbol = self.rng.choice(self.all_signs)
            string_to_user += massif_n_m_copy[i] + symbol
            symbols.append(symbol)
        string_to_user = string_to_user[:-2]
        symbols.pop(-1)

        return string_to_user, indices_of_start_brackets, symbols

    @staticmethod
    def replace_x_to_a(string_to_user, massif_n_m):
        flag_a_or_x = 0
        if 'A' not in string_to_user:
            string_to_user = string_to_user.replace('x', 'A', 1)
            flag_a_or_x = 1
        elif 'x' not in string_to_user:
            string_to_user = string_to_user.replace('A', 'x', 1)
            flag_a_or_x = 2

        for i in range(len(massif_n_m)):
            if flag_a_or_x == 1 and 'x' in massif_n_m[i]:
                massif_n_m[i][massif_n_m[i].index('x')] = 'A'
                break
            elif flag_a_or_x == 2 and 'A' in massif_n_m[i]:
                massif_n_m[i][massif_n_m[i].index('A')] = 'x'
                break

        return string_to_user, massif_n_m

    # Решение
    def solution(self, indices, easy_massif, symbols):

        for i in range(len(symbols)):
            symbols[i] = symbols[i].replace('∨', 'or')
            symbols[i] = symbols[i].replace('∧', 'and')
            symbols[i] = symbols[i].replace('→', '<=')
        massif_str = []
        for i in easy_massif:
            bool_str = str(i[0] + '%' + i[1] + '==0')
            if not i[-1]:
                bool_str = bool_str.replace('==', '!=')
            massif_str.append(bool_str)

        for i in indices:
            massif_str[i] = '(' + massif_str[i]
            massif_str[i + 1] += ')'

        main_string = ''
        for i in range(self.amount_of_exp):
            try:
                main_string += massif_str[i] + symbols[i]
            except IndexError:
                main_string += massif_str[i]
        main_string = '(' + main_string + ')'

        answer = 0
        t = time()
        for A in range(1, 1000):
            flag = True
            for x in range(1, 1000):
                if eval(main_string) == 0:
                    flag = False
                    break
            if flag:
                answer = A

            if time() - t > 5:  # 5 - Время в секундах, выключение после 5 секунд
                # Создание нового сида
                return 0
        return answer

    # Вывод для пользователя
    def print_to_user(self):
        easy_massif, string_to_user, indices, symbols = self.generate_problem()
        answer = self.solution(indices, easy_massif, symbols)

        while answer == 0:
            self.re_init()
            easy_massif, string_to_user, indices, symbols = self.generate_problem()
            answer = self.solution(indices, easy_massif, symbols)

        print('Обозначим через ДЕЛ(n, m) утверждение \n'
              '«натуральное число n делится без остатка на натуральное число m».'
              'Для какого наибольшего натурального числа А формула')
        print(string_to_user,
              '\nтождественно истинна \n'
              '(то есть принимает значение 1 при любом натуральном значении переменной x)?')

        return answer


# НАЧАЛ
if __name__ == '__main__':
    question()

# детерминированность

# до 11 утра или после обеда
