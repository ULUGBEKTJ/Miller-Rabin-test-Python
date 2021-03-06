import sys
def isPrime(n, k=5): # количество раундов проверки
    from random import randint
    if n < 2: return False # число не простое
    for p in [2,3,5,7,11,13,17,19,23,29]: # начальные простые числа чтобы сократить время работы программы.
        if n % p == 0: return n == p
    s = 0
    d = n-1 

    # алоритм n - 1 = 2^S * t 
    while d % 2 == 0: # пока d делится на 2 без остатка, мы делим его на 2
        s = s + 1
        d = d/2 # вычисляем степень 2-ки S . когда d перестанет делить на 2, то мы нашли t


    for i in range(k):# выполняет K раз проверку.
        x = pow(randint(2, n-1), int(d), n) # Выбираем случ число в диапазоне от [2 n-2]. затем сразу возводим в степень Pow(a,b,n)согласно алгоритму
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n#возведение степени по модулю ( сначала возводим в степень, затем от результата берем модуль%( остаток от деления )

            if x == 1: return False# x == 1 значит число составное. иначе продолжаем цикл согласно алгоритму
            if x == n-1: break
        else: return False
    return True


n = int(input())
if (isPrime(n)):
    print ('число простое')
else:
    print ('число не простое')
