import random
from functools import lru_cache


def question():
    print('1) 1 куча')
    print('2) 2 кучи')
    type_of_problem = int(input())
    if type_of_problem == 1:
        c_a = one_pile()
    else:
        c_a = two_pile()
    return c_a


def termins_and_questions():
    print('Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.')
    print(
        'Описать стратегию игрока — значит, описать, какой ход он должен сделать в любой ситуации, которая ему может встретиться при различной игре противника.')
    print(
        '19) Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, когда такая ситуация возможна')
    print(
        '20) Найдите два (НАИМЕНЬШИХ) таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:')
    print(' — Петя не может выиграть за один ход;')
    print(' — Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.')
    print('21) Найдите минимальное значение S, при котором одновременно выполняются два условия:')
    print(' — у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;')
    print('— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.')


def what_is_this_a(real_moves, amount_of_moves, a):
    if 'Увеличить в' in real_moves[amount_of_moves]:
        return a * int(real_moves[amount_of_moves][-1])
    else:
        return a + int(real_moves[amount_of_moves][-1])


def correct_answer(all_results):
    c_answer = []
    if 'Ваня1 после неудачного хода' in all_results:
        c_answer.append(all_results.index('Ваня1 после неудачного хода'))
    else:
        return 0
    zxc = 0
    s = ''
    for i in range(2):
        if 'П2' in all_results:
            s += str(all_results.index('П2', zxc))
            zxc = all_results.index('П2') + 1
        else:
            return 0
    c_answer.append(int(s))
    if 'В2' in all_results:
        c_answer.append(all_results.index('В2'))
    else:
        return 0
    return c_answer


def one_pile_solution(real_moves, amount_of_moves, winning_game):
    def moves(S):
        if amount_of_moves == 2:
            return what_is_this_a(real_moves, 0, S), what_is_this_a(real_moves, 1, S)
        else:
            return what_is_this_a(real_moves, 0, S), what_is_this_a(real_moves, 1, S), what_is_this_a(real_moves, 2, S)

    @lru_cache(None)
    def game(S):
        if S >= winning_game:
            return 'E'
        elif any(game(x) == 'E' for x in moves(S)):
            return 'П1'
        elif all(game(x) == 'П1' for x in moves(S)):
            return 'В1'
        elif any(game(x) == 'В1' for x in moves(S)):
            return 'П2'
        elif all(game(x) == 'П1' or game(x) == 'П2' for x in moves(S)):
            return 'В2'
        elif any(game(x) == 'П1' for x in moves(S)):
            return 'Ваня1 после неудачного хода'

    all_results = [0] * winning_game
    for i in range(1, winning_game - 1):
        all_results[i] = (game(i))
    answer = correct_answer(all_results)
    return answer


def one_pile():
    amount_of_moves = random.randint(2, 3)
    probably_moves = ['Увеличить в', 'Добавить']
    real_moves = []
    winning_game = random.randint(70, 140)
    for i in range(amount_of_moves):
        move_change = random.choice(probably_moves)
        if move_change == 'Добавить':
            move_change += ' ' + str(random.randint(1, 6))
        else:
            move_change += ' ' + str(random.randint(2, 4))
        real_moves.append(move_change)
    correct_answer = one_pile_solution(real_moves, amount_of_moves, winning_game)
    while correct_answer == 0:
        amount_of_moves = random.randint(2, 3)
        real_moves = []
        winning_game = random.randint(70, 140)
        for i in range(amount_of_moves):
            move_change = random.choice(probably_moves)
            if move_change == 'Добавить':
                move_change += ' ' + str(random.randint(1, 6))
            else:
                move_change += ' ' + str(random.randint(2, 4))
            real_moves.append(move_change)
        correct_answer = one_pile_solution(real_moves, amount_of_moves, winning_game)
    print('Два игрока, Петя и Ваня, играют в следующую игру. ')
    print('Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя.')
    print('За один ход игрок может:')
    for i in range(amount_of_moves):
        print((real_moves[i]) + ' камня/раза количество камней')
    print('Игра завершается в тот момент, когда количество камней в куче становится не менее {}'.format(winning_game))
    print(
        'Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет {} или больше камней.'.format(
            winning_game))
    print('В начальный момент в куче было S камней; 1 ≤ S ≤ {}.'.format(winning_game - 1))
    termins_and_questions()
    return correct_answer


def two_pile_solution(real_moves, amount_of_moves, first_pile, winning_game):
    def moves(move):
        a, b = move
        if amount_of_moves == 2:
            return (what_is_this_a(real_moves, 0, a), b), (what_is_this_a(real_moves, 1, a), b), (
                a, what_is_this_a(real_moves, 0, b)), (
                       a, what_is_this_a(real_moves, 1, b))
        else:
            return (what_is_this_a(real_moves, 0, a), b), (what_is_this_a(real_moves, 1, a), b), (
                what_is_this_a(real_moves, 2, a), b), (a, what_is_this_a(real_moves, 0, b)), (
                       a, what_is_this_a(real_moves, 1, b)), (a, what_is_this_a(real_moves, 2, b))

    @lru_cache(None)
    def game(move):
        if sum(move) >= winning_game:
            return 'E'
        elif any(game(x) == 'E' for x in moves(move)):
            return 'П1'
        elif all(game(x) == 'П1' for x in moves(move)):
            return 'В1'
        elif any(game(x) == 'В1' for x in moves(move)):
            return 'П2'
        elif all(game(x) == 'П2' or game(x) == 'П1' for x in moves(move)):
            return 'В2'
        elif any(game(x) == 'П1' for x in moves(move)):
            return 'Ваня1 после неудачного хода'

    all_results = [0] * winning_game
    for i in range(1, winning_game - 1):
        move = first_pile, i
        all_results[i] = game(move)

    asnwer = correct_answer(all_results)
    return asnwer


def two_pile():
    amount_of_moves = random.randint(2, 3)
    probably_moves = ['Увеличить в', 'Добавить']
    real_moves = []
    winning_game = random.randint(70, 140)
    first_pile = random.randint(3, 12)
    for i in range(amount_of_moves):
        move_change = random.choice(probably_moves)
        if move_change == 'Добавить':
            move_change += ' ' + str(random.randint(1, 6))
        else:
            move_change += ' ' + str(random.randint(2, 4))
        real_moves.append(move_change)
    correct_answer = two_pile_solution(real_moves, amount_of_moves, first_pile, winning_game)
    while correct_answer == 0:
        amount_of_moves = random.randint(2, 3)
        real_moves = []
        winning_game = random.randint(70, 140)
        for i in range(amount_of_moves):
            move_change = random.choice(probably_moves)
            if move_change == 'Добавить':
                move_change += ' ' + str(random.randint(1, 6))
            else:
                move_change += ' ' + str(random.randint(2, 4))
            real_moves.append(move_change)
        correct_answer = two_pile_solution(real_moves, amount_of_moves, first_pile, winning_game)
    print('Два игрока, Петя и Ваня, играют в следующую игру.')
    print('Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя.')
    print('За один ход игрок может:')
    for i in range(amount_of_moves):
        print((real_moves[i]) + ' камень(ня/ней)/раза количество камней')
    print('Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее {}.'.format(
        winning_game))
    print('Победителем считается игрок, сделавший последний ход')
    print('В начальный момент в первой куче было', first_pile,
          'камней, во второй куче — S камней; 1 ≤ S ≤ {}.'.format(winning_game - 1))
    termins_and_questions()
    return correct_answer
