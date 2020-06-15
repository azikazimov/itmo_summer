import math

def plos(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return('у нас тут так нельзя')
    try:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        if s == 0:
            return 'ай, ай. какой-то неправильный треугольник.'
        return s
    except ValueError:
        return 'ай, ай. какой-то неправильный треугольник.'

print(plos(1, 1, 3)) #just debug
