# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#      xc,yc
#       C
#      /|\
#    b/ | \a
#    /  h  \
#   /   |   \
#  A____c____B
# xa,ya    xb,yb
#
# h(c) = 2*S/c
#
import math

class Triangle:
    def __init__(self, xa, ya, xb, yb, xc, yc):
        self.xa = xa
        self.xb = xb
        self.xc = xc
        self.ya = ya
        self.yb = yb
        self.yc = yc
        self.a = tr_side(self.xb, self.yb, self.xc, self.yc)
        self.b = tr_side(self.xa, self.ya, self.xc, self.yc)
        self.c = tr_side(self.xa, self.ya, self.xb, self.yb)
    def __str__(self):
        return str('---------------\n'+
                   '      xc,yc \n'+
                   '       C \n'+
                   '      /|\ \n'+
                   '    b/ | \\a \n'+
                   '    /  h  \ \n'+
                   '   /   |   \ \n'+
                   '  A____c____B \n'+
                   ' xa,ya    xb,yb \n'+
                   '--------------- \n')
        
        
    def square(self):
        S = tr_square(self.a, self.b, self.c)
        print('S = :')
        return S
    def height(self):
        print('height a, height b, height c: ', tr_height(self.a, self.b, self.c))
        
    def perimeter(self):
        perim = 2 * pperim(self.a, self.b, self.c)
        print('Perimeter = :')
        return perim
        
def tr_side(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    side = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return side

def pperim(a = 0, b = 0, c = 0):
    return float((a + b + c) / 2)

def tr_square(a = 0, b = 0, c = 0):
    pp = pperim(a, b, c)
    return math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))

def tr_height(a = 0, b = 0, c = 0):
    S = tr_square(a, b, c)
    ha = float(2 * S / a)
    hb = float(2 * S / b)
    hc = float(2 * S / c)
    return (ha, hb, hc)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

