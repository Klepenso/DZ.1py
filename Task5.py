# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = float(input('Ось x:'))
ay = float(input('Ось y:'))
bx = float(input('Ось x:'))
by = float(input('Ось y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {distans}' )