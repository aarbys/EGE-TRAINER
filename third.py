import random
import sqlite3 as sq
import random as r

con = sq.connect('third.db')

def basic_word():
    print('В файле приведён фрагмент базы данных «Продукты» о поставках товаров в магазины районов города. \nБаза данных состоит из трёх таблиц.')
    print('Таблица «Движение товаров» содержит записи о поставках товаров в магазины в течение первой декады июня 2021г., \nа также информацию о проданных товарах.')
    print('Поле Тип операции содержит значение Поступление или Продажа, а в соответствующее поле Количество упаковок, шт. \nзанесена информация о том, сколько упаковок товара поступило в магазин или было продано в течение дня.')
    print('Таблица «Товар» содержит информацию об основных характеристиках каждого товара. ')
    print('Таблица «Магазин» содержит информацию о местонахождении магазинов.')


def solution(ids_name_items, shop, t_o_p: str):  # That's mean Type of problem
    ids_item = list(ids_name_items.keys())
    id_shop = list(shop.values())
    id_shop_correct =[]
    for i in range(len(id_shop)):
        K = id_shop[i]
        for j in K:
            id_shop_correct.append(j)
    id_shop = id_shop_correct
    status_amount = []
    for smtm in id_shop:
        for smth in ids_item:
            sorting = con.execute("SELECT Status, Amount,vendor_code,Price_by_one "
                                  "FROM Movement_of_goods "
                                  "WHERE vendor_code == {} AND Shop_ID == '{}'".format(smth, smtm))
            for v in sorting:
                v = list(v)
                if v[0] == 'Продажа':
                    v[1] = v[1] * (-1)
                status_amount.append(v)
    t_o_p.lower()
    t_o_p = t_o_p.split()
    answer =0
    if t_o_p[0] == 'увеличилось' or t_o_p[0] == 'уменьшилось':
        if t_o_p[1] == 'упаковок':
            answer = 0
            for i in range(len(status_amount)):
                answer += status_amount[i][1]
        elif t_o_p[1] == 'килограмм' or t_o_p[1] == 'литров':
            masses = dict()
            for i in status_amount:
                if i[2] in masses:
                    masses[i[2]].append(i[1])
                else:
                    masses[i[2]] = [i[1]]
            end_sum = 0
            for i in ids_item:
                smth = ids_name_items[i]
                end_sum += sum(masses[i]) * float(smth[1])
            answer = int(end_sum)
        if t_o_p[0] == 'уменьшилось':
            answer = answer *(-1)
    elif t_o_p[0] == 'заработали':
        summ = 0
        for i in status_amount:
            smth = i
            if smth[0] == 'Продажа':
                summ+= (smth[-1]*smth[1])
        summ *= -1
        answer = summ
    elif t_o_p[0] == 'потратили':
        summ = 0
        for i in status_amount:
            smth = i
            if smth[0] == 'Поступление':
                summ+= (smth[-1]*smth[1])
        answer = summ
    return answer


def items():
    # Vendor code same as v_c
    x = r.randint(1, 4)
    amount_of_v_c = 0
    q = con.execute("SELECT COUNT(vendor_code) from Product")
    for i in q: amount_of_v_c = int(*i)
    all_v_c = [int(i) for i in range(1, amount_of_v_c + 1)]
    liter = [int(i) for i in range(1, 13)]
    kilo = [int(i) for i in range(13, amount_of_v_c + 1)]
    kilo.remove(kilo[3])
    usable_v_c = []
    k =r.choice(all_v_c)
    usable_v_c.append(k)
    smth = 'упаковок'
    if k in liter:
        liter.remove(k)
        smth = 'литров'
        for i in range(x - 1):
            k = r.choice(liter)
            usable_v_c.append(k)
    elif k in kilo:
        kilo.remove(k)
        smth = 'килограмм'
        for i in range(x - 1):
            k = r.choice(kilo)
            usable_v_c.append(k)
    dictionary = dict()
    for i in range(len(usable_v_c)):
        get_name = con.execute("SELECT item_name from Product where vendor_code == {}".format(usable_v_c[i]))
        for v in get_name:
            dictionary[usable_v_c[i]] = [str(*v)]
    for i in range(len(usable_v_c)):
        get_name = con.execute("SELECT amount_in_unit from Product where vendor_code == {}".format(usable_v_c[i]))
        for v in get_name:
            dictionary[usable_v_c[i]].append(str(*v))
    return dictionary,smth


def shops():
    x = r.randint(1, 2)  # Choosing how many shops will be using
    prob = ['Первомайский', 'Заречный'] # 'Октябрьский',
    usable_shops = []
    for i in range(x):
        asd = r.choice(prob)
        usable_shops.append(asd)
        prob.remove(asd)
    dictionary = dict()
    for i in range(x):
        get_shop = con.execute("SELECT Shop_ID FROM Shops where area == '{}'".format(usable_shops[i]))
        for v in get_shop:
            smth = str(*v)
            if not (usable_shops[i] in dictionary):
                dictionary[usable_shops[i]] = [smth]
            else:
                dictionary[usable_shops[i]].append(smth)
    return dictionary


def question():
    ids_name_items,prob2 = items()
    shop = shops()
    prob = ['увеличилось', 'уменьшилось']
    prob3 = ['заработали', 'потратили']
    c_of_q_u = ''  # composition of question for user !!!!OUTPUT!!!!
    c_of_q_p = ''  # composition of question for programm
    k = r.randint(1, 2)
    if k == 1:
        f = r.choice(prob)
        c_of_q_u = f + ' количество ' + prob2
        c_of_q_p = f + ' ' + prob2
    else:c_of_q_p = c_of_q_u = r.choice(prob3)

    correct_answer = solution(ids_name_items, shop, c_of_q_p)
    basic_word()

    print('Используя информацию из приведённой базы данных, определите')
    if k == 1:
        print('На сколько {}:'.format(c_of_q_u))
    elif k == 2 and c_of_q_u == 'заработали': print('сколько {} с продажи:'.format(c_of_q_u))
    elif k == 2 and c_of_q_u == 'потратили':print('сколько {} на покупку:'.format(c_of_q_u))
    string = ''
    for i in ids_name_items:
        smth = ids_name_items[i][0]
        string += smth +' и '
    string = string[:-2]
    print(string)
    shop_keys = list(shop.keys())
    what =''
    for i in shop_keys:what+= i +' '
    print('Магазины этих районов:\n {}'.format(what))
    print('В ответ укажите целую часть полученного числа.')
    print('Если получается обратное значение.Укажите отрицательное число.\nПример:')
    print('Вопрос про уменьшее, а количество на самом деле УВЕЛИЧИЛОСЬ => знак меняется')
    return correct_answer
