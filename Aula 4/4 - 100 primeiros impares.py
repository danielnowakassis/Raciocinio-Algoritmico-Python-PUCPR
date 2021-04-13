"""Escreva um Algoritmo que imprima os 100 primeiros números ímpares. """
#corpo do código
n = 1 
while n < 198:
    n += 2
    print(n)

#ou 
j = 0
n = 2
while j < 100:
    if n % 2 == 0:
        continue
    else:
        print(j)
    n += 1 
    j += 1 

