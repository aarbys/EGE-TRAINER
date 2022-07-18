import sqlite3 as sl
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def question_6():
    amount_of_id = 0
    con = sl.connect('six.db')
    d = con.execute("SELECT COUNT(id) from PROBLEMS")
    for c in d:
        amount_of_id = int(*c)
    x = random.randint(1, amount_of_id)
    print('Ниже на нескольких языках будет написан алгоритм.')
    with con:
        output = con.execute("SELECT problem_txt from PROBLEMS WHERE id == {}".format(x))
        answer = con.execute("SELECT answer from PROBLEMS WHERE id == {}".format(x))
        for c in answer:
            correct_answer = int(*c)
        for c in output:
            print(*c)

        output_code(x, 6)
    return correct_answer


def question_22():
    amount_of_id = 0
    con = sl.connect('twenty_two.db')
    d = con.execute("SELECT COUNT(id) from PROBLEMS")
    for c in d:
        amount_of_id = int(*c)
    x = random.randint(1, amount_of_id)  # 1,107
    print('Ниже на нескольких языках будет написан алгоритм.')
    with con:
        output = con.execute("SELECT problem_txt from PROBLEMS WHERE id == {}".format(x))
        answer = con.execute("SELECT answer from PROBLEMS WHERE id == {}".format(x))
        for c in answer:
            correct_answer = int(*c)
        for c in output:
            print(*c)

    output_code(x, 22)
    return correct_answer


def output_code(x: int, connection_to_BD: int):
    db_langs = ['c', 'python', 'basic', 'algorithm', 'pascal']
    image_offset = 45

    print(f'{x} is X')

    def create_four_positions(ime: Image):

        def create_lines(max_wid: int, k_w: int, max_hei: int, k_h: int):  # k - koef
            img1 = ImageDraw.Draw(ime)
            img1.line([(max_wid - k_w, 0), (max_wid - k_w, image_height)], fill=(0, 0, 0), width=10)
            img1.line([(0, max_hei - k_h), (image_width, max_hei - k_h)], fill=(0, 0, 0), width=10)

        width, height = 20, max(text_to_draw_image[0].height, text_to_draw_image[1].height)

        m_h = max(image_to_draw[0].height, image_to_draw[1].height)

        m_w = max(image_to_draw[0].width, image_to_draw[3].width)

        m_h_in_3_4_txt = max(text_to_draw_image[3].height, text_to_draw_image[4].height)

        ime.paste(text_to_draw_image[0], (20, 10))
        ime.paste(text_to_draw_image[1], (m_w + 50, 10))
        ime.paste(text_to_draw_image[3], (20, m_h + 55 + height))
        ime.paste(text_to_draw_image[4], (m_w + 50, m_h + 55 + height))

        create_lines(0, 0, height, 25)
        create_lines(0, 0, height + m_h_in_3_4_txt + m_h, -15)

        m_w += 65
        m_h += 55

        create_lines(m_w, 35, m_h, 45 - height)

        m_h += m_h_in_3_4_txt + height
        ime.paste(image_to_draw[0], (20, height))
        ime.paste(image_to_draw[1], (m_w + 20, height))
        ime.paste(image_to_draw[3], (20, m_h))
        ime.paste(image_to_draw[4], (m_w + 20, m_h))

    def finding_resolution_and_font_type(txt: str):
        image = Image.new('RGB', (200, 100), (255, 255, 255))
        dr = ImageDraw.Draw(image)
        f_t = ImageFont.truetype("arial.ttf", 65)
        trash_1, trash_2, t_wi, t_he, = dr.textbbox(xy=(0, 0), text=txt, font=f_t)
        return t_wi, t_he, f_t

    def taking_problem():
        if connection_to_BD == 22:
            con = sl.connect('twenty_two.db')
        else:
            con = sl.connect('six.db')
        strings_out = []
        for j in db_langs:
            with con:
                output = con.execute(f"SELECT {j} from PROBLEMS WHERE id == {x}")
                for v in output:
                    b = str(*v).replace(' ', ' ')
                    b = b.replace('\r', '')
                    strings_out.append(b)
        return strings_out

    strings = taking_problem()
    image_to_draw = []
    is_basic_required = True
    for text in strings:

        text_width, text_height, font_type = finding_resolution_and_font_type(text)

        im = Image.new('RGB', (text_width + image_offset, text_height + image_offset), (255, 255, 255))

        d = ImageDraw.Draw(im)

        d.text(xy=(2, 2), text=text, fill=(0, 0, 0), font=font_type)

        if text == 'None':
            is_basic_required = False
        image_to_draw.append(im)

    resol = []
    max_height_1, max_height_2 = 0, 0
    max_width_1, max_width_2 = 0, 0
    for i in image_to_draw:
        resol.append([i.width, i.height])
        if len(image_to_draw) == 5 and image_to_draw[2] == i:
            continue
        if max_height_1 < i.height:
            max_height_2 = max_height_1
            max_height_1 = i.height
        else:
            max_height_2 = max(max_height_2, i.height)
        if max_width_1 < i.width:
            max_width_2 = max_width_1
            max_width_1 = i.width
        else:
            max_width_2 = max(max_width_2, i.width)

    image_height = max_height_1 + max_height_2 + 300  # leave space for languages
    image_width = max_width_1 + max_width_2 + 300  # leave space for languages
    img = Image.new('RGB', (image_width, image_height), (255, 255, 255))

    text_to_draw_image = []

    prob_lang = ['c++', 'python', 'basic', 'algorithm', 'pascal']

    for k in prob_lang:
        t_w, t_h, font_type = finding_resolution_and_font_type(k)
        im = Image.new('RGB', (t_w + 45, t_h + 45), (255, 255, 255))

        draw = ImageDraw.Draw(im)

        d = draw

        d.text(xy=(2, t_h - 2), text=k, fill=(0, 0, 0), font=font_type, anchor='lb')
        text_to_draw_image.append(im)

    create_four_positions(img)

    if is_basic_required:
        max_h = max(text_to_draw_image[0].height, text_to_draw_image[1].height)

        image_width_last = image_width + image_to_draw[2].width + 75

        last_img = Image.new('RGB', (image_width_last, image_height), (255, 255, 255))
        img_for_line = ImageDraw.Draw(last_img)

        img_for_line.line([(image_width, 0), (image_width, image_height)], fill=(0, 0, 0), width=10)

        last_img.paste(img, (0, 0))

        last_img.paste(image_to_draw[2], (image_width + 45, text_to_draw_image[1].height))

        last_img.paste(text_to_draw_image[2], (image_width + 50, 10))

        img_for_line.line([(0, max_h - 25), (image_width_last, max_h - 25)], fill=(0, 0, 0), width=10)

        img = last_img.copy()

    img.show()


if __name__ == '__main__':
    question_6()
