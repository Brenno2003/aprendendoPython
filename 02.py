from math import radians, sin, cos, tan, degrees
n = float(input('Qual é o angulo: '))
n1 = radians(n)
Cg = cos(n1)
Sg = sin(n1)
Tg = tan(n1)
print('O angulo de {} tem o seno de {}, o cosseno de {} e a tangente de {}'.format(n, Sg, Cg, Tg))




