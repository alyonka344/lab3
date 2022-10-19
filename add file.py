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
