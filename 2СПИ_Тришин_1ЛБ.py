def main():


    # 1 задание
    a = input()
    b = input()
    c = input()
    print('билет на', a, 'в', b, "на", c, 'забранирован')

    # 2 задание
    g = int(input("зарплата за месяц:"))
    f = int(input("количество отработанных в выходные:"))
    print("размер премии", g * 0.01 * f)

    # 3 задание
    j = int(input('напишите количество купюр:'))
    tus = j // 1000
    j = j % 1000
    sot = j // 100
    j = j % 100
    des = j // 10
    j = j % 10
    print(tus)
    print(sot)
    print(des)
    print(a)

    # 4 задание
    o = input("оцените развлекательный центр:")
    print(o.find("весело"), o.find("увлекательный"), o.find('развлечение'))

    # 5 задание
    s = input()
    print(s[(len(s) - 1) // 2])

    # 6 задание
    l = "Алиса и Ваня большое спосибо за теплый прием!"
    n1 = l[0:5]
    n2 = l[8:12]
    print("прием", n1 + "/" + n2)

    # 7 задание
    z = "ABCDEFGHIJKLMOPQRSTUWXYZ"
    w = int(input())
    print(a[w:w + 4])

    # 8.1 - 8.8 задания
    g = [0]
    print(g)

    a = [0, 1]
    a.append(5)
    print(a)

    f = [1, 1, 2, 3, 4, 6, 7, 8, 4, 2, 0]
    f.remove(1)
    print(f)

    print(f[1:9])

    f.reverse()
    print(f[::-1])

    d = [[1, 2, 3], [[1, 8, 0, 7], 7, 9]]
    print(d[0][2:])
    print(d[1][0][1])

    m = [1, 2, 3, 4, 5]
    m.clear()
    print(m)

    # 9.1 - 9.2 задания
    a = ()
    print(a)

    d = (35, "я не сдам до 5 ноября", 1, "f[f[f[f[f")
    print(d)

    # 10.1 - 10.4 задания
    set_c = {}
    print(set_c)

    set_l = {"1,2,3"}
    print(set_l)

    letters = {'а', 'б', 'в'}
    letters.add('г')
    print(letters)

    set_g = {2, 3, 5, 1, 8}
    set_h = {2, 5, 0, 9, 7}
    print(set_g.intersection(set_h))  # Пересечение
    set_a = {1, 2, 3}
    set_b = {4, 5, 6}
    print(set_a.union(set_b))  # Объединение
    set_v = {4, 9, 7, 2, 1, 0}
    set_k = {5, 8, 3, 1, 4, 9}
    print(set_v.difference(set_k))  # Разность
    set_aa = {1, 2, 3, 4}
    set_bb = {6, 8, 4, 3}
    print(set_aa.symmetric_difference(set_bb))  # Симметрическая

    # 11.1 - 11.5 задание
    info_dict = {}
    my_dict = dict()

    car = {'модель': 'Audi A5 Sportback', 'цвет': 'красный', 'пробег': '100500 км'}
    print(car)

    s = {'должность': 'разработчик', 'имя': 'Антон'}
    s['фамилия'] = 'Егоров'
    print(s)

    d = {'жанр': 'триллер', 'рейтинг': 7.5, 'название': 'Опасные связи'}
    del d['название']
    print(d)

    d = {'должность': 'разработчик', 'имя': 'Антон'}
    d['имя'] = 'Евгений'
    print(d)

if __name__ == "__main__":
    main()