import random as r

def question():
	print('Выберите тип задания')
	print('1) Кратность одного из чисел')
	print('2) Кратность произведения')
	print('3) Остатки от деления')
	print('4) Кратность разности')
	type_of_problem = int(input())
	if type_of_problem == 1:
		summ()
	elif type_of_problem == 2:
		multiplying()
	elif type_of_problem == 3:
		mod()
	elif type_of_problem == 4:
		difference()

def check_answer(correct_answers):
	print('Введите ответ: ')
	answer = [int(x) for x in input().split()]
	if answer == correct_answers:
		print('Молодец, всё верно!')
	else:
		print('К сожалению, это неправильный ответ')
		print('Хотите узнать правильный ответ? (Да/Нет)')
		y_n = input()
		if y_n == 'Да':
			print(*correct_answers)
	exit()

def gen_file():
	file = open("17.txt", 'w')
	s = ''
	for i in range(10000):
		s += str(r.randint(100, 10000)) + '\n'
	file.write(s)
	file.close()

def summ():
	gen_file()
	random_divider = r.randint(3, 99)
	number_order = r.randint(1, 2)
	print("В файле содержится последовательность целых чисел.")
	print("Каждое число не превышает 10 000.")
	print("Определите и запишите в ответе сначала количество\n пар элементов последовательности, в которых хотя\n бы одно число делится на {}, затем максимальную из\n сумм элементов таких пар.".format(random_divider))
	if number_order == 1:
		print("В данной задаче под парой подразумевается два идущ-\nих подряд элемента последовательности.")
	elif number_order == 2:
		print("В данной задаче под парой подразумевается два разл-\nичных элемента последовательности.")
	correct_answers = summ_solution(random_divider, number_order)
	check_answer(correct_answers)

def summ_solution(random_divider, number_order):
	with open("17.txt", 'r') as file:
		F = [int(x) for x in file]
	count = MAX = 0
	if number_order == 1:
		for i in range(len(F)-1):
			if F[i] % random_divider == 0 or F[i+1] % random_divider == 0:
				count += 1
				MAX = max(MAX, F[i] + F[i+1])
	elif number_order == 2:
		for i in range(len(F)):
			for j in range(i+1, len(F)):
				if F[i] % random_divider == 0 or F[j] % random_divider == 0:
					count += 1
					MAX = max(MAX, F[i] + F[j])
	return [count, MAX]

def multiplying():
	gen_file()
	random_divider = r.randint(3, 99)
	number_order = r.randint(1, 2)
	print("В файле содержится последовательность целых чисел.")
	print("Каждое число не превышает 10 000.")
	print("Определите и запишите в ответе сначала количество\n пар элементов последовательности, у которых сумма\n нечётна, а произведение делится на {}, затем макс-\nимальную из сумм элементов таких пар.".format(random_divider))
	if number_order == 1:
		print("В данной задаче под парой подразумевается два идущ-\nих подряд элемента последовательности.")
	elif number_order == 2:
		print("В данной задаче под парой подразумевается два разл-\nичных элемента последовательности.")
	correct_answers = multiplying_solution(random_divider, number_order)
	check_answer(correct_answers)

def multiplying_solution(random_divider, number_order):
	with open("17.txt", 'r') as file:
		F = [int(x) for x in file]
	count = MAX = 0
	if number_order == 1:
		for i in range(len(F)-1):
			if (F[i] + F[i+1]) % 2 != 0 and (F[i] * F[i+1]) % random_divider == 0:
				count += 1
				MAX = max(MAX, F[i] + F[i+1])
	elif number_order == 2:
		for i in range(len(F)):
			for j in range(i+1, len(F)):
				if (F[i] + F[j]) % 2 != 0 and (F[i] * F[j]) % random_divider == 0:
					count += 1
					MAX = max(MAX, F[i] + F[j])
	return [count, MAX]

def mod():
	gen_file()
	random_mod_divider = r.randint(101, 199)
	random_num_divider = r.randint(3, 99)
	number_order = r.randint(1, 2)
	print("В файле содержится последовательность целых чисел.")
	print("Каждое число не превышает 10 000.")
	print("Определите и запишите в ответе сначала количество \nпар элементов последовательности, у которых различ-\nные остатки от деления на d = {} и хотя бы одно из\n чисел делится на p = {}, затем максимальную из\n сумм элементов таких пар.".format(random_mod_divider, random_num_divider))
	if number_order == 1:
		print("В данной задаче под парой подразумевается два идущ-\nих подряд элемента последовательности.")
	elif number_order == 2:
		print("В данной задаче под парой подразумевается два разл-\nичных элемента последовательности.")
	correct_answers = mod_solution(random_mod_divider, random_num_divider, number_order)
	check_answer(correct_answers)

def mod_solution(random_mod_divider, random_num_divider, number_order):
	with open("17.txt", 'r') as file:
		F = [int(x) for x in file]
	count = MAX = 0
	if number_order == 1:
		for i in range(len(F)-1):
			if F[i] % random_mod_divider != F[i+1] % random_mod_divider:
				if F[i] % random_num_divider == 0 or F[i+1] % random_num_divider == 0:
					count += 1
					MAX = max(MAX, F[i] + F[i+1])
	elif number_order == 2:
		for i in range(len(F)):
			for j in range(i+1, len(F)):
				if F[i] % random_mod_divider != F[j] % random_mod_divider:
					if F[i] % random_num_divider == 0 or F[j] % random_num_divider == 0:
						count += 1
						MAX = max(MAX, F[i] + F[j])
	return [count, MAX]

def difference():
	gen_file()
	random_divider = r.randint(3, 99)
	random_odd_even = r.randint(1, 2)
	number_order = r.randint(1, 2)
	print("В файле содержится последовательность целых чисел.")
	print("Каждое число не превышает 10 000.")
	if random_odd_even == 1:
		print("Определите и запишите в ответе сначала количество\n пар элементов последовательности, разность которых\n нечётна и хотя бы одно из чисел делится на {}, зат-\nем максимальную из сумм элементов таких пар.".format(random_divider))
	elif random_odd_even == 2:
		print("Определите и запишите в ответе сначала количество\n пар элементов последовательности, разность которых\n чётна и хотя бы одно из чисел делится на {}, затем\n максимальную из сумм элементов таких пар.".format(random_divider))
	if number_order == 1:
		print("В данной задаче под парой подразумевается два идущ-\nих подряд элемента последовательности.")
	elif number_order == 2:
		print("В данной задаче под парой подразумевается два разл-\nичных элемента последовательности.")
	correct_answers = difference_solution(random_divider, random_odd_even, number_order)
	check_answer(correct_answers)

def difference_solution(random_divider, random_odd_even, number_order):
	with open("17.txt", 'r') as file:
		F = [int(x) for x in file]
	count = MAX = 0
	if number_order == 1:
		for i in range(len(F)-1):
			if random_odd_even == 1 and abs(F[i]-F[i+1]) % 2 != 0:
				if F[i] % random_divider == 0 or F[i+1] % random_divider == 0:
					count += 1
					MAX = max(MAX, F[i] + F[i+1])
			elif random_odd_even == 2 and abs(F[i]-F[i+1]) % 2 == 0:
				if F[i] % random_divider == 0 or F[i+1] % random_divider == 0:
					count += 1
					MAX = max(MAX, F[i] + F[i+1])
	elif number_order == 2:
		for i in range(len(F)):
			for j in range(i+1, len(F)):
				if random_odd_even == 1 and abs(F[i]-F[j]) % 2 != 0:
					if F[i] % random_divider == 0 or F[j] % random_divider == 0:
						count += 1
						MAX = max(MAX, F[i] + F[j])
				elif random_odd_even == 2 and abs(F[i]-F[j]) % 2 == 0:
					if F[i] % random_divider == 0 or F[j] % random_divider == 0:
						count += 1
						MAX = max(MAX, F[i] + F[j])
	return [count, MAX]