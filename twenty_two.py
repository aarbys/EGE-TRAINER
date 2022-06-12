import sqlite3 as sl
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io

con = sl.connect('twenty_two.db')

q = con.execute("SELECT COUNT(id) from PROBLEMS")
for i in q:
    amount_of_ids = int(*i)


def check_answer(correct_answer, if_miss_write):
    if if_miss_write == correct_answer:
        print('Молодец, всё верно!')
    else:
        print('К сожалению, это неправильный ответ')
        print('Хотите узнать правильный ответ? (Да/Нет)')
        y_n = input()
        if y_n == 'Да':
            print(correct_answer)
        elif y_n != 'Нет':
            print('Что?')
            print('Надеюсь, Вы хотели узнать ответ')
            print(correct_answer)
    exit()


def question():
    q = con.execute("SELECT COUNT(id) from PROBLEMS")
    for i in q:
        amount_of_ids = int(*i)
    x = random.randint(1, amount_of_ids)  # 1,107
    print('Ниже на выбранном Вами языке будет написан алгоритм.')
    print('Прошу заметить, что Вам следует указать полное название языка')
    print('Все доступные языки для задачи будут прописаны в конце условия.')
    with con:
        output = con.execute("SELECT problem_txt from PROBLEMS WHERE id == {}".format(x))
        answer = con.execute("SELECT answer from PROBLEMS WHERE id == {}".format(x))
        for i in answer:
            correct_answer = int(*i)
        for i in output:
            print(*i)

        output_code(correct_answer, x)


def output_code(correct_answer, x):
    while True:
        flag = True
        language = input().lower()
        if language == 'c++':
            language = 'c'
        elif language == 'algorithmic':
            language = 'algorithm'
        prob_lang = ['c', 'python', 'basic', 'algorithm', 'pascal']
        if language in prob_lang:
            print('Ваш код:\n')
            with con:
                output = con.execute("SELECT {} from PROBLEMS WHERE id == {}".format(language, x))
                for i in output:
                    a = str(*i)
                    text = i[0].encode('UTF-8')
                    text = text.decode('UTF-8')
                    im = Image.new('RGB', (200, 100))
                    d = ImageDraw.Draw(im)
                    font_type = ImageFont.truetype("arial.ttf", 119)
                    text_width, text_height = d.textsize(text, font=font_type)
                    im = Image.new('RGB', (text_width + 45, text_height + 45), (255, 255, 255))
                    draw = ImageDraw.Draw(im)
                    d = draw
                    d.text(xy=(2, 2), text=text, fill=(0, 0, 0), font=font_type)
                    im.show()

            if flag:
                while True:
                    print(
                        'Если Вы случайнор указали не тот язык, можете ввести "Change" чтобы поменять его.\nВ слеющей строке введите новый язык')
                    print('Если Вы верно указали язык, то вводите ответ:')
                    if_miss_write = input()

                    try:
                        asnwer = isinstance(int(if_miss_write), int)
                        check_answer(correct_answer, int(if_miss_write))
                    except ValueError:
                        if if_miss_write.lower() == 'change':
                            output_code(correct_answer, x)
                        else:
                            print('Что?')
                            break
        else:
            print('Что? Повторите, пожалуйста:')
            continue


question()
