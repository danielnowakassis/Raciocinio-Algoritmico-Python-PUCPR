"""Escreva um Algoritmo que imprima os número de 1 à 100, menos os múltiplos de 5"""


#corpo do código
n = 1
while n < 100:
    if n % 5 != 0:
        print(n)
    n += 1
