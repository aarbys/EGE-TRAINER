import random
import os
import psutil
from time import sleep


# numba
# pypy
# cython


def check_process(process_name):
    for proc in psutil.process_iter():
        if process_name == proc.name():
            return True
    return False


def question():
    print('Выберите тип задания')
    print('1) Мусорный бак')
    print('2) Максимальная последовательность кратная x')
    print('3) Некратная сумма')
    print('4) Буферный массив кратности x')
    print('5) Количество сумм пар чисел не кратных x')
    print('6) Максимальная сумма из X- чисел не кратное Y')
    print('7) НОВИНКА МАГИСТРАЛЬ')
    print('8) НОВИНКА РОБОТ ДОСТАВЩИК')
    type_of_problem = int(input())
    if type_of_problem == 1:
        c_a = m_buck(type_of_problem)
    elif type_of_problem == 2:
        c_a = longest_line(type_of_problem)
    elif type_of_problem == 3:
        c_a = not_multi_sum(type_of_problem)
    elif type_of_problem == 4:
        c_a = buff_massif(type_of_problem)
    elif type_of_problem == 5:
        c_a = a_pair_of_numbers(type_of_problem)
    elif type_of_problem == 7:
        c_a = medical_company(type_of_problem)
    elif type_of_problem == 8:
        c_a = robot_postman(type_of_problem)
    else:
        c_a = max_sum_of_some_values(type_of_problem)
    return c_a


def gen_file(type_of_problem):
    generator_file_name = 'generator.exe'

    type_of_columns = 0
    file = open('conditions.txt', 'w')

    if type_of_problem == 1:
        file.write('0 0 50')

    elif type_of_problem == 2:
        file.write('0 0 999')

    elif type_of_problem == 3 or type_of_problem == 5:
        file.write('0 0 5000')

    elif type_of_problem == 4:
        file.write('0 0 1000')

    elif type_of_problem == 6:
        type_of_columns = random.randint(2, 3)
        file.write(f'0 {type_of_columns} 1000')

    elif type_of_problem == 7:
        file.write('1 0 0')

    elif type_of_problem == 8:
        file.write('2 0 0')

    file.close()
    # long launch c++ generator
    assert not check_process(generator_file_name)
    os.startfile(generator_file_name)

    while check_process(generator_file_name):
        sleep(0.01)

    return type_of_columns


def m_buck_solution():
    correct_answers = [0, 0]
    for k in range(2):
        if k == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n = int(f.readline())
        a = [int(i) for i in f]
        price = [0] * n
        for i in range(1, n):
            price[0] += min(i, n - i) * a[i]
        cen = n // 2
        minus = sum(a[:cen])
        plus = sum(a[cen + n % 2:])
        for i in range(1, n):
            plus = plus + a[i - 1] - a[(cen + n % 2) % n]
            minus = minus - a[i - 1] + a[cen]
            price[i] = price[i - 1] + plus - minus
            cen = (cen + 1) % n
        correct_answers[k] = price.index(min(price)) + 1
        f.close()
    return correct_answers


def m_buck(type_of_problem):
    gen_file(type_of_problem)
    correct_answers = m_buck_solution()
    print('На каждом километре кольцевой автодороги с двусторонним движением установлены контейнеры для мусора.')
    print('Длина кольцевой автодороги равна N. Нулевой и N-ый километр в одном месте')
    print('Известно количество мусора, которое накапливается ежедневно в каждом из контейнеров.')
    print('Из каждого пункта мусор вывозит отдельный мусоровоз')
    print('Стоимость доставки мусора равняется весу умноженному на длину пути')
    print('Найдите наименьший номер на километровой дороге,где следует установить мусорозавод.')
    print('Завод надо установить так,чтобы цена доставки была минимальной')
    print('Входные данные. Первая строка - N. В последующих N строках содержится количество мусора.')
    print('В ответ укажите 2 числа, сначала номер для файла А, затем для файла B')
    return correct_answers


def longest_line_solution(number):
    correct_answers = [0, 0]
    for circle in range(2):
        if circle == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n = int(f.readline())
        max_sum = 0
        min_len = n
        s = 0
        ost_sum = [99999 * n] * number
        ost_ind = [-1] * number
        ost_sum[0] = 0
        for i in range(n):
            x = int(f.readline())
            s += x
            p = s % number
            if s - ost_sum[p] > max_sum:
                max_sum = s - ost_sum[p]
                min_len = i - ost_ind[p]
            elif s - ost_sum[p] == max_sum:
                min_len = min(min_len, i - ost_ind[p])
            elif s < ost_sum[p]:
                ost_sum[p] = s
                ost_ind[p] = i
        correct_answers[circle] = min_len
        f.close()
    return correct_answers


def longest_line(type_of_problem):
    number = random.randint(34, 199)
    gen_file(type_of_problem)
    correct_answers = longest_line_solution(number)
    print('На вход программы поступает последовательность из целых положительных чисел. ')
    print('Необходимо выбрать подпоследовательность подряд идущих чисел.')
    print('Сумма подпоследовательности должна быть максимальной и делилась на', number, ',а также найти её длину. ')
    print('Если таких подпоследовательностей несколько, выбрать такую, у которой длина меньше.')
    return correct_answers


def not_multi_sum_solution():
    correct_answer = [0, 0]
    for circle in range(2):
        if circle == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n = int((f.readline()))
        ch = nch = ch2 = nch2 = 0
        for i in range(n):
            x = int(f.readline())
            if x % 2 != 0:
                if x > nch2:
                    if nch < x:
                        nch2 = nch
                        nch = x
                    else:
                        nch2 = x
            else:
                if x > ch2:
                    if x > ch:
                        ch2 = ch
                        ch = x
                    else:
                        ch2 = x
        correct_answer[circle] = max(nch2 + nch, ch2 + ch)
        f.close()
    return correct_answer


def not_multi_sum(type_of_problem):
    gen_file(type_of_problem)
    correct_answer = not_multi_sum_solution()
    print('По каналу связи передаются положительные целые числа, не превышающие 5 000.')
    print(' Числа - результаты измерений, полученных в ходе эксперимента.')
    print('Необходимо выбрать наибольшее число R, удовлетворяющее следующим условиям:')
    print('1)R — сумма двух различных переданных элементов последовательности')
    print('(«различные» означает, что нельзя просто удваивать переданные числа.')
    print(' Суммы различных, но равных по величине элементов допускаются)')
    print(' R — чётное число.')
    print('Если чисел, соответствующих приведённым условиям, нет, считается, что R = 0.')
    print('Программа должна напечатать одно число – наибольшее значение R удовлетворяющее условиям.')
    print('Первая строка файла - N, последующие N строк натуральное число <5000')
    return correct_answer


def only_two_dividers(number):
    a = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            a.append(i)
    if len(a) == 2:
        return [1] + a + [number]
    else:
        return 0


def buff_massif_solution(value, k):
    correct_answers = [0, 0]
    for circle in range(2):
        if circle == 0:
            f = open("27_A.txt")
        else:
            f = open("27_B.txt")
        n = int(f.readline())
        a = [int(f.readline()) for _i in range(value)]
        r, m14, m41, m23, m32 = 0, 0, 0, 0, 0
        for i in range(n - value):
            if a[0] > m41 and a[0] % k[3] == 0:
                m41 = a[0]
            if a[0] > m32 and a[0] % k[2] == 0:
                m32 = a[0]
            if a[0] > m23 and a[0] % k[1] == 0:
                m23 = a[0]
            m14 = max(m14, a[0])
            x = int(f.readline())
            p = x * m41
            if x % k[3] == 0:
                p = max(p, x * m14)
            elif x % k[2] == 0:
                p = max(p, x * m23)
            elif x % k[1] == 0:
                p = max(p, x * m32)
            a.remove(a[0])
            a.append(x)
            r = max(r, p)
        f.close()
        correct_answers[circle] = r
    return correct_answers


def buff_massif(type_of_problem):
    number = random.randint(3, 150)
    k = only_two_dividers(number)
    while k == 0:
        cifra = random.randint(3, 150)
        k = only_two_dividers(cifra)
    value = random.randint(2, 16)
    gen_file(type_of_problem)
    correct_answers = buff_massif_solution(value, k)
    print('Файл содержит последовательность натуральных чисел не превыщающих 1000 ')
    print('Вычислите значение альфа - максимальное кратное', number, 'произвепдение двух показаний.')
    print('Между моментами передачи которых прошло более', value, 'минут')
    print('Входной файл содержит в первой строке значение N - количество показаний. ')
    print('В каждой из  последующих N строк показание')
    return correct_answers


def a_pair_of_numbers_solution(type_of_question, k):
    answers = [0, 0]
    for circle in range(2):
        if circle == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n = int(f.readline())
        kr23, kr32, kr41 = 0, 0, 0
        for i in range(n):
            x = int(f.readline())
            if x % k[3] == 0:
                kr41 += 1
            elif x % k[2] == 0:
                kr32 += 1
            elif x % k[1] == 0:
                kr23 += 1
        if type_of_question == 1:
            r = (((n * (n - 1)) // 2) - (kr23 * kr32 + kr41 * (n - kr41) + kr41 * (kr41 - 1) // 2))
        else:
            r = (kr23 * kr32 + kr41 * (n - kr41) + kr41 * (kr41 - 1) // 2)
        answers[circle] = r
        f.close()
    return answers


def a_pair_of_numbers(type_of_problem):
    gen_file(type_of_problem)
    type_of_question = random.randint(0, 1)
    number = random.randint(3, 150)
    k = only_two_dividers(number)
    while k == 0:
        number = random.randint(3, 150)
        k = only_two_dividers(number)
    correct_answers = a_pair_of_numbers_solution(type_of_question, k)
    if type_of_question == 1:
        print('Найдите количество пар значение которых не кратно', number)
    else:
        print('Найдите количество пар значение которых кратно', number)
    print('Значение должно состоять из произведения двух чисел последовательности')
    print('Файл содержит в себе натуральные числа не более 5000')
    print('Во входном файле первая строка - число N, где N - количество значений')
    return correct_answers


def is_prime(value_of_y):
    for i in range(2, value_of_y // 2 + 1):
        if value_of_y % i == 0:
            return 0
    return value_of_y


def max_sum_of_some_values_solution(k, type_of_columns):
    answers = [0, 0]
    for circle in range(2):
        if circle == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        amount_columns = int(f.readline())
        s = 0
        m = 1000
        if type_of_columns == 2:
            for i in range(amount_columns):

                line = list(map(int, f.readline().split()))
                s += max(line)
                if min(line) % k != 0:
                    m = min(m, min(line))

        else:
            for i in range(amount_columns):
                line = list(map(int, f.readline().split()))
                line.sort(reverse=True)
                s += line[0]
                if line[2] % k != 0:
                    m = min(m, line[2])
                elif line[1] % k != 0:
                    m = min(m, line[1])

        if s % k == 0 and m % k != 0:
            s = s - m
        elif s % k == 0 and m % k == 0:
            s = -1
        answers[circle] = s
        f.close()
    return answers


def max_sum_of_some_values(type_of_problem):
    type_of_columns = gen_file(type_of_problem)
    value_of_y = random.randint(3, 150)
    k = is_prime(value_of_y)
    while k == 0:
        value_of_y = random.randint(3, 150)
        k = is_prime(value_of_y)
    correct_answer = max_sum_of_some_values_solution(k, type_of_columns)
    print('Паша очень любит заниматься математикой. ')
    print('Сначала он записывает к себе в тетрадку число n, а потом n раз записывает по', type_of_columns, ' числа. ')
    print(
        'После этого выбирает по одному числу из каждой строки с учётом того, \n'
        'что сумма выбранных им чисел будет максимальной и не делилась бы на',
        value_of_y)
    print('Также Паша НЕ гарантирует, что искомую сумму получить можно. В итоге он говорит нам только результат')
    print('Дан файл с N строками, в каждой последующей N строке', type_of_columns, 'числа')
    print('Числа натуральные, не превыщают 1000')
    print('Если такой суммы нет, ввести -1')
    return correct_answer


def medical_company_solution(NumberOfTubesInABox):
    answer = []
    for bnm in range(2):
        if bnm == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n = int(f.readline())
        prob = []
        places = []
        price = [0] * n
        plus = 0
        minus = 0
        for i in range(n):
            x = f.readline().split()
            places.append(int(x[0]))
            k = (int(x[1]) // NumberOfTubesInABox) + min(1, int(x[1]) % NumberOfTubesInABox)
            prob.append(k)
            if i != 0:
                price[0] += (places[i] - places[0]) * prob[i]
                plus += prob[i]

        for i in range(1, n):
            minus = minus + prob[i - 1]
            r = places[i] - places[i - 1]
            price[i] = price[i - 1] + (r * (minus - plus))
            plus = plus - prob[i]
        x = price.index(min(price))
        answer.append(places[x])
    return answer


def medical_company(type_of_problem):
    number_of_tubes_in_a_box = random.randint(13, 99)

    gen_file(type_of_problem)

    print('У медицинской компании есть N пунктов приёма биоматериалов на анализ.')
    print(
        'Все пункты расположены вдоль автомагистрали и имеют номера,\n '
        'соответствующие расстоянию от нулевой отметки до конкретного пункта.')
    print('Известно количество пробирок, которое ежедневно принимают в каждом из пунктов.')
    print(
        f'Пробирки перевозятв специальных транспортировочных контейнерах вместимостью не более\n '
        f'{number_of_tubes_in_a_box} штук.')
    print('Каждый транспортировочный контейнер упаковывается в пункте приёма и вскрывается только в лаборатории.')
    print('Компания планирует открыть лабораторию в одном из пунктов. ')
    print(
        'Стоимость перевозки биоматериалов равна \n'
        'произведению расстояния от пункта до лаборатории на количество контейнеров с пробирками.')
    print('Общая стоимость перевозки за день равна сумме стоимостей перевозок из каждого пункта в лабораторию.')
    print(
        'Лабораторию расположили в одном из пунктов приёма биоматериалов таким образом,\n'
        ' что общая стоимость доставки биоматериалов из всех пунктов минимальна.')
    print('Определите минимальную общую стоимость доставки биоматериалов из всех пунктов приёма в лабораторию.')
    print('Входные данные:')
    print(
        'Дано два входных файла (файл A и файл B), каждый из которых в первой строке содержит\n'
        ' число N (1 ≤ N ≤ 10 000 000) – количество пунктов приёма биоматериалов.')
    #
    print('В каждой из следующих N строк находится два числа: номер пункта и количество пробирок в этом пункте.')
    print('Пункты перечислены в порядке их расположения вдоль дороги, начиная от нулевой отметки.')
    print('В ответе укажите два числа: сначала значение искомой величины для файла А, затем – для файла B.')
    print('Типовой пример организации данных во входном файле')
    print('6\n1 100\n2 200\n5 4\n7 3\n8 2\n10 190')
    print(
        'При таких исходных данных и вместимости транспортировочного контейнера, '
        'составляющей 96 пробирок,компании выгодно открыть лабораторию в пункте 2.')
    print('В этом случае сумма транспортных затрат составит: 1*2 + 3*1 + 5*1 + 6*1 + 8*2.')

    correct_answer = medical_company_solution(number_of_tubes_in_a_box)
    return correct_answer


def robot_postman_solution(amount):
    answer = []
    for asd in range(2):
        if asd == 0:
            f = open('27_A.txt')
        else:
            f = open('27_B.txt')
        n, s, z = map(int, f.readline().split())
        x = [0] * s
        price = [0] * s
        d = []
        for i in range(1, n):
            a, b = map(int, f.readline().split())
            x[a - 1] = b // amount + min(1, b % amount)
            d.append(a - 1)
        for i in range(z * 2 + 1):
            price[z] += x[i]
        l = 0
        r = z * 2 + 1
        for i in range(z + 1, s):
            price[i] = price[i - 1] + x[r] - x[l]
            l = (l + 1) % s
            r = (r + 1) % s
        price[0] = price[s - 1] + x[r] - x[l]
        l = (l + 1) % s
        r = (r + 1) % s
        for i in range(1, z):
            price[i] = price[i - 1] + x[r] - x[l]
            l = (l + 1) % s
            r = (r + 1) % s
        m = 0
        for i in d:
            m = max(m, price[i])
        answer.append(m)
    return answer


def robot_postman(type_of_problem):
    gen_file(type_of_problem)

    amount = random.randint(1, 100)
    print('На кольцевой автодороге с двусторонним движением находится N многоэтажных жилых домов\n'
          '(не более одного дома на каждом километре дороги). \n'
          'Длина кольцевой автодороги равна K км. \n'
          'Нулевой километр и K-й километр находятся в одной точке. \n'
          'Жители домов ежедневно получают почту. Которую доставляют роботы-почтальоны. \n'
          f'Почта упакована в доставочные пакеты, каждый из которых вмещает не более {amount} кг посылок или писем.\n '
          'Каждый доставочный пакет используется для доставки почты только в один жилой дом, \n'
          'при этом в каждый дом может быть доставлено не более одного пакета с неполной загрузкой. \n'
          'Известно, что заряд аккумулятора робота-почтальона позволяет проходить ему не более M км, \n'
          'заряд аккумулятора для возвращения робота в почтовое отделение не учитывается. \n'
          'Почтовое отделение открыли в одном из домов таким образом, \n'
          'чтобы количество доставляемых пакетов с корреспонденцией было максимальным. \n'
          'В каждом доставочном пакете перевозится почта только для одного дома. \n')
    print('Определите необходимое количество доставочных пакетов в этом почтовом отделении. \n')
    print('Дано два входных файла (файл A и файл B), каждый из которых в первой строке содержит три числа\n'
          ' N, K и M число N (1 ≤ N ≤ 10 000 000, 1 ≤ K ≤ 10 000 000, 1 ≤ M ≤ 10 000 000)\n'
          ' – количество жилых домов, длина кольцевой дороги в километрах и максимальное расстояние,\n'
          ' на которое робот может осуществлять доставку почтовых отправлений. \n'
          'В каждой из следующих N строк находится два числа: номер километра кольцевой автодороги, \n'
          'на котором расположен жилой дом, и вес ежедневной корреспонденции (все числа натуральные, \n'
          'вес писем и посылок для каждого дома не превышает 1000 кг). \n'
          'Числа указаны в порядке расположения домов на автодороге. \n')
    print('В ответе укажите два числа: сначала значение искомой величины для файла А, затем – для файла В. ')
    print('Типовой пример организации данных во входном файле')
    print('5 11 3\n'
          '1 8\n'
          '3 7\n'
          '5 6\n'
          '7 5\n'
          '9 3\n')
    print('При таких исходных данных и вместимости пакета 3 кг \n'
          'максимальное количество пакетов для доставки корреспонденции \n'
          'из оптимального расположения почтового отделения составит: 3+3+2 ')
    correct_answer = robot_postman_solution(amount)
    return correct_answer
