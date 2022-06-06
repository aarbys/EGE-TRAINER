import twenty_five
import twenty_seven
import twenty_six
import twenty_three
import twenty_four
import games
import sixteen
import seventeen

def start():
    print('Выберите номер задания')
    x = int(input())
    if x == 2:
        two.question()
    elif x == 6:
        six.question()
    elif x == 12:
        twelve.question()
    elif x == 14:
        fourteen.question()
    elif x == 15:
        fifteen.question()
    elif x == 16:
        sixteen.question()
    elif x == 17:
        seventeen.question()
    elif x == 19 or x == 20 or x == 21:
        games.question()
    elif x == 22:
        twenty_two.question()
    elif x == 23:
        twenty_three.question()
    elif x == 24:
        twenty_four.question()
    elif x == 25:
        twenty_five.question()
    elif x == 26:
        twenty_six.question()
    elif x == 27:
        twenty_seven.question()
    else:
        print('Are you sure?')
        start()
