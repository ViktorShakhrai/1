# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    f = "name"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a + self.b > self.c:
            print("Ура, можно построить треугольник!")
        elif self.a < 0 and self.b < 0 and self.c < 0:
            print("С отрицательными числами ничего не выйдет!")
        # elif isinstance(self.a,self.b,self.c,str):


class Point:
    def set_coords(self,x,y):
        self.x = x
        self.y = y
    def get_distance(self,point):
        if isinstance(point,point):
            rez = ((point.x-self.x)**2+(point.y-self.y)**2)**0.5
            return rez
        else:
            print("Передана не точка")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"