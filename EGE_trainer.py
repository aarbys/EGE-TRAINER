import third  # есть
import four
import five
import six_1
import nine  # есть
import fourteen  # есть
import sixteen  # есть
import seventeen  # есть
import eighteen  # есть
import games  # есть
import twenty_two  # есть
import twenty_three  # есть
import twenty_four  # есть
import twenty_five  # есть
import twenty_six  # есть
import twenty_seven  # есть


# Need to create new 26 and other


def check_answer(correct_answer, number):
    two_answers = [27, 26, 18, 17]
    more_two = [19, 20, 21, 25]
    if number in two_answers:
        answer = input()
        answer = answer.split()
        try:
            answer[0], answer[1] = int(answer[0]), int(answer[1])
        except IndexError:
            answer = [int(answer[0]), -1000 ** 1001]
        if correct_answer[0] == answer[0] and correct_answer[1] == answer[1]:
            print('Молодец. 2 Балла')
        elif correct_answer[0] == answer[0] or correct_answer[1] == answer[1] or (
                correct_answer[0] == answer[1] and correct_answer[1] == answer[0]):
            print('Почти получилось. 1 балл.')
        else:
            print('Попробуйте в другой раз. 0 баллов')
            print('Хотите узнать правильный ответ? (Да/Нет)')
            new_answer = input().lower()
            if new_answer == 'да':
                print(*correct_answer)
            elif new_answer != 'нет':
                print('Что? Надеюсь Вы не хотели узнать ответ)')
                print('Всё равно покажу, на всякий случай.', *correct_answer)
        exit()
    elif number in more_two:
        asd = input().split()  # User's input
        asd = list(map(int, asd))
        if asd[0] == correct_answer[0] and asd[1] == correct_answer[1]:
            print('Да,Вы верны!')
        else:
            print('Вы не правы(')
            print('Хотите узнать верный ответ? (Да/Нет)')
            y_n = input().lower()  # Variable for answer question upper
            if y_n == 'да':
                print(correct_answer)
            elif y_n != 'нет':
                print('Что?')
                print('Надеюсь, Вы хотели узнать ответ')
                print(*correct_answer)
        exit()
    else:
        if number == 12:
            asd = input()
        else:
            asd = int(input())
        if asd == correct_answer:
            print('Молодец, всё верно!')
        else:
            print('К сожалению, это неправильный ответ')
            print('Хотите узнать правильный ответ? (Да/Нет)')
            y_n = input().lower()
            if y_n == 'да':
                print(correct_answer)
            elif y_n != 'нет':
                print('Что?')
                print('Надеюсь, Вы хотели узнать ответ')
                print(correct_answer)
        exit()

def start():
    print('Выберите номер задания')
    x = int(input())
    if x == 1:
        c_a = one.question()
    elif x == 2:
        c_a = two.question()
    elif x == 3:
        c_a = third.question()  # есть
    elif x == 4:
        c_a = four.question()
    elif x == 5:
        c_a = five.question()
    elif x == 6:
        c_a = six_1.question()
    elif x == 7:
        c_a = seven.question()
    elif x == 8:
        c_a = eight.question()
    elif x == 9:
        c_a = nine.question()  # есть
    elif x == 10:
        c_a = ten.question()
    elif x == 11:
        c_a = eleven.question()
    elif x == 12:
        c_a = twelve.question()
    elif x == 13:
        c_a = thirteen.question()
    elif x == 14:
        c_a = fourteen.question()  # есть
    elif x == 15:
        c_a = fifteen.question()
    elif x == 16:
        c_a = sixteen.question()  # есть
    elif x == 17:
        c_a = seventeen.question()  # есть
    elif x == 18:
        c_a = eighteen.question()  # есть
    elif x == 19 or x == 20 or x == 21:
        c_a = games.question()  # есть
    elif x == 22:
        c_a = twenty_two.question()  # есть
    elif x == 23:
        c_a = twenty_three.question()  # есть
    elif x == 24:
        c_a = twenty_four.question()  # есть
    elif x == 25:
        c_a = twenty_five.question()  # есть
    elif x == 26:
        c_a = twenty_six.question()  # есть
    elif x == 27:
        c_a = twenty_seven.question()  # есть
    else:
        print('Are you sure?')
        start()
    check_answer(c_a, x)