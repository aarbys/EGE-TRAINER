import random as r
import numpy as np
import pandas as pd
from collections import Counter


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


# 258010
class NumericalSegments:

    # initialization
    # logging debug
    def __init__(self, rng_seed: int = None):
        if rng_seed is None:
            rng_seed = r.randint(0, 1000000)
        print('rng_seed =', rng_seed)
        self.rng = np.random.default_rng(seed=rng_seed)
        self.values = self.rng.choice(a=range(1, 190), size=4)
        while len(set(self.values)) != 4:
            self.values = list(self.values)
            self.values.append(self.rng.choice(a=range(1, 190)))
            self.values = np.asarray(self.values)

        self.seed = rng_seed

        self.values = list(set(self.values))
        self.values.sort()

        self.type_answer = self.rng.choice(['наибольшую', 'наименьшую'])
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
        open_bracket_index = self.rng.integers(0, self.amount_expressions - 2)  # 0-2

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
        dictionary = {'Fast cycle': [], 'Slow cycle': [], 'id': []}
        # easy_massif, output_string, open_bracket = self.gen_numerical_segments()
        # answer, answer_1 = self.solution(easy_massif, open_bracket)
        # easy_massif intended to make solution a few faster and easier
        i = 0
        while i != 50:
            easy_massif, output_string, open_bracket = self.gen_numerical_segments()
            answer, answer_1 = self.solution(easy_massif, open_bracket)

            if answer != 0:
                print(f'Now we made cycle №{i}')
                dictionary['Fast cycle'].append(answer)
                dictionary['Slow cycle'].append(answer_1)
                dictionary['id'].append(self.seed)
                i += 1

            self.re_init()

        df = pd.DataFrame(dictionary)
        df.to_excel('test.xlsx', index=False)

        return answer

    # Block with full solution
    # Попробуй потом тут переписать код, выглядит сложновато и много повтора
    def solution(self, massif: list, open_bracket: int):

        def P(n: int, type_answer: str) -> bool:
            if type_answer == "∉":
                bool_val = not (self.P_min <= n <= self.P_max)
            else:
                bool_val = (self.P_min <= n <= self.P_max)
            return bool(bool_val)

        def Q(n: int, type_answer: str) -> bool:
            if type_answer == "∉":
                bool_val = not (self.Q_min <= n <= self.Q_max)
            else:
                bool_val = (self.Q_min <= n <= self.Q_max)
            return bool(bool_val)

        def X(n: int, a_1: int, a_2: int, type_answer: str) -> bool:
            if type_answer == "∉":
                bool_val = not (a_1 <= n <= a_2)
            else:
                bool_val = (a_1 <= n <= a_2)
            return bool(bool_val)

        def f(x: int, a_1: int, a_2: int) -> int:
            values = []
            for exp in massif:
                self.exp_in_self_usable_signs(exp, values)

                us = self.in_exp_sign_in_self_inhere(exp)

                if us is None:
                    continue

                if 'Q' in exp:
                    values.append(Q(x, us))
                elif 'P' in exp:
                    values.append(P(x, us))
                elif 'A' in exp:
                    values.append(X(x, a_1, a_2, us))

            if open_bracket == 0:
                values[0] = replace_two_boolean_and_sign_to_boolean(values[0], values[2], values[1].replace(' ', ''))
                popper(values, 1)
            elif open_bracket == 1:
                values[2] = replace_two_boolean_and_sign_to_boolean(values[2], values[4], values[3].replace(' ', ''))
                popper(values, 3)
            else:
                values[4] = replace_two_boolean_and_sign_to_boolean(values[4], values[6], values[5].replace(' ', ''))
                popper(values, 5)

            values = self.sign_in_sings(values)

            assert len(values) == 1

            return int(values[0])

        if self.type_answer == 'наибольшую':
            answer_1 = 0
        else:
            answer_1 = 10 ** 5

        print('Starting resolving, slow method')
        for a1 in range(self.P_min - 5, self.Q_max + 5):
            for a2 in range(a1 + 1, self.Q_max + 5):
                if all(f(x, a1, a2) for x in range(self.P_min - 5, self.Q_max + 5)):
                    if self.type_answer == 'наибольшую':
                        answer_1 = max(answer_1, a2 - a1)
                    else:
                        answer_1 = min(answer_1, a2 - a1)

        print('Starting resolving, fast method')
        indices = [all(f(x, self.P_min, self.Q_min) for x in range(self.P_min, self.Q_max + 1)),
                   all(f(x, self.Q_min, self.P_max) for x in range(self.P_min, self.Q_max + 1)),
                   all(f(x, self.P_max, self.Q_max) for x in range(self.P_min, self.Q_max + 1))]

        def func_min_max(left_border, right_border, ans):
            if self.type_answer == 'наибольшую':
                return max(ans, right_border - left_border)
            else:
                return min(ans, right_border - left_border)

        if self.type_answer == 'наибольшую':
            m = 0
        else:
            m = 10 ** 5

        if indices[0] == 1:
            m = func_min_max(self.P_min, self.Q_min, m)
        if indices[1] == 1:
            m = func_min_max(self.Q_min, self.P_max, m)
        if indices[2] == 1:
            m = func_min_max(self.P_max, self.Q_max, m)

        if self.type_answer == 'наибольшую':
            if all(indices) == 1:
                return 0, 0
            elif (indices[0] and indices[1]) == 1:
                m = max(m, self.P_max - self.P_min)
            elif (indices[1] and indices[2]) == 1:
                m = max(m, self.Q_max - self.Q_min)

        if m % 10 == 9:
            m += 1
        if answer_1 % 10 == 9:
            answer_1 += 1
        return m // 10, answer_1 // 10

    def exp_in_self_usable_signs(self, exp: str, values: list) -> None:
        if exp in self.usable_signs:
            values.append(exp)

    def in_exp_sign_in_self_inhere(self, exp: str) -> str:
        us = None
        for sign in self.inhere:
            if sign in exp:
                us = sign
                break
        return us

    def sign_in_sings(self, values: list) -> list:
        for sign in self.usable_signs:
            if sign in values:
                values = main_cycle_while(values, sign)
        return values


if __name__ == '__main__':
    print('Start')
    ns = NumericalSegments()
    c_a = ns.print_to_user()
