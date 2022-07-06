import random as r


def question():
    c_a = 1
    print('1) Передача файла из города А в С')
    print('2) Количество цветов в изображении')
    print('3) Перезапись файла')
    print('4) Передача текстового файла по кабелю связи')
    print('5) Толя передает файл Мише')
    print('6) Передача файла из города А в С')
    type_of_problem = int(input())
    if type_of_problem == 1:
        c_a = file_A_to_C()
    elif type_of_problem == 2:
        if r.randint(1, 2) == 1:
            c_a = picture_w()
        else:
            c_a = picture_c()
    elif type_of_problem == 3:
        c_a = rewriting_audio()
    elif type_of_problem == 4:
        c_a = how_many_symbols()
    elif type_of_problem == 5:
        c_a = tolya_to_misha()
    return c_a


def file_A_to_C_solution(time: int, resolution: int, frequency: int, speed: int, usable_phrases: list):
    weight = 1
    s_time = 1
    if usable_phrases[0] == 'выше':
        weight *= resolution
    else:
        weight /= resolution
    if usable_phrases[1] == 'выше':
        weight *= frequency
    else:
        weight /= frequency
    if usable_phrases[2] == 'выше':
        s_time /= speed
    else:
        s_time *= speed
    answer = int(time * weight * s_time)
    return answer


def file_A_to_C():
    phrases = ['выше', 'ниже']
    time = r.randint(10, 100)
    resolution = int(r.random() * 100) / 10
    frequency = int(r.random() * 100) / 10
    speed = int(r.random() * 10)
    usable_phrases = [r.choice(phrases) for _ in range(3)]
    correct_answer = file_A_to_C_solution(time, resolution, frequency, speed, usable_phrases)
    print('Музыкальный фрагмент был оцифрован и записан в виде файла без использования сжатия данных.')
    print('Получившийся файл был передан в город А по каналу связи за {} секунд.'.format(time))
    print(
        'Затем тот же музыкальный фрагмент был оцифрован повторно с разрешением в {} раза {}\n'
        'и частотой дискретизации в {} раза {}, чем в первый раз.'.format(resolution, usable_phrases[0], frequency,
                                                                          usable_phrases[1]))

    print('Сжатие данных не производилось.')
    print('Полученный файл был передан в город Б')
    print('Пропускная способность канала связи с городом Б в {} раза {},'
          ' чем канала связи с городом А.'.format(speed,
                                                  usable_phrases[
                                                      2]))
    print('Сколько секунд длилась передача файла в город Б?')
    print('В ответе запишите только целое число, единицу измерения писать не нужно.')
    return correct_answer


def picture_w_solution(resolution: list, color: int, type_answer: str):
    i = 0
    while 2 ** i < color:
        i += 1
    answer = resolution[0] * resolution[1] * i
    weight = size_conversion(type_answer, 2)
    return answer // weight


def picture_w():
    grades_2 = [2 ** i for i in range(0, 22)]
    resolution = [r.choice(grades_2), r.randint(2, 33554432)]
    color = r.randint(2, 33554432)
    type_answer = r.choice(['Кбайт', 'битах', 'Мбайт', 'байт', 'Гбайт'])
    correct_answer = picture_w_solution(resolution, color, type_answer)
    print(
        'Какой минимальный объём памяти (в {}) нужно зарезервировать, '
        '\nчтобы можно было сохранить любое растровое изображение '
        '\nразмером {}x{} пикселей при условии, '
        '\nчто в изображении могут использоваться {} различных цветов?'.format(
            type_answer, resolution[0], resolution[1], color))
    print('В ответе запишите только целое число, единицу измерения писать не нужно.')
    return correct_answer


def picture_c_solution(number: int, type_save: str, resolution: list):
    x = resolution[0] * resolution[1]
    weight = size_conversion(type_save, 1) * number
    answer = weight // x
    return answer


def picture_c():
    grades_2 = [2 ** i for i in range(0, 22)]
    resolution = [r.choice(grades_2), r.randint(2, 33554432)]
    type_save = r.choice(['Кбайт', 'битах', 'Мбайт', 'байт', 'Гбайт'])
    number = r.randint(1, 2 ** 15)
    print(
        f'Автоматическая фотокамера производит растровые изображения размером {resolution[0]}x{resolution[1]} пикселей. '
        f'При этом объём файла с изображением не может превышать {number} {type_save}, упаковка данных не производится. '
        'Какое максимальное количество цветов можно использовать в палитре?')
    answer = picture_c_solution(number, type_save, resolution)
    return 2 ** answer


def size_conversion(type_save: str, more_less: 'More = 1 Less = else'):
    weight = 1
    if more_less == 1:
        if type_save == 'байт':
            weight *= (2 ** 3)
        elif type_save == 'Кбайт':
            weight *= (2 ** 3 * 2 ** 10)
        elif type_save == 'Мбайт':
            weight *= (2 ** 3 * 2 ** 10 * 2 ** 10)
        elif type_save == 'Гбайт':
            weight *= (2 ** 3 * 2 ** 10 * 2 ** 10 * 2 ** 10)
    else:
        if type_save == 'байт':
            weight //= (2 ** 3)
        elif type_save == 'Кбайт':
            weight //= (2 ** 3 * 2 ** 10)
        elif type_save == 'Мбайт':
            weight //= (2 ** 3 * 2 ** 10 * 2 ** 10)
        elif type_save == 'Гбайт':
            weight //= (2 ** 3 * 2 ** 10 * 2 ** 10 * 2 ** 10)
    return weight


def decoding(type_record):
    if 'стерео' in type_record:
        type_record = 2
    elif 'моно' in type_record:
        type_record = 1
    else:
        type_record = 4
    return type_record


def recording_file_solution(weight: int, type_save: str, bites: int, frequency: int, type_record: str):
    type_record = decoding(type_record)
    type_save = size_conversion(type_save, 1)

    weight = weight * type_save
    near_time = frequency * 1000 * type_record * bites
    return int((weight / near_time) / 60)


def recording_file():
    grades_2 = [2 ** i for i in range(0, 22)]
    type_record = r.choice(['двухканальная (стерео)', 'одноканальная (моно)', 'четырехканальная (квадро)'])
    frequency = r.randint(10, 100)
    bites = r.choice(grades_2)
    weight = r.randint(2, 1000)
    type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
    print(
        f'Производилась {type_record} звукозапись с частотой дискретизации {frequency} кГц и {bites}-битным разрешением.\n '
        f'В результате был получен файл размером {weight} {type_save}, сжатие данных не производилось. \n'
        f'Определите приблизительно, сколько времени (в минутах) проводилась запись. \n'
        f'В качестве ответа укажите ближайшее к времени записи целое число.')
    answer = recording_file_solution(weight, type_save, bites, frequency, type_record)
    return answer


def rewriting_audio_solution(type_record_1: str, type_record_2: str, weight: int, type_save: str, less_more_1: str,
                             less_more_2: str,
                             amount_less_more_1: int, amount_less_more_2: int, type_answer: str):
    def less_more_sol(index: int, value: int, argument: str):
        if argument == 'выше':
            return index * value
        else:
            return index / value

    type_record_1 = decoding(type_record_1)
    type_record_2 = decoding(type_record_2)
    type_save = size_conversion(type_save, 1)
    type_answer = size_conversion(type_answer, 1)
    weight = weight * type_save
    index = 1
    if type_record_1 > type_record_2:
        index /= (type_record_1 / type_record_2)
    else:
        index *= (type_record_2 / type_record_1)

    index = less_more_sol(index, amount_less_more_1, less_more_1)
    index = less_more_sol(index, amount_less_more_2, less_more_2)
    # original_weight = type_record_1 * time * bites * frequency* type_save
    answer = int((weight * index) / type_answer)
    return answer


def rewriting_audio():
    type_record_1 = r.choice(['стерео', 'моно', 'квадро'])
    type_record_2 = r.choice(['стерео', 'моно', 'квадро'])
    weight = r.randint(1, 100)
    type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
    less_more_1 = r.choice(['выше', 'ниже'])
    less_more_2 = r.choice(['выше', 'ниже'])
    amount_less_more_1 = r.randint(10, 70) / 10
    amount_less_more_2 = r.randint(10, 70) / 10
    type_answer = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
    print(f'Музыкальный фрагмент был записан в формате {type_record_1},\n '
          f'оцифрован и сохранён в виде файла без использования сжатия данных. \n'
          f'Размер полученного файла без учёта размера заголовка файла — {weight} {type_save}. \n'
          f'Затем тот же музыкальный фрагмент был записан повторно в формате {type_record_2} и \n'
          f'оцифрован с разрешением в {amount_less_more_1} раза {less_more_1} и \n'
          f'частотой дискретизации в {amount_less_more_2} раза {less_more_2}, \n'
          f'чем в первый раз. Сжатие данных не производилось. Укажите размер в {type_answer} файла,\n'
          'полученного при повторной записи. В ответе запишите только целое число, \n'
          'единицу измерения писать не нужно. Искомый объём не учитывает размера заголовка файла.\n')
    correct_answer = rewriting_audio_solution(type_record_1, type_record_2, weight, type_save, less_more_1,
                                              less_more_2, amount_less_more_1, amount_less_more_2, type_answer)
    return correct_answer


def how_many_symbols_solution(code: int, time: int, speed: int):
    answer = speed * time / code
    return answer


def how_many_symbols():
    grades_2 = [2 ** i for i in range(0, 22)]
    speed = r.choice(grades_2)
    code = r.choice(grades_2)
    while code > speed:
        code = r.choice(grades_2)
    time = r.randint(1, 15000)
    print(f'Скорость передачи данных через модемное соединение равна {speed} бит/с. \n'
          f'Передача текстового файла через это соединение заняла {time} с. \n'
          ' Определите, сколько символов содержал переданный текст, если известно, \n'
          f' что он был представлен в {code}-битной кодировке .')
    correct_answer = how_many_symbols_solution(code, time, speed)
    return correct_answer


def tolya_to_misha(first_grade: int, second_grade: int, files_weight: int, bites_before_send: int):
    size = size_conversion('Мбайт', 1) * files_weight
    delay_time = size_conversion('Кбайт', 1) * bites_before_send / (2 ** first_grade)
    time_for_misha = size / (2 ** second_grade)
    return delay_time + time_for_misha


def tolya_to_misha():
    grades_2 = [i for i in range(0, 22)]
    files_weight = r.randint(1, 10000)
    first_grade = r.choice(grades_2)
    second_grade = r.choice(grades_2)
    bites_before_send = 2 ** r.choice(grades_2)
    while second_grade >= first_grade:
        second_grade = r.choice(grades_2)
    print('У Толи есть доступ к сети Интернет по высокоскоростному одностороннему радиоканалу, '
          f'обеспечивающему скорость получения информации 2 в степени ({first_grade})  бит в секунду. '
          'У Миши нет скоростного доступа в Интернет, но есть возможность получать информацию от Толи '
          f'по низкоскоростному телефонному каналу со средней скоростью 2 в степени ({second_grade})  бит в секунду.'
          f' Миша договорился с Толей, что тот будет скачивать для него данные объемом {files_weight} Мбайт по высокоскоростному '
          'каналу и ретранслировать их Мише по низкоскоростному каналу')
    print(
        f'Компьютер Толи может начать ретрансляцию данных не раньше, чем им будут получены первые {bites_before_send} Кбайт этих данных. '
        'Каков минимально возможный промежуток времени (в секундах) '
        'с момента начала скачивания Толей данных до полного их получения Мишей?')
    correct_answer = tolya_to_misha(first_grade, second_grade, files_weight, bites_before_send)


def txt_file_solution(amount_symbols: int, first_bites: int, seconde_bites: int):
    f = amount_symbols * first_bites
    s = amount_symbols * seconde_bites
    answer = f -s
    return answer


def txt_file():
    grades_2 = [2 ** i for i in range(0, 22)]
    amount_symbols = r.choice(grades_2)
    first_bites = r.choice(grades_2)
    while first_bites == 2 ** 22:
        first_bites = r.choice(grades_2)
    seconde_bites = r.choice(grades_2)
    while seconde_bites <= 2 ** 22:
        seconde_bites = r.choice(grades_2)
    print(f'Текстовый документ, состоящий из {amount_symbols} символов, хранился в {first_bites}-битной кодировке. \n'
          f'Этот документ был преобразован в {seconde_bites}-битную кодировку. \n'
          f'Укажите, какое дополнительное количество бит потребуется для хранения документа. \n'
          f'В ответе запишите только число.')
    correct_answer = txt_file_solution(amount_symbols, first_bites, seconde_bites)
