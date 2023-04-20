import random as r
from PIL import Image, ImageDraw, ImageFont
import networkx as nx


def question():
    print('1) Закодируйте слово')
    print('2) Декодируйте последовательность букв')
    print('3) Минимальная длина кодов')
    x = int(input())
    if x == 1:
        c_a = word_to_n_system()
    elif x == 2:
        c_a = decoding_information()
    else:
        c_a = shortest_code()
    return c_a


def word_to_n_system():
    new_system = r.randint(3, 10)
    data_set_words = ['Колобка', 'Миллион', 'Оконный', 'Родовой', 'Турнуть']
    this_word = r.choice(data_set_words).lower()
    to_user_and_prog = list(set(this_word))
    trash = list(set(this_word.upper()))
    print(
        'Для кодирования букв {}, {}, {}, {}, {} решили использовать двоичное представление чисел 0, 1, 2, 3 и 4 соответственно'.format(

            *trash))
    print('(с сохранением одного незначащего нуля в случае одноразрядного представления)')
    print('Закодируйте последовательность букв {} таким способом и результат запишите в {} системе счистления'.format(
        this_word.upper(), new_system))
    correct_answer = solution(to_user_and_prog, this_word, new_system)
    return correct_answer


def solution(to_user_and_prog, this_word, new_system):
    codes = ['00', '01', '10', '11', '100']
    answer = this_word.replace(to_user_and_prog[0], codes[0])
    answer = answer.replace(to_user_and_prog[1], codes[1])
    answer = answer.replace(to_user_and_prog[2], codes[2])
    answer = answer.replace(to_user_and_prog[3], codes[3])
    answer = answer.replace(to_user_and_prog[4], codes[4])
    k = ''
    x = int(answer, new_system)
    while x > 0:
        k += str(x % new_system)
        x //= new_system
    k = k[::-1]
    return int(k)


def fano(amount_values):
    to_return = []
    i = 0
    while i != amount_values:
        st = r.randint(0, amount_values + 4)
        st = bin(st)[2:]
        if len(st) == 1:
            st = '0' + st
        if st not in to_return:
            to_return.append(st)
            i += 1
    return to_return


def decoding_information_generate_image(k):
    letters = [chr(65 + i) for i in range(k)]
    im = Image.new('RGB', size=((k + 1) * 3000 + 1000, 2000), color=(255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.line(xy=[(0, 1000), ((k + 1) * 3000 + 1000, 1000)], width=100, fill=(0, 0, 0))
    value = int((k * 3000) / (k - 1))

    codes = fano(k)
    fonts = 'arial.ttf'
    font = ImageFont.truetype(fonts, 600)
    amount_letters = r.randint(5, 9)
    wtf, answer = '', ''
    for i in range(amount_letters):
        this = r.choice(letters)
        wtf += codes[letters.index(this)]
        answer += this

    for i in range(k):
        draw.multiline_text(xy=(((i + 0.5) * value) - 50, 100), fill=(0, 0, 0), font=font, text=letters[i])

        draw.multiline_text(xy=((i + 0.5) * value, 1500), fill=(0, 0, 0), font=font, text=codes[i], anchor="mm")
    for i in range(1, k):
        draw.line(xy=[(i * value, 0), (i * value, 2000)], width=100, fill=(0, 0, 0))
    im.show()
    return wtf, answer, amount_letters


def decoding_information():
    k = r.randint(4, 7)
    print(
        'Для {} букв латинского алфавита заданы их двоичные коды (для некоторых букв из двух бит, для некоторых – из трех).'.format(
            k))
    print('Эти коды представлены в таблице:')
    wtf, correct_answer, amount_letters = decoding_information_generate_image(k)
    print('Какая последовательность из {} букв закодирована двоичной строкой {}'.format(amount_letters, wtf))
    return correct_answer


def shortest_code_solution(g, their_codes, all_weights):
    answer = 0
    if len(all_weights) == 1:
        answer += (int(all_weights[0]) + 2) * 2
    elif all_weights[0] + 2 < all_weights[1]:
        answer += (int(all_weights[0]) + 2) * 2
    else:
        answer += int(all_weights[0]) + int(all_weights[1]) + 2
    if g == 1:
        for i in their_codes:
            answer += len(i)
    return answer


def shortest_code():
    amount_letters, their_codes, all_weights = shortest_code_true_generation()
    k = r.randint(67, 90 - amount_letters)
    this_letters = [chr(k + i) for i in range(amount_letters)]
    print(
        'Для кодирования некоторой последовательности, состоящей из {} букв,решили использовать неравномерный двоичный код, удовлетворяющий условию Фано.'.format(
            amount_letters + 2))
    for i in range(amount_letters):
        print('{} имеет код {}'.format(this_letters[i], their_codes[i]))

    g = r.randint(1, 2)
    if g == 1:
        print('Какова наименьшая возможная суммарная длина всех кодовых слов?')
    else:
        print('Какова наименьшая возможная суммарная длина двух оставшихся кодовых слов?')
    correct_answer = shortest_code_solution(g, their_codes, all_weights)
    return correct_answer


def shortest_code_true_generation():
    amount_letters, codes = 0, []
    graph_0, graph_1 = 0, 1
    main_flag = True
    while main_flag:
        graph_0 = nx.Graph()
        graph_1 = nx.Graph()
        graph_0.add_node('0')
        graph_1.add_node('1')
        codes = []
        amount_operation = 0
        amount_letters = r.randint(4, 6)
        while len(codes) != amount_letters and amount_operation <= 100:
            if len(codes) < amount_letters - 4:
                smth = r.randint(4, 4)
            elif len(codes) < amount_letters - 2:
                smth = r.randint(3, 4)
            else:
                smth = r.randint(2, 2)
            st = ''
            for i in range(smth):
                st += r.choice('10')
            if st in codes:
                amount_operation += 1
                continue
            else:
                flag = True
                for i in codes:
                    index = i.find(st)
                    if index == 0:
                        flag = False
                        amount_operation += 1

                        break
            if flag:
                amount_operation += 1
                codes.append(st)
                start = st[0]
                if start == '0':
                    i = 0
                    while st[:i] in graph_0: i += 1
                    k = i
                    while st[:k - 1] not in graph_0:
                        if k == 1:
                            graph_0.add_edge(st[0], st[:2])
                        else:
                            graph_0.add_edge(st[:k - 2], st[:k - 1])
                        k -= 1
                    graph_0.add_edge(st, st[:i - 1])
                else:
                    i = 0
                    while st[:i] in graph_1: i += 1
                    k = i
                    while st[:k - 1] not in graph_1:
                        if k == 1:
                            graph_1.add_edge(st[0], st[:2])
                        else:
                            graph_1.add_edge(st[:k - 2], st[:k - 1])
                        k -= 1
                    graph_1.add_edge(st, st[:i - 1])

        ch = 0
        for i in codes:
            if len(i) == 2:
                ch += 1
        if ch == 2:
            main_flag = False

    if '00' in graph_0:
        graph_0.add_edge('00', '0')
    if '01' in graph_0:
        graph_0.add_edge('01', '0')
    if '10' in graph_1:
        graph_1.add_edge('10', '1')
    if '11' in graph_1:
        graph_1.add_edge('11', '1')

    main_graph = nx.union(graph_0, graph_1)
    main_graph.add_edge('start', '0')
    main_graph.add_edge('start', '1')
    all_weights = []
    for i in main_graph:
        if (((i + '1') in main_graph) and ((i + '0') not in main_graph)) or (
                ((i + '0') in main_graph) and ((i + '1') not in main_graph)):
            all_weights.append(len(i))

    return amount_letters, codes, sorted(all_weights)
