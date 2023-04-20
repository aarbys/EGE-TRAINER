import random as r


def question():
    c_a = 1
    print('1) Передача файла из города А в С')
    print('2) Количество цветов в изображении')
    print('3) Перезапись файла')
    print('4) Передача текстового файла по кабелю связи')
    print('5) Толя передает файл Мише')
    print('6) Сжатый файл')
    print('7) Прозрачность изображения')
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
        c_a = anatoly_to_misha()
    elif type_of_problem == 6:
        c_a = compressed_file()
    elif type_of_problem == 7:
        c_a = rgba_format_png()
    return c_a


def file_A_to_C_solution(time: int, resolution: float, frequency: float, speed: int, usable_phrases: list):
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
    power_2 = [2 ** i for i in range(0, 22)]
    resolution = [r.choice(power_2), r.randint(2, 33554432)]
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
    power_2 = [2 ** i for i in range(0, 22)]
    resolution = [r.choice(power_2), r.randint(2, 33554432)]
    type_save = r.choice(['Кбайт', 'битах', 'Мбайт', 'байт', 'Гбайт'])
    number = r.randint(1, 2 ** 15)
    print(
        f'Автоматическая фотокамера производит растровые изображения размером {resolution[0]}x{resolution[1]} пикселей.'
        f'При этом объём файла с изображением не может превышать {number} {type_save}, упаковка данных не производится.'
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


def decoding(type_record: str):
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
    power_2 = [2 ** i for i in range(0, 22)]
    type_record = r.choice(['двухканальная (стерео)', 'одноканальная (моно)', 'четырехканальная (квадро)'])
    frequency = r.randint(10, 100)
    bites = r.choice(power_2)
    weight = r.randint(2, 1000)
    type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
    print(
        f'Производилась {type_record} звукозапись\n'
        f'с частотой дискретизации {frequency} кГц и {bites}-битным разрешением.\n '
        f'В результате был получен файл размером {weight} {type_save}, сжатие данных не производилось. \n'
        f'Определите приблизительно, сколько времени (в минутах) проводилась запись. \n'
        f'В качестве ответа укажите ближайшее к времени записи целое число.')
    answer = recording_file_solution(weight, type_save, bites, frequency, type_record)
    return answer


class AudioRewriter:
    def __init__(self):
        self.type_record_1 = r.choice(['стерео', 'моно', 'квадро'])
        self.type_record_2 = r.choice(['стерео', 'моно', 'квадро'])

        self.weight = r.randint(1, 100)

        self.type_save_str = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
        self.type_save_value = size_conversion(self.type_save_str, 1)

        self.less_more_1 = r.choice(['выше', 'ниже'])
        self.less_more_2 = r.choice(['выше', 'ниже'])

        self.amount_less_more_1 = r.randint(10, 70) / 10
        self.amount_less_more_2 = r.randint(10, 70) / 10

        self.type_answer_str = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
        self.type_answer_value = size_conversion(self.type_answer_str, 1)

    def rewriting_audio_solution(self):

        def less_more_sol(coefficient, value: float, argument: str):
            if argument == 'выше':
                return coefficient * value
            else:
                return coefficient / value

        type_record_1 = decoding(self.type_record_1)
        type_record_2 = decoding(self.type_record_2)
        weight = self.weight * self.type_save_value
        index = 1
        if type_record_1 > type_record_2:
            index /= (type_record_1 / type_record_2)
        else:
            index *= (type_record_2 / type_record_1)

        index = less_more_sol(index, self.amount_less_more_1, self.less_more_1)
        index = less_more_sol(index, self.amount_less_more_2, self.less_more_2)
        answer = int((weight * index) / self.type_answer_value)
        return answer

    def print_problem(self):
        print(f'Музыкальный фрагмент был записан в формате {self.type_record_1},\n '
              f'оцифрован и сохранён в виде файла без использования сжатия данных. \n'
              f'Размер полученного файла без учёта размера заголовка файла — {self.weight} {self.type_save_str}. \n'
              f'Затем тот же музыкальный фрагмент был записан повторно в формате {self.type_record_2} и \n'
              f'оцифрован с разрешением в {self.amount_less_more_1} раза {self.less_more_1} и \n'
              f'частотой дискретизации в {self.amount_less_more_2} раза {self.less_more_2}, \n'
              f'чем в первый раз. Сжатие данных не производилось. Укажите размер в {self.type_answer_str} файла,\n'
              'полученного при повторной записи. В ответе запишите только целое число, \n'
              'единицу измерения писать не нужно. Искомый объём не учитывает размера заголовка файла.\n')


def rewriting_audio():
    ar = AudioRewriter()
    ar.print_problem()
    correct_answer = ar.rewriting_audio_solution()
    return correct_answer


def how_many_symbols_solution(code: int, time: int, speed: int):
    answer = speed * time / code
    return answer


def how_many_symbols():
    power_2 = [2 ** i for i in range(0, 22)]
    speed = r.choice(power_2)
    code = r.choice(power_2)
    while code > speed:
        code = r.choice(power_2)
    time = r.randint(1, 15000)
    print(f'Скорость передачи данных через модемное соединение равна {speed} бит/с. \n'
          f'Передача текстового файла через это соединение заняла {time} с. \n'
          ' Определите, сколько символов содержал переданный текст, если известно, \n'
          f' что он был представлен в {code}-битной кодировке .')
    correct_answer = how_many_symbols_solution(code, time, speed)
    return correct_answer


def anatoly_to_misha_solution(first_power: int, second_power: int, files_weight: int, bites_before_send: int):
    size = size_conversion('Мбайт', 1) * files_weight
    delay_time = size_conversion('Кбайт', 1) * bites_before_send / (2 ** first_power)
    time_for_misha = size / (2 ** second_power)
    return delay_time + time_for_misha


def anatoly_to_misha():
    power_2 = [i for i in range(0, 22)]
    files_weight = r.randint(1, 10000)
    first_power = r.choice(power_2)
    second_power = r.choice(power_2)
    bites_before_send = 2 ** r.choice(power_2)
    while second_power >= first_power:
        second_power = r.choice(power_2)
    print('У Толи есть доступ к сети Интернет по высокоскоростному одностороннему радиоканалу,\n '
          f'обеспечивающему скорость получения информации 2 в степени ({first_power})  бит в секунду.\n '
          'У Миши нет скоростного доступа в Интернет, но есть возможность получать информацию от Толи\n '
          f'по низкоскоростному телефонному каналу со средней скоростью 2 в степени ({second_power})  бит в секунду.\n'
          f' Миша договорился с Толей, что тот будет скачивать для него данные\n'
          f'объемом {files_weight} Мбайт по высокоскоростному \n'
          'каналу и ретранслировать их Мише по низкоскоростному каналу')
    print(
        f'Компьютер Толи может начать ретрансляцию данных не раньше,\n'
        f'чем им будут получены первые {bites_before_send} Кбайт этих данных. \n'
        'Каков минимально возможный промежуток времени (в секундах) \n'
        'с момента начала скачивания Толей данных до полного их получения Мишей?')
    correct_answer = anatoly_to_misha_solution(first_power, second_power, files_weight, bites_before_send)
    return correct_answer


def txt_file_solution(amount_symbols: int, first_bites: int, second_bites: int):
    f = amount_symbols * first_bites
    s = amount_symbols * second_bites
    answer = f - s
    return answer


def txt_file():
    power_2 = [2 ** i for i in range(0, 22)]
    amount_symbols = r.choice(power_2)
    first_bites = r.choice(power_2)
    while first_bites == 2 ** 22:
        first_bites = r.choice(power_2)
    second_bites = r.choice(power_2)
    while second_bites <= 2 ** 22:
        second_bites = r.choice(power_2)
    print(f'Текстовый документ, состоящий из {amount_symbols} символов, хранился в {first_bites}-битной кодировке. \n'
          f'Этот документ был преобразован в {second_bites}-битную кодировку. \n'
          f'Укажите, какое дополнительное количество бит потребуется для хранения документа. \n'
          f'В ответе запишите только число.')
    correct_answer = txt_file_solution(amount_symbols, first_bites, second_bites)
    return correct_answer


def compressed_file_solution(weight: int, type_save: str, resolution: list, percent: int):
    res_mult_percent = resolution[0] * resolution[1] * (100 - percent) / 100
    size = size_conversion(type_save, 1) * weight
    i = int(size / res_mult_percent)
    try:
        answer = 2 ** i
        if answer > 2 ** 20:
            return -1
        else:
            return answer
    except OverflowError:
        return -1


def compressed_file():
    while True:
        power_2 = [2 ** i for i in range(22)]
        resolution = [r.choice(power_2), r.randint(2, 33554432)]
        resolution.sort(reverse=True)
        weight = r.randint(1, 1000)
        type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
        percent = r.randint(10, 70)
        answer = compressed_file_solution(weight, type_save, resolution, percent)
        if answer != -1:
            break
    print(
        f'Для хранения произвольного сжатого растрового изображения размером {resolution[0]}x{resolution[1]} пикселей\n'
        f'отведено {weight} {type_save} памяти без учёта размера заголовка файла.\n'
        'Для кодирования цвета каждого пикселя используется одинаковое количество бит,\n'
        'коды пикселей записываются в файл один за другим без промежутков.\n'
        'После сохранения информации о пикселях изображение сжимается.\n'
        f'Размер итогового файла после сжатия на {percent}% меньше исходного.\n'
        'Какое максимальное количество цветов можно использовать в изображении?')
    return answer


def compressed_file_v2_solution(weight: int, type_save: str, resolution: list, percent: int):
    res = resolution[0] * resolution[1]
    size = size_conversion(type_save, 1) * weight * ((100 + percent) / 100)
    i = int(size / res)
    try:
        answer = 2 ** i
        if answer > 2 ** 20:
            return -1
        else:
            return answer
    except OverflowError:
        return -1


def compressed_file_v2():
    while True:
        power_2 = [2 ** i for i in range(22)]
        resolution = [r.choice(power_2), r.randint(2, 33554432)]
        resolution.sort(reverse=True)
        weight = r.randint(1, 1000)
        type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
        percent = r.randint(10, 70)
        answer = compressed_file_v2_solution(weight, type_save, resolution, percent)
        if answer != -1:
            break
    print(
        f'Для хранения сжатого произвольного растрового изображения размером {resolution[0]}x{resolution[1]} пикселей\n'
        f'отведено {weight} {type_save} памяти без учёта размера заголовка файла.\n'
        f'Файл оригинального изображения больше сжатого на {percent}%.\n'
        'Для кодирования цвета каждого пикселя используется одинаковое количество бит,\n'
        'коды пикселей записываются в файл один за другим без промежутков.\n'
        'Какое максимальное количество цветов можно использовать в изображении?')
    return answer


def rgba_format_png_solution(weight: int, type_save: str, resolution: list, amount_bits: int):
    res = resolution[0] * resolution[1]
    size = size_conversion(type_save, 1) * weight
    i = int(size / res) - amount_bits
    if i < 0:
        return -1
    try:
        answer = 2 ** i
        if answer > 2 ** 20:
            return -1
        else:
            return answer
    except OverflowError:
        return -1

    # res * (i+a_b) = size
    # i+a_b = size/res
    #


def rgba_format_png():
    while True:
        power_2 = [2 ** i for i in range(22)]
        resolution = [r.choice(power_2), r.randint(2, 33554432)]
        resolution.sort(reverse=True)
        weight = r.randint(1, 1000)
        type_save = r.choice(['Кбайт', 'Мбайт', 'байт', 'Гбайт'])
        amount_bits = r.randint(2, 32)
        answer = rgba_format_png_solution(weight, type_save, resolution, amount_bits)
        if answer != -1:
            break
    print(f'Для хранения произвольного растрового изображения размером {resolution[0]}x{resolution[1]} пикселей\n'
          f'отведено {weight} {type_save} памяти без учёта размера заголовка файла.\n'
          f'При кодировании каждого пикселя используется {amount_bits} бит для определения степени прозрачности\n'
          'и одинаковое количество бит для указания его цвета.\n'
          'Коды пикселей записываются в файл один за другим без промежутков.\n'
          'Какое максимальное количество цветов (без учета степени прозрачности) можно использовать в изображении?')
    return answer
