def circle(r):
    s = int(3.14 * r**2)
    l = int(2 * 3.14 * r)
    return (s, l)

def triangle(a, b, c):
    l = a + b + c
    p = l // 2
    s = int((p * (p - a) * (p - b) * (p - c))**0.5)
    return (s, l)

def rectangle(a, b):
    l = (a + b) * 2
    s = a * b
    return (s, l)

function = input()
if function == 'circle':
    print('Введите радиус окружности: ')
    r = int(input())
    s, l = circle(r)
    print('s = ', s, '\nl = ', l)
elif function == 'triangle':
    print('Введите стороны треугольника: ')
    a = int(input())
    b = int(input())
    c = int(input())
    s, l = triangle(a, b, c)
    print('s = ', s, '\nl = ', l)
elif function == 'rectangle':
    print('Введите стороны прямоугольника: ')
    a = int(input())
    b = int(input())
    s, l = rectangle(a, b)
    print('s = ', s, '\nl = ', l)
