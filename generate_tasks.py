from random import randint

students = [
    "Абакумов Алексей Сергеевич",
    "Боголепов Николай Александрович",
    "Дарьин Даниил Олегович",
    "Дядюра Влад Александрович",
    "Ершов Максим Алексеевич",
    "Ковалева Мария Артемовна",
    "Кожокарь Иван Владимирович",
    "Кузуб Даниил Станиславович",
    "Лосюк Дарья Олеговна",
    "Майоров Александр Дмитриевич",
    "Маркова Анна Игоревна",
    "Пантелеев Егор Александрович",
    "Струков Павел Андреевич",
    "Федоров Сергей Владимирович",
    "Финягина Анастасия Денисовна",
    "Харламов Матвей Леонидович",
    "Хисматуллин Дамир Ильдарович",
    "Якубовский Дмитрий Сергеевич"
]

random_set = set()
student_set = set()


def gen_ticket(q1_max, q2_max):
    q1 = randint(1, q1_max)
    while True:
        q2 = randint(1, q2_max)
        if q2 == q1 or (q1, q2) in random_set or (q1, q2) in student_set:
            continue
        break
    random_set.add((q1, q2))
    student_set.add((q1, q2))

    return q1, q2


i = 1
for s in students:
    theory = gen_ticket(8, 8)
    random_set.clear()
    practice = gen_ticket(9, 6)
    print(f"{i}) {s}: теория:{theory}, практика:{practice}", end='\n')
    i += 1

'''
1) Абакумов Алексей Сергеевич: теория:(1, 6), практика:(6, 1)
2) Боголепов Николай Александрович: теория:(5, 8), практика:(3, 4)
3) Дарьин Даниил Олегович: теория:(2, 6), практика:(2, 1)
4) Дядюра Влад Александрович: теория:(3, 7), практика:(9, 1)
5) Ершов Максим Алексеевич: теория:(1, 5), практика:(5, 1)
6) Ковалева Мария Артемовна: теория:(7, 4), практика:(6, 5)
7) Кожокарь Иван Владимирович: теория:(3, 2), практика:(8, 2)
8) Кузуб Даниил Станиславович: теория:(8, 4), практика:(7, 1)
9) Лосюк Дарья Олеговна: теория:(6, 2), практика:(7, 5)
10) Майоров Александр Дмитриевич: теория:(2, 8), практика:(2, 4)
11) Маркова Анна Игоревна: теория:(7, 2), практика:(8, 3)
12) Пантелеев Егор Александрович: теория:(7, 8), практика:(5, 2)
13) Струков Павел Андреевич: теория:(2, 5), практика:(1, 3)
14) Федоров Сергей Владимирович: теория:(2, 7), практика:(7, 6)
15) Финягина Анастасия Денисовна: теория:(5, 4), практика:(4, 6)
16) Харламов Матвей Леонидович: теория:(4, 8), практика:(3, 5)
17) Хисматуллин Дамир Ильдарович: теория:(3, 6), практика:(5, 6)
18) Якубовский Дмитрий Сергеевич: теория:(8, 5), практика:(6, 4)
'''