import matplotlib.pyplot as plt
import random as rnd
from Point import Point

# Задание 1

def draw1(p0: Point, p1: Point, p2: Point):
    figure = plt.figure()
    plt.plot([p1.x, p2.x], [p1.y, p2.y])  # рисуем прямую
    plt.text(p1.x + 0.1, p1.y + 0.1, "P1")
    plt.text(p2.x + 0.1, p2.y + 0.1, "P2")
    plt.text(p0.x + 0.1, p0.y + 0.1, "P0")
    grid = plt.grid(True)
    p0 = plt.scatter([p1.x, p2.x, p0.x], [p1.y, p2.y, p0.y]) # рисуем точки

def det(a, b, c, d):
    return a * d - b * c

def checkPlace(points: list) -> int:
    d = det(points[1].x - points[0].x, points[1].y - points[0].y, points[2].x - points[0].x, points[2].y - points[0].y)
    return d

def initPoints(n) -> list:
    X = [rnd.randint(0, 10) for _ in range(n)]
    Y = [rnd.randint(0, 10) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        points.append(el)
    return points


def init1():
    n = 3
    points = initPoints(n)  # массив, где первый элемент - точка Р0

    answer1 = checkPlace(points)
    draw1(points[0], points[1], points[2])

    if int(answer1) > 0:
        plt.suptitle('Левее', fontsize=10)
    elif int(answer1) < 0:
        plt.suptitle('Правее', fontsize=10)
    elif int(answer1) == 0:
        plt.suptitle('На прямой', fontsize=10)

    plt.show()

init1()

#Задание 2


def draw2(p1: Point, p2: Point, p3: Point, p4: Point):
    figure = plt.figure()
    plt.plot([p1.x, p2.x], [p1.y, p2.y])  # рисуем прямую
    plt.plot([p3.x, p4.x], [p3.y, p4.y])  # рисуем прямую
    plt.text(p1.x + 0.1, p1.y + 0.1, "P1")
    plt.text(p2.x + 0.1, p2.y + 0.1, "P2")
    plt.text(p3.x + 0.1, p3.y + 0.1, "P3")
    plt.text(p4.x + 0.1, p4.y + 0.1, "P4")
    grid = plt.grid(True)
    p0 = plt.scatter([p1.x, p2.x, p3.x, p4.x], [p1.y, p2.y, p3.y, p4.y])  # рисуем точки

def areIntersect(P1: Point, P2: Point, P3: Point, P4: Point) -> bool:
    d1 = det(P4.x - P3.x, P4.y - P3.y, P1.x - P3.x, P1.y - P3.y)
    d2 = det(P4.x - P3.x, P4.y - P3.y, P2.x - P3.x, P2.y - P3.y)
    d3 = det(P2.x - P1.x, P2.y - P1.y, P3.x - P1.x, P3.y - P1.y)
    d4 = det(P2.x - P1.x, P2.y - P1.y, P4.x - P1.x, P4.y - P1.y)

    c1 = (P3.x - P1.x) * (P4.x - P1.x) + (P3.y - P1.y) * (P4.y - P1.y)
    c2 = (P3.x - P2.x) * (P4.x - P2.x) + (P3.y - P2.y) * (P4.y - P2.y)
    c3 = (P1.x - P3.x) * (P2.x - P3.x) + (P1.y - P3.y) * (P2.y - P3.y)
    c4 = (P1.x - P4.x) * (P2.x - P4.x) + (P1.y - P4.y) * (P2.y - P4.y)

    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == 0:
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0:
            return False
        else:
            return True
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False

def init2():
    n = 4
    points = initPoints(n)

    answer2 = areIntersect(points[0], points[1], points[2], points[3])
    draw2(points[0], points[1], points[2], points[3])

    if answer2:
        plt.suptitle('Пересекаются', fontsize=10)
    else:
        plt.suptitle('Не пересекаются', fontsize=10)

    plt.show()

init2()

#Задание 3

def drawPolygon(points: list):
    for i in range(0, len(points)):
        if i + 1 == len(points):
            k = 0  # k - индекс последней точки
        else:
            k = i + 1
        plt.scatter(points[i].x, points[i].y)
        plt.text(points[i].x + 0.1, points[i].y + 0.1, 'P{}'.format(i+1))
        plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y])
    grid = plt.grid(True)

def isPolygonSimple(points: list) -> bool:
    n = len(points)
    for i in range(len(points) - 2):
        if i == 0:
            t = n - 1
        else:
            t = n
        for j in range(i + 2, t):
            if areIntersect(points[i], points[(i+1)], points[j], points[(j+1) % n]):
                return False
        #t += 1
    return True

def init3():
    n = 5
    points = initPoints(n)

    answer3 = isPolygonSimple(points)
    drawPolygon(points)

    if answer3:
        plt.suptitle('Простой', fontsize=10)
    else:
        plt.suptitle('Не простой', fontsize=10)

    plt.show()

init3()