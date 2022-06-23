import random as r
from PIL import Image, ImageDraw, ImageFont
import random as r
 # https://inf-ege.sdamgia.ru/problem?id=7658
 # Надо сделать, пока не поманию как


def question():
    print('1) Закодируйте слово')
    print('2) Декодируйте последовательность букв')
    x = int(input())
    if x == 1:
        word_to_n_system()
    elif x == 2:
        decoding_information()


def check_answer(correct_answer):
    print('Вводите ответ:')
    x = input()
    try:
        x = int(x)
    except ValueError:
        x = x
    if x == correct_answer:
        print('Поздравляю, верно!')
    else:
        print('Вы не правы(')
        print('Хотите узнать верный ответ? (Да/Нет)')
        y_n = input().lower()
        if y_n == 'да':
            print(correct_answer)
        elif y_n != 'нет':
            print('Что?')
            print('Надеюсь, Вы хотели узнать ответ')
            print(correct_answer)


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
    check_answer(correct_answer)


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
    check_answer(correct_answer)

