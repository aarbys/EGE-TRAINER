import random


def question():
    print('Выберите тип задания')
    print('1) Системный администратор')
    print('2) Скидки в магазине')
    print('3) Грузы в машину')
    print('4) Закупка деталей')
    print('5) Посадка деревьев')
    type_of_problem = int(input())
    if type_of_problem == 1:
        c_a = sys_admin(type_of_problem)
    elif type_of_problem == 2:
        c_a = discount(type_of_problem)
    elif type_of_problem == 3:
        c_a = truck(type_of_problem)
    elif type_of_problem == 4:
        c_a = buy_details()
    elif type_of_problem == 5:
        c_a = some_trees(type_of_problem)
    return c_a


def gen_file(type_of_problem):
    file = open('26.txt', 'w')
    if type_of_problem == 1:
        s = random.randint(1000, 10000)
        amount = random.randint(800, 1000)
        file.write(str(s) + ' ' + str(amount) + '\n')
        for i in range(amount):
            z = random.randint(1, 100)
            file.write(str(z) + '\n')
    elif type_of_problem == 2:
        n = random.randint(800, 1000)
        file.write(str(n) + '\n')
        for i in range(n):
            z = random.randint(10, 1000)
            file.write(str(z) + '\n')
    elif type_of_problem == 3:
        s = random.randint(9000, 15000)
        amount = random.randint(800, 1000)
        file.write(str(amount) + ' ' + str(s) + '\n')
        for i in range(amount):
            z = random.randint(70, 500)
            file.write(str(z) + '\n')
    elif type_of_problem == 5:
        s = random.randint(90000, 100000)
        file.write(str(s) + '\n')
        for i in range(s):
            amount = random.randint(10000, 100000)
            amount_r = random.randint(90000, 100000)
            file.write(str(amount) + ' ' + str(amount_r) + '\n')
    file.close()


def sys_admin_solution():
    f = open('26.txt')
    k = f.readline().split()
    s = int(k[0])
    n = int(k[1])
    a = [int(i) for i in f]
    a.sort()
    amount_files = 0
    t_sum = 0
    max_file = 0
    for i in range(n):
        if a[i] + t_sum <= s:
            t_sum += a[i]
            amount_files += 1
            max_file = a[i]
        elif (a[i] + t_sum - a[i - 1]) <= s:
            t_sum = (a[i] + t_sum - a[i - 1])
            max_file = a[i]
    answer = [amount_files, max_file]
    f.close()
    return answer


def sys_admin(type_of_problem):
    gen_file(type_of_problem)
    correct_answer = sys_admin_solution()
    print('Системный администратор раз в неделю создаёт архив пользовательских файлов.')
    print('Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов')
    print('Известно, какой объём занимает файл каждого пользователя.')
    print('По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске')
    print('определите максимальное число пользователей, чьи файлы можно сохранить в архиве')
    print('А также максимальный размер имеющегося файла,который может быть сохранён в архиве, ')
    print('при условии, что сохранены файлы максимально возможного числа пользователей')
    print('В первой строке входного файла находятся два числа: S и N')
    print('S - размер свободного места на диске (натуральное число, не превышающее 10 000)')
    print('N — количество пользователей (натуральное число, не превышающее 1000)')
    print('В следующих N строках находятся значения объёмов файлов каждого пользователя')
    print('(все числа натуральные, не превышающие 100), каждое в отдельной строке.')
    print('Запишите в ответе два числа: сначала наибольшее число пользователей, затем максимальный размер файла')
    return correct_answer


def discount_solution(percent, less_then):
    f = open('26.txt')
    n = int(f.readline())
    discount_massif = []
    price = 0
    for i in range(n):
        x = int(f.readline())
        if x <= less_then:
            price += x
        else:
            discount_massif.append(x)
    discount_massif.sort()
    center = len(discount_massif) // 2
    with_discount = discount_massif[:center]
    without_discount = discount_massif[center:]
    price = price + sum(without_discount) + (sum(with_discount) * (1 - (percent / 100)))
    answer = [int(price) + 1, with_discount[-1]]
    f.close()
    return answer


def discount(type_of_problem):
    percent = random.randint(10, 51)
    less_then = random.randint(50, 251)
    gen_file(type_of_problem)
    correct_answer = discount_solution(percent, less_then)
    print('Продавец предоставляет покупателю, делающему большую закупку, скидку по следующим правилам:')
    print('— на каждый второй товар стоимостью больше', less_then, 'рублей предоставляется скидка', str(percent), '%;')
    print('— общая стоимость покупки со скидкой округляется вверх до целого числа рублей;')
    print('— порядок товаров в списке определяет продавец и делает это так, чтобы общая сумма скидки была наименьшей.')
    print(
        'По известной стоимости каждого товара в покупке необходимо определить общую стоимость покупки с учётом скидки')
    print('А также стоимость самого дорогого товара, на который будет предоставлена скидка.')
    print('Входные данные:')
    print('Первая строка входного файла содержит число N — общее количество купленных товаров')
    print('Каждая из следующих N строк содержит одно целое число — стоимость товара в рублях.')
    print(
        'В ответе запишите два целых числа: сначала общую стоимость покупки с учётом скидки, затем стоимость самого дорогого товара, на который будет предоставлена скидка.')
    return correct_answer


def truck_solution(range_weight_less, range_weight_gather):
    f = open('26.txt')
    a = []
    k = f.readline().split()
    n, m = int(k[0]), int(k[1])
    t_weight = 0
    max_weight = 0
    amount = 0
    for i in range(n):
        x = int(f.readline())
        if (x >= range_weight_gather) and (x <= range_weight_less) and x + t_weight <= m:
            t_weight += x
            max_weight = max(max_weight, x)
            amount += 1
        elif (x >= range_weight_gather) and (
                x <= range_weight_less) and x + t_weight - max_weight <= m and x > max_weight:
            t_weight = t_weight + x - max_weight
            max_weight = max(max_weight, x)
        else:
            a.append(x)
    a.sort()
    for i in range(len(a)):
        if a[i] + t_weight <= m:
            t_weight += a[i]
            amount += 1
            max_weight = max(max_weight, a[i])
        elif a[i] + t_weight - a[i - 1] <= m:
            t_weight = a[i] + t_weight - a[i - 1]
            max_weight = max(max_weight, a[i])
    answer = [amount, max_weight]
    f.close()
    return answer


def truck(type_of_problem):
    gen_file(type_of_problem)
    range_weight_gather = random.randint(100, 300)
    range_weight_less = random.randint(range_weight_gather + 2, range_weight_gather + 16)
    correct_answers = truck_solution(range_weight_less, range_weight_gather)
    print(
        'Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена, поэтому перевезти сразу все грузы не удастся.')
    print('Грузы массой от', range_weight_gather, 'до', range_weight_less,
          'грузят в первую очередь, НЕ гарантируется, что все такие грузы поместятся.')
    print('На оставшееся после этого место стараются взять как можно больше грузов.')
    print(
        'Если это можно сделать несколькими способами, выбирают тот способ, при котором самый большой из выбранных грузов имеет наибольшую массу.')
    print(
        'Если и при этом условии возможно несколько вариантов,выбирается тот, при котором наибольшую массу имеет второй по величине груз, и т.д.')
    print('Известны количество грузов, масса каждого из них и грузоподъёмность грузовика.')
    print(
        'Необходимо определить количество и общую массу грузов, которые будут вывезены при погрузке по вышеописанным правилам.')
    print(
        'Первая строка входного файла содержит два целых числа: N — общее количество грузов и M — грузоподъёмность грузовика в кг.')
    print('Каждая из следующих N строк содержит одно целое число — массу груза в кг.')
    print(
        'В ответе запишите два целых числа: сначала максимально возможное количество грузов, затем наибольший возможный груз.')
    return correct_answers


def buy_details_solution_3():
    answer = [0, 0]
    f = open('26.txt')
    str1 = f.readline().split()
    N, M = int(str1[0]), int(str1[1])
    a, b = [], []
    for i in range(N):
        x = f.readline().split()
        x[0] = int(x[0])
        x[1] = int(x[1])
        if x[2] == 'B':
            b.append(x)
        else:
            a.append(x)
    b.sort()
    a.sort()
    tsumma, kolvoa = 0, 0
    for i in range(len(b)):
        if b[i][0] * b[i][1] + tsumma <= M:
            tsumma += b[i][0] * b[i][1]
        elif b[i][0] * b[i][1] + tsumma > M:
            for j in range(b[i][1] - 1, 0, -1):
                if b[i][0] * (b[i][1] - j) + tsumma <= M:
                    tsumma = tsumma + (b[i][0] * (b[i][1] - j))
    for i in range(len(a)):
        if a[i][0] * a[i][1] + tsumma <= M:
            tsumma += a[i][0] * a[i][1]
            kolvoa += a[i][1]
        elif a[i][0] * a[i][1] + tsumma > M:
            for j in range(a[i][1] - 1, 0, -1):
                if a[i][0] * j + tsumma <= M:
                    kolvoa = kolvoa + j
                    tsumma = tsumma + a[i][0] * j
                    break
    answer = [kolvoa, M - tsumma]
    f.close()
    return answer


def buy_details_solution_2():
    answer = [0, 0]
    f = open('26.txt')
    str1 = f.readline().split()
    N, M = int(str1[0]), int(str1[1])
    all_details = []
    for i in range(N):
        x = f.readline().split()
        x[0] = int(x[0])
        all_details.append(x)
    all_details.sort()
    b = []
    end_massif = []
    t_summa, amount_a = 0, 0
    for i in range(N):
        if t_summa + all_details[i][0] <= M:
            t_summa += all_details[i][0]
            if all_details[i][1] == 'B':
                b.append(all_details[i])
                end_massif.append(all_details[i])
            else:
                end_massif.append(all_details[i])
                amount_a += 1
        elif len(b) >= 1 and t_summa + all_details[i][0] - b[-1][0] <= M:
            t_summa = t_summa + all_details[i][0] - b[-1][0]
            k = b[-1]
            b.remove(b[-1])
            if all_details[i][1] == 'B':
                b.append(all_details[i])
                end_massif.remove(k)
                end_massif.append(all_details[i])
            else:
                end_massif.append(all_details[i])
                amount_a += 1
    answer = [amount_a, M - t_summa]
    f.close()
    return answer


def buy_details():
    type_of_question = random.randint(2, 3)
    gen_file_exc(type_of_question)
    if type_of_question == 2:
        correct_answer = buy_details_solution_2()
        print('Предприятие производит закупку изделий A и B, на которую выделена определённая сумма денег.')
        print('У поставщика есть в наличии различные модификации этих изделий по различной цене.')
        print('При покупке необходимо руководствоваться следующими правилами:')
        print('1. Нужно купить как можно больше изделий, независимо от их типа и модификации.')
        print(
            '2. Если можно разными способами купить максимальное количество изделий, нужно выбрать тот способ, при котором будет куплено как можно больше изделий A.')
        print(
            '3.Если можно разными способами купить максимальное количество изделий с одинаковым количеством изделий A, нужно выбрать тот способ, при котором вся покупка будет дешевле.')
        print('Определите, сколько всего будет куплено изделий A и какая сумма останется неиспользованной.')
        print(
            'Первая строка входного файла содержит два целых числа: N — общее количество изделий у поставщика и M — сумма выделенных на закупку денег.')
        print(
            'Каждая из следующих N строк содержит целое число (цена изделия в рублях) и символ (латинская буква A или B), определяющий тип изделия.')
        print('Все данные в строках входного файла отделены одним пробелом.')
        print(
            'В ответе запишите два целых числа: сначала количество закупленных изделий типа A, затем оставшуюся неиспользованной сумму денег.')
    else:
        correct_answer = buy_details_solution_3()
        print(
            'Предприятие производит оптовую закупку некоторых изделий A и B, на которую выделена определённая сумма денег.')
        print('У поставщика есть в наличии партии этих изделий различных модификаций по различной цене.')
        print('На выделенные деньги необходимо приобрести как можно больше изделий B независимо от модификации.')
        print(
            'Если у поставщика закончатся изделия B, то на оставшиеся деньги необходимо приобрести как можно больше изделий A.')
        print(
            'Известны выделенная для закупки сумма, а также количество и цена различных модификаций данных изделий у поставщика.')
        print('Необходимо определить, сколько будет закуплено изделий A и какая сумма останется неиспользованной.')
        print(
            'Первая строка входного файла содержит два целых числа: N — общее количество партий изделий у поставщика и M — сумма выделенных на закупку денег.')
        print(
            'Каждая из следующих N строк описывает одну партию и содержит два целых числа (цена одного изделия и количество изделий в партии) и один символ (латинская буква A или B), определяющий тип изделия.')
        print('Все данные в строках входного файла отделены одним пробелом.')
        print(
            'В ответе запишите два целых числа: сначала количество закупленных изделий типа A, затем оставшуюся неиспользованной сумму денег.')
    return correct_answer


def gen_file_exc(type_of_question):
    file = open('26.txt', 'w')
    s = random.randint(1000, 10000)
    amount = random.randint(800, 1000)
    file.write(str(amount) + ' ' + str(s) + '\n')
    if type_of_question == 1:
        for i in range(amount):
            z = random.randint(30, 150)
            letter = random.choice('AB')
            file.write(str(z) + ' ' + letter + '\n')
    else:
        for i in range(amount):
            z = random.randint(30, 150)
            v = random.randint(1, 13)
            letter = random.choice('AB')
            file.write(str(z) + ' ' + str(v) + ' ' + letter + '\n')


def some_trees_solution(how_many):
    f = open('26.txt')
    N = int(f.readline())
    massif = []
    for i in range(N):
        x = f.readline().split()
        massif.append(list(map(int, x)))
    massif.sort()
    N_row = -1
    N_place = 100001
    for i in range(N - 1):
        if massif[i][0] == massif[i + 1][0] and massif[i + 1][1] - massif[i][1] - 1 == how_many:
            N_row, N_place = massif[i][0], massif[i][1] + 1
    answer = [N_row, N_place]
    f.close()
    if answer == [-1, 100001]:
        answer = [-1, -1]
    return answer


def some_trees(type_of_problem):
    gen_file(type_of_problem)
    how_many = random.randint(10, 35)
    correct_answer = some_trees_solution(how_many)
    print('В лесополосе осуществляется посадка деревьев. Причем саженцы высаживают рядами на одинаковом расстоянии.')
    print('Через какое-то время осуществляется аэросъемка.')
    print('в результате которой определяется, какие саженцы прижились.')
    print('Необходимо определить ряд с максимальным номером, в котором есть подряд ровно', how_many,
          ' не прижившихся саженцев, при условии, что справа и слева от них саженцы прижились.')
    print('В ответе запишите сначала наибольший номер ряда, затем наименьший номер из найденных не прижившихся мест.')
    print(
        'В первой строке входного файла 26.txt находится число N - количество прижившихся саженцев (натуральное число, не превышающее 100 000). ')
    print(
        'Каждая из следующих N строк содержит два натуральных числа, не превышающих 100 000: номер ряда и номер места для прижившегося саженца.')
    print('Если таких рядов нет, то в ответе укажите -1 и -1')
    return correct_answer
