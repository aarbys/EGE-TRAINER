import pandas as pd
import random as r
from math import trunc
from styleframe import StyleFrame, Styler, utils

def question():
	print("Выберите тип задания:")
	print("1) Температуры воздуха")
	print("2) Различные задания с числами")
	type_of_problem = int(input())
	if type_of_problem == 1:
		temperature(type_of_problem)
	elif type_of_problem == 2:
		numbers(type_of_problem)

def check_answer(correct_answer):
	print("Введите ответ: ")
	answer = int(input())
	if answer == correct_answer:
		print('Молодец, всё верно!')
	else:
		print('К сожалению, это неправильный ответ')
		print('Хотите узнать правильный ответ? (Да/Нет)')
		y_n = input()
		if y_n == 'Да' or y_n == 'y':
			print(correct_answer)
	exit()

def gen_file(type_of_problem, random_condition):
	if type_of_problem == 1:
		table = dict()
		first_column = chr(0x20)
		for i in range(-1, 24):
			if i < 10 and i >= 0:
				table['0{}:00'.format(i)] = []
			elif i == -1:
				table[first_column] = []
			else:
				table['{}:00'.format(i)] = []
		table_keys = list(table.keys())
		for k in table_keys[1:]:
			for i in range(91):
				random_float = r.uniform(5.0, 30.0)
				while random_float == trunc(random_float):
					random_float = r.uniform(10, 30)
				table[k].append(float('{:.1f}'.format(random_float)))
		months = ('04', '05', '06')
		rows = list()
		for m in months:
			if m == '05':
				for i in range(1, 32):
					if i < 10:
						rows.append('0{}/{}/2021'.format(i, m))
					else:
						rows.append('{}/{}/2021'.format(i, m))
			else:
				for i in range(1, 31):
					if i < 10:
						rows.append('0{}/{}/2021'.format(i, m))
					else:
						rows.append('{}/{}/2021'.format(i, m))
		for i in rows:
			table[first_column].append(i)
		df = pd.DataFrame(data=table, columns=table.keys())
		writer = StyleFrame.ExcelWriter('9.xlsx')
		sf = StyleFrame(df)
		sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.yellow, bold=False, font=utils.fonts.calibri, font_size=12, border_type=None))
		sf.apply_column_style(cols_to_style=df.columns, styler_obj=Styler(bold=False, font=utils.fonts.calibri, font_size=12, border_type=utils.borders.default_grid))
		sf.apply_column_style(cols_to_style=[df.columns[0]], styler_obj=Styler(bg_color=utils.colors.yellow, bold=False, font=utils.fonts.calibri, font_size=12, border_type=None))
		sf.set_column_width([df.columns[0]], 12)
		sf.set_column_width(df.columns[1:], 11)
		df_index = list(df.index)[1:]
		sf.set_row_height(df_index, 16.5)
		sf.to_excel(excel_writer=writer)
		writer.save()
	elif type_of_problem == 2:
		table = dict()
		n = number_range = 0
		if random_condition == 'five':
			n = 5
			number_range = 3200
		else:
			n = 3
			number_range = 5000
		for i in range(n):
			table[i] = []
		for keys in table:
			for i in range(number_range):
				table[keys].append(r.randint(1, 100))
		df = pd.DataFrame(data=table)
		df.to_excel('9.xlsx', header=False, index=False)

def temperature(type_of_problem):
	gen_file(type_of_problem, '')
	random_condition = r.choice(['max-mid', 'min-mid', 'count<>=mid', 'count<=max', 'count>=min', 'mid/2<count<max/2', 'mid<count<min*2'])
	random_equality = ''
	print("Откройте файл электронной таблицы, содержащей веще-\nственные числа — результаты ежечасного измерения\n температуры воздуха на протяжении трёх месяцев.")
	if random_condition == 'max-mid':
		print('Найдите разность между максимальным значением темп-\nературы и её средним арифметическим значением.\n В ответе запишите только целую часть получившегося\n числа.')
	elif random_condition == 'min-mid':
		print('Найдите разность между минимальным значением темпе-\nратуры и её средним арифметическим значением. Ответ\n округлите до целого числа.')
	elif random_condition == 'count<>=mid':
		random_equality = r.choice(['>', '<', '='])
		if random_equality == '>':
			print('Сколько раз встречалась температура, выше округлен-\nного до десятых среднего арифметического значения\n всех чисел в таблице?')
		elif random_equality == '<':
			print('Сколько раз встречалась температура, ниже округлен-\nного до десятых среднего арифметического значения\n всех чисел в таблице?')
		elif random_equality == '=':
			print('Сколько раз встречалась температура, которая \nравна округлённому до десятых среднему арифметичес-\nкому значения всех чисел в таблице?')
	elif random_condition == 'count<=max':
		random_equality = r.choice(['=', '<'])
		if random_equality == '=':
			print('Сколько раз встречалась температура, которая равна\n максимальному значению?')
		elif random_equality == '<':
			print('Сколько раз встречалась температура, которая была \nниже половины от максимального значения?')
	elif random_condition == 'count>=min':
		random_equality = r.choice(['=', '>'])
		if random_equality == '=':
			print('Сколько раз встречалась температура, которая равна\n минимальному значению?')
		elif random_equality == '>':
			print('Сколько раз встречалась температура, которая была \nвыше удвоенного минимального значения?')
	elif random_condition == 'mid/2<count<max/2':
		print('Сколько раз встречалась температура, которая была \nвыше половины среднего арифметического значения \nокругленного до десятых, но ниже половины от макси-\nмального значения?')
	elif random_condition == 'mid<count<min*2':
		print('Сколько раз встречалась температура, которая была \nниже среднего арифметического значения округленного\n до десятых, но выше удвоенного минимального значе-\nния?')
	correct_answer = temperature_solution(random_condition, random_equality)
	check_answer(correct_answer)

def temperature_solution(random_condition, random_equality):
	table = pd.read_excel('9.xlsx')
	table_columns = table.columns[1:]
	correct_answer = 0
	if random_condition == 'max-mid':
		MID = MAX = 0
		for key in table_columns:
			for value in table[key]:
				MID += float(value)
				MAX = max(MAX, float(value))
		MID /= 91*24
		correct_answer = abs(MAX - MID)
	elif random_condition == 'min-mid':
		MID = 0; MIN = 10**10
		for key in table_columns:
			for value in table[key]:
				MID += float(value)
				MIN = min(MIN, float(value))
		MID /= 91*24
		correct_answer = abs(MIN - MID)
	elif random_condition == 'count<>=mid':
		MID = 0
		for key in table_columns:
			for value in table[key]:
				MID += float(value)
		MID = float("{:.1f}".format(MID / 91*24))
		count = 0
		if random_equality == '>':
			for key in table_columns:
				for value in table[key]:
					if float(value) > MID: count += 1
		elif random_equality == '<':
			for key in table_columns:
				for value in table[key]:
					if float(value) < MID: count += 1
		elif random_equality == '=':
			for key in table_columns:
				for value in table[key]:
					if float(value) == MID: count += 1
		correct_answer = count
	elif random_condition == 'count<=max':
		count = MAX = 0
		for key in table_columns:
			for value in table[key]:
				MAX = max(MAX, float(value))
		if random_equality == '=':
			for key in table_columns:
				for value in table[key]:
					if float(value) == MAX: count += 1
		elif random_equality == '<':
			for key in table_columns:
				for value in table[key]:
					if float(value) < (MAX / 2): count += 1
		correct_answer = count
	elif random_condition == 'count>=min':
		count = 0; MIN = 10**10
		for key in table_columns:
			for value in table[key]:
				MIN = min(MIN, float(value))
		if random_equality == '=':
			for key in table_columns:
				for value in table[key]:
					if float(value) == MIN: count += 1
		elif random_equality == '>':
			for key in table_columns:
				for value in table[key]:
					if float(value) > (MIN * 2): count += 1
		correct_answer = count
	elif random_condition == 'mid/2<count<max/2':
		count = MAX = MID = 0
		for key in table_columns:
			for value in table[key]:
				MID += float(value)
				MAX = max(MAX, float(value))
		MID = float("{:.1f}".format(MID / 91*24*2))
		for key in table_columns:
			for value in table[key]:
				if MID < float(value) < (MAX / 2): count += 1
		correct_answer = count
	elif random_condition == 'mid<count<min*2':
		count = MID = 0; MIN = 10**10
		for key in table_columns:
			for value in table[key]:
				MID += float(value)
				MIN = min(MIN, float(value))
		MID = float("{:.1f}".format(MID / 91*24))
		for key in table_columns:
			for value in table[key]:
				if (MIN*2) < float(value) < MID: count += 1
		correct_answer = count
	return correct_answer

def numbers(type_of_problem):
	random_condition = r.choice(['jtriangle', 'sharpangle', '90angle', 'obtuseangle', 'box', 'five'])
	gen_file(type_of_problem, random_condition)
	random_equality = ''
	if random_condition == 'jtriangle':
		print('Откройте файл электронной таблицы, содержащей в \nкаждой строке три натуральных числа.')
		print('Выясните, какое количество троек чисел может яв-\nляться сторонами треугольника, то есть удовлетворяет\n неравенству треугольника. В ответе запишите только\n число.')
	elif random_condition == 'sharpangle':
		print('Откройте файл электронной таблицы, содержащей в \nкаждой строке три натуральных числа.')
		print('Определите сколько среди заданных троек чисел таких,\n которые могут быть сторонами остроугольного треугольника.')
	elif random_condition == '90angle':
		print('Откройте файл электронной таблицы, содержащей в \nкаждой строке три натуральных числа.')
		print('Определите, сколько среди заданных троек чисел таких,\n которые могут быть сторонами прямоугольного треугольника.')
	elif random_condition == 'obtuseangle':
		print('Откройте файл электронной таблицы, содержащей в \nкаждой строке три натуральных числа.')
		print('Определите, сколько среди заданных троек чисел таких,\n которые могут быть сторонами тупоугольного треугольника.')
	elif random_condition == 'box':
		random_equality = r.choice(['more', 'less'])
		if random_equality == 'more':
			print('В каждой строке электронной таблицы записаны три \nнатуральных числа, задающих длины трёх взаимно \nперпендикулярных рёбер прямоугольного параллелепи-\nпеда. Определите, сколько в таблице троек, для \nкоторых у заданного ими параллелепипеда можно так \nвыбрать три грани с общей вершиной, что сумма площ-\nадей двух из них будет меньше площади третьей.')
		elif random_equality == 'less':
			print('В каждой строке электронной таблицы записаны три \nнатуральных числа, задающих длины трёх взаимно \nперпендикулярных рёбер прямоугольного параллелепипеда.\n Определите, сколько в таблице троек, для которых \nу заданного ими параллелепипеда для любых трёх \nграней с общей вершиной сумма площадей двух из \nних больше площади третьей.')
	elif random_condition == 'five':
		print('Откройте файл электронной таблицы, содержащей в \nкаждой строке пять натуральных чисел.')
		print('Определите количество строк таблицы, в которых \nквадрат суммы максимального и минимального чисел в\n строке больше суммы квадратов трёх оставшихся.')
	correct_answer = numbers_solution(random_condition, random_equality)
	check_answer(correct_answer)

# gen_file(2, '')

def numbers_solution(random_condition, random_equality):
	table = pd.read_excel('9.xlsx')
	first_column = list(table.columns)
	correct_answer = 0
	if random_condition == 'jtriangle':
		count = 0
		for i in range(-1, 4999):
			if i == -1:
				if (first_column[0] < first_column[1] + first_column[2]) and (first_column[1] < first_column[0] + first_column[2]) and (first_column[2] < first_column[0] + first_column[1]):
					count += 1
			else:
				if (table[first_column[0]][i] < table[first_column[1]][i] + table[first_column[2]][i]) and (table[first_column[1]][i] < table[first_column[0]][i] + table[first_column[2]][i]) and (table[first_column[2]][i] < table[first_column[0]][i] + table[first_column[1]][i]):
					count += 1
		correct_answer = count
	elif random_condition == 'sharpangle':
		count = 0
		for i in range(-1, 4999):
			if i == -1:
				if (first_column[0]**2 < first_column[1]**2 + first_column[2]**2) or (first_column[1]**2 < first_column[0]**2 + first_column[2]**2) or (first_column[2]**2 < first_column[0]**2 + first_column[1]**2):
					count += 1
			else:
				if (table[first_column[0]][i]**2 < table[first_column[1]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[1]][i]**2 < table[first_column[0]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[2]][i]**2 < table[first_column[0]][i]**2 + table[first_column[1]][i]**2):
					count += 1
		correct_answer = count
	elif random_condition == '90angle':
		count = 0
		for i in range(-1, 4999):
			if i == -1:
				if (first_column[0]**2 == first_column[1]**2 + first_column[2]**2) or (first_column[1]**2 == first_column[0]**2 + first_column[2]**2) or (first_column[2]**2 == first_column[0]**2 + first_column[1]**2):
					count += 1
			else:
				if (table[first_column[0]][i]**2 == table[first_column[1]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[1]][i]**2 == table[first_column[0]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[2]][i]**2 == table[first_column[0]][i]**2 + table[first_column[1]][i]**2):
					count += 1
		correct_answer = count
	elif random_condition == 'obtuseangle':
		count = 0
		for i in range(-1, 4999):
			if i == -1:
				if (first_column[0]**2 > first_column[1]**2 + first_column[2]**2) or (first_column[1]**2 > first_column[0]**2 + first_column[2]**2) or (first_column[2]**2 > first_column[0]**2 + first_column[1]**2):
					count += 1
			else:
				if (table[first_column[0]][i]**2 > table[first_column[1]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[1]][i]**2 > table[first_column[0]][i]**2 + table[first_column[2]][i]**2) or (table[first_column[2]][i]**2 > table[first_column[0]][i]**2 + table[first_column[1]][i]**2):
					count += 1
		correct_answer = count
	elif random_condition == 'box':
		count = 0
		if random_equality == 'more':
			for i in range(-1, 4999):
				if i == -1:
					S_MAX = max(first_column)*(sum(first_column)-max(first_column)-min(first_column))
					S_MID = max(first_column)*min(first_column)
					S_MIN = min(first_column)*(sum(first_column)-max(first_column)-min(first_column))
					if S_MAX > S_MID + S_MIN:
						count += 1
				else:
					table_values = [table[first_column[0]][i], table[first_column[1]][i], table[first_column[2]][i]]
					S_MAX = max(table_values)*(sum(table_values)-max(table_values)-min(table_values))
					S_MID = max(table_values)*min(table_values)
					S_MIN = min(table_values)*(sum(table_values)-max(table_values)-min(table_values))
					if S_MAX > S_MID + S_MIN:
						count += 1
		elif random_equality == 'less':
			for i in range(-1, 4999):
				if i == -1:
					S_MAX = max(first_column)*(sum(first_column)-max(first_column)-min(first_column))
					S_MID = max(first_column)*min(first_column)
					S_MIN = min(first_column)*(sum(first_column)-max(first_column)-min(first_column))
					if S_MAX < S_MID + S_MIN:
						count += 1
				else:
					table_values = [table[first_column[0]][i], table[first_column[1]][i], table[first_column[2]][i]]
					S_MAX = max(table_values)*(sum(table_values)-max(table_values)-min(table_values))
					S_MID = max(table_values)*min(table_values)
					S_MIN = min(table_values)*(sum(table_values)-max(table_values)-min(table_values))
					if S_MAX < S_MID + S_MIN:
						count += 1
		correct_answer = count
	elif random_condition == 'five':
		count = 0
		for i in range(-1, 3199):
			if i == -1:
				first_column.sort()
				if (first_column[4] + first_column[0])**2 > (first_column[1]**2 + first_column[2]**2 + first_column[3]**2):
					count += 1
			else:
				table_values = list()
				for key in first_column:
					table_values.append(first_column[key][i])
				table_values.sort()
				if (table_values[4] + table_values[0])**2 > (table_values[1]**2 + table_values[2]**2 + table_values[3]**2):
					count += 1
		correct_answer = count
	return correct_answer

question()