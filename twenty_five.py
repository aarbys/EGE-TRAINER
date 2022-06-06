import random


def question():
    random_prototype = random.randint(1,3)
    if random_prototype == 1:
        between_some_some()
    elif random_prototype == 2:
        letter_M()
    elif random_prototype == 3:
        mask_of_number()

def check_answer(correct_answer):
    print('Вводите ответ:')
    for i in range(len(correct_answer)):
        x = input().split()
        x = list(map(int, x))
        if correct_answer[i][0] == x[0] and correct_answer[i][1] == x[1]:
            print('Правильно!')
            continue
        else:
            print('Вы не правы, могу предложить Вам ответ, интересует? ( Да/Нет)')
            answer = input()
            if answer == 'Да':
                for j in range(len(correct_answer)):
                    print(*correct_answer[j])
            elif answer != 'Нет':
                print('Что? Надеюсь Вы хотели узнать ответ)')
                print('Всё равно покажу, на всякий случай.')
                for j in range(len(correct_answer)):
                    print(*correct_answer[j])
        break
    exit()

def check_answer_1(correct_answer):
    print('Вводите ответ:')
    for i in range(len(correct_answer)):
        x = int(input())
        if correct_answer[i] == x:
            print('Правильно!')
            continue
        else:
            print('Вы не правы, могу предложить Вам ответ, интересует? ( Да/Нет)')
            answer = input()
            if answer == 'Да':
                for j in range(len(correct_answer)):
                    print(correct_answer[j])
        break

    exit()

def between_some_some_solution(number_one, number_two,amount_dividers):
    answer = []
    for i in range(number_one, number_two + 1):
        a = []
        for j in range(2, i // 2 + 1):
            if i % j == 0 and len(a) <= amount_dividers:
                a.append(j)
            elif len(a) > amount_dividers:
                break
        if len(a) == amount_dividers:
            answer.append(a)
    if len(answer)==0:
        answer=[[-1,-1]]
    return answer

def between_some_some():
    number_one = random.randint(150000, 200000)
    number_two = random.randint(number_one+30, number_one + 65)
    amount_dividers = random.randint(2,7)
    correct_answer = between_some_some_solution(number_one, number_two,amount_dividers)
    print('Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку[',number_one,';',number_two,']')
    print('числа, имеющие ровно',amount_dividers,' различных натуральных делителя, не считая единицы и самого числа')
    print('Для каждого найденного числа запишите эти делители в строку через пробел в порядке возрастания произведения этих двух делителей.')
    print('Делители в строке также должны следовать в порядке возрастания.')
    print('В случае не совпадения Вашего ответа и результата, Вам сразу же будет предложен выбор: Показать ответ или нет.')
    print('Пример для ДВУХ делителей, чтобы Вы понимали, что и как надо указать')
    print('Например, в диапазоне [5;9] ровно два различных натуральных делителя имеют числа 6 и 8, поэтому для этого диапазона вывод на экране должна содержать следующие значения:')
    print('2 3')
    print('2 4')
    print('Если таких чисел нет введите -1 -1')
    check_answer(correct_answer)

def letter_M_solution_1(type_of_letter,amount_M1):
    answer =[]
    k = 0
    a = 100001
    while k!=amount_M1:
        j=[]
        for i in range(2,a//2 +1):
            if a%i==0:
                j.append(i)
        if len(j)>=2:
            M = j[-1]+j[-2]
            if M<10000:
                answer.append(M)
                k+=1
        a+=1
    return answer

def letter_M_solution_2(type_of_letter,amount_M1,amount_M):
    answer =[]
    k = 0
    a = 100001
    while k!=amount_M1:
        M = 1
        j=[]
        for i in range(2,a//2 +1):
            if a%i==0:
                j.append(i)
        if len(j)>=amount_M:
            for zxc in range(amount_M):
                M *= j[zxc]
        if M<10000 and M!=1:
            answer.append(M)
            k+=1
        a+=1
    return answer

def letter_M():
    type_of_letter = random.randint(1,2)
    amount_M1 = random.randint(4, 9)
    if type_of_letter == 1:
        amount_M = random.randint(2, 4)
        correct_answer = letter_M_solution_2(type_of_letter, amount_M1,amount_M)
        print('Пусть M(N)— произведение',amount_M,'наименьших различных натуральных делителей натурального числа N, не считая единицы.')

    else:
        correct_answer = letter_M_solution_1(type_of_letter, amount_M1)
        print('Пусть M(N) — сумма двух наибольших различных натуральных делителей натурального числа N, не считая самого числа.')
    print('Найдите',amount_M1,'наименьших натуральных чисел, превышающих 100 000, для которых M(N) < 10 000')
    print('В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.')
    check_answer_1(correct_answer)

def mask_of_number_solution(first,seconde,third,number):
    answer =[]
    number_is = int(first)*10000+int(seconde) *100 + int(third)
    first_1 = first+'0000'
    for i in range(int(first_1),10**10):
        x = str(i)
        if x[0:5] == first and seconde == x[6] and third == x[-1] and i%number == 0:
            n = [i,i//number]
            answer.append(n)
        elif int(x[0:5]) > int(first):
            break
    if len(answer) == 0:
        answer.append([-1,-1])
    return answer

def mask_of_number():
    first = str(random.randint(10000,15000))
    seconde = str(random.randint(0,9))
    third = str(random.randint(0,9))
    number_is = first+'?'+seconde+'?'+third
    number=random.randint(10,30)
    correct_answer = mask_of_number_solution(first,seconde,third,number)
    print('Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:')
    print('— символ «?» означает ровно одну произвольную цифру;')
    print('— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.')
    print('Например, маске 123*4?5 соответствуют числа 123405 и 12300405.')
    print('Среди натуральных чисел, не превышающих 10^9, найдите все числа, соответствующие маске',number_is,', делящиеся на число',number,'без остатка.')
    print('В ответе запиcывайте через пробел сначала число, а затем соответсвующий результат деления на',number)
    check_answer(correct_answer)

