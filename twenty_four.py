import random as r


def question():
    print('Выберите тип задания')
    print('1) Идущие подряд символы алфавита')
    print('2) Идущие подряд символы, алфавит из трёх букв')
    print('3) Строки различной длины')
    type_of_problem = int(input())
    if type_of_problem == 1:
        c_a=alphabet(type_of_problem)
    elif type_of_problem == 2:
        c_a=alpha3(type_of_problem)
    elif type_of_problem == 3:
        c_a=lines(type_of_problem)
    return c_a



def gen_file(type_of_problem):
    file = open("24.txt", 'w')
    if type_of_problem == 1:
        s = ''
        for i in range(1000000):
            s += chr(r.randint(65, 90))
        file.write(s)
    elif type_of_problem == 2:
        s = ''
        first_symbol = r.randint(65, 87)
        symbols = (chr(first_symbol), chr(first_symbol + 1), chr(first_symbol + 2))
        for i in range(1000000):
            s += r.choice(symbols)
        file.write(s)
    elif type_of_problem == 3:
        length_of_line = r.randint(981, 1020)
        s = ''
        for i in range(1000):
            for j in range(length_of_line):
                s += chr(r.randint(65, 90))
            s += '\n'
        file.write(s)
    file.close()


def alphabet(type_of_problem):
    gen_file(type_of_problem)
    character = chr(r.randint(65, 90))
    print("Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).")
    print("Определите букву, которая чаще всего встречается в файле сразу после буквы {}.".format(character))
    correct_answer = alphabet_solution(character)
    return correct_answer


def alphabet_solution(character):
    with open("24.txt", 'r') as file:
        s = file.readline()
    symbols_count = dict()
    for i in range(len(s) - 1):
        if s[i] == character:
            if s[i + 1] in symbols_count:
                symbols_count[s[i + 1]] += 1
            else:
                symbols_count[s[i + 1]] = 1
    MAX = 0
    char = ''
    for key in symbols_count:
        if MAX < symbols_count[key]:
            MAX = symbols_count[key]
            char = key
    return char


def check_alpha3():
    with open("24.txt", 'r') as file:
        s = file.readline()
    symbols = set()
    for c in s:
        symbols.add(c)
    return list(symbols)


def alpha3(type_of_problem):
    gen_file(type_of_problem)
    symbols = check_alpha3()
    random_type = r.randint(1, 2)
    if random_type == 1:
        print("Текстовый файл состоит не более чем из 10⁶ символов {}, {} и {}.".format(symbols[0], symbols[1],
                                                                                        symbols[2]))
        line = 3 * (symbols[0] + symbols[1] + symbols[2])
        print(
            "Определите максимальную длину цепочки вида {}... (составленной из фрагментов {}, последний фрагмент может быть неполным).".format(
                line, symbols[0] + symbols[1] + symbols[2]))
        correct_answer = alpha3_1_solution(symbols)
        return correct_answer
    elif random_type == 2:
        print("Текстовый файл состоит не более чем из 10⁶ символов {}, {} и {}.".format(symbols[0], symbols[1],
                                                                                        symbols[2]))
        random_symbol = r.choice(symbols)
        print("Определите длину самой длинной последовательности, состоящей из символов {}.".format(random_symbol))
        print("Хотя бы один символ {} находится в последовательности.".format(random_symbol))
        correct_answer = alpha3_2_solution(random_symbol)
        return correct_answer


def alpha3_1_solution(symbols):
    with open("24.txt", 'r') as file:
        s = file.readline()
    MAX = count = 0
    i = 0
    while i < len(s) - 2:
        if s[i] == symbols[0] and s[i + 1] == symbols[1] and s[i + 2] == symbols[2]:
            count += 3
            i += 3
        else:
            MAX = max(MAX, count)
            count = 0
            i += 1
    return str(MAX)


def alpha3_2_solution(random_symbol):
    with open("24.txt", 'r') as file:
        s = file.readline()
    MAX = count = 1
    for c in s:
        if c == random_symbol:
            count += 1
        else:
            MAX = max(MAX, count)
            count = 1
    return str(MAX)


def lines(type_of_problem):
    gen_file(type_of_problem)
    random_type = r.randint(1, 2)
    if random_type == 1:
        print("Текстовый файл содержит строки различной длины.")
        print("Общий объём файла не превышает 1 Мбайт.")
        print("Строки содержат только заглавные буквы латинского алфавита (ABC…Z).")
        random_symbol_1 = chr(r.randint(65, 90))
        random_symbol_2 = chr(r.randint(65, 90))
        while random_symbol_1 == random_symbol_2:
            random_symbol_1 = chr(r.randint(65, 90))
            random_symbol_2 = chr(r.randint(65, 90))
        print("Определите количество строк, в которых буква {} встречается чаще, чем буква {}.".format(random_symbol_1,
                                                                                                       random_symbol_2))
        correct_answer = lines_1_solution(random_symbol_1, random_symbol_2)
        return correct_answer
    elif random_type == 2:
        print("Текстовый файл содержит строки различной длины.")
        print("Общий объём файла не превышает 1 Мбайт.")
        print("Строки содержат только заглавные буквы латинского алфавита (ABC…Z).")
        random_symbol = chr(r.randint(65, 90))
        print(
            "Необходимо найти строку, содержащую наименьшее количество букв {} (если таких строк несколько, надо взять ту, которая находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего.".format(
                random_symbol))
        print("Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.")
        correct_answer = lines_2_solution(random_symbol)
        return correct_answer


def lines_1_solution(random_symbol_1, random_symbol_2):
    with open("24.txt", 'r') as file:
        F = [x for x in file]
    count = 0
    for x in F:
        if x.count(random_symbol_1) > x.count(random_symbol_2):
            count += 1
    return str(count)


def lines_2_solution(random_symbol):
    with open("24.txt", 'r') as file:
        F = [x for x in file]
    string = ''
    MIN = 10 ** 10
    for x in F:
        if x.count(random_symbol) < MIN:
            MIN = x.count(random_symbol)
            string = x
    symbols_count = dict()
    for c in string:
        if c in symbols_count:
            symbols_count[c] += 1
        else:
            symbols_count[c] = 1
    MAX = 0
    char = ''
    for key in symbols_count:
        if symbols_count[key] > MAX:
            MAX = symbols_count[key]
            char = key
    return char
