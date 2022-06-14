import third # есть
import nine # есть
import fourteen # есть
import sixteen # есть
import seventeen # есть
import eighteen # есть
import games # есть
import twenty_two # есть
import twenty_three # есть
import twenty_four # есть
import twenty_five # есть
import twenty_six # есть
import twenty_seven # есть

def start():
    print('Выберите номер задания')
    x = int(input())
    if x == 1:
        one.question()
    elif x == 2:
        two.question()
    elif x == 3: 
        third.question()  # есть
    elif x == 4:
        four.question()
    elif x == 5:
        five.question()
    elif x == 6:
        six.question()
    elif x == 7:
        seven.question()
    elif x == 8:
        eight.question()
    elif x == 9:
        nine.question()  # есть
    elif x == 10:
        ten.question()
    elif x == 11:
        eleven.question()
    elif x == 12:
        twelve.question()
    elif x == 13:
        thirteen.question()
    elif x == 14:
        fourteen.question()  # есть
    elif x == 15:
        fifteen.question()
    elif x == 16:
        sixteen.question()  # есть
    elif x == 17:
        seventeen.question()  # есть
    elif x == 18:
        eighteen.question() # есть
    elif x == 19 or x == 20 or x == 21:
        games.question() # есть
    elif x == 22:
        twenty_two.question() # есть
    elif x == 23:
        twenty_three.question() # есть
    elif x == 24:
        twenty_four.question() # есть
    elif x == 25:
        twenty_five.question() # есть
    elif x == 26:
        twenty_six.question() # есть
    elif x == 27:
        twenty_seven.question() # есть
    else:
        print('Are you sure?')
        start()
