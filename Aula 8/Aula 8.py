"""2) Desenvolva uma App em Python para somar as duas listas abaixo e gera
uma terceira com o resultado. Ao fina, a App deverá imprimir as três listas.
A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54]
B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] 
"""

A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54]
B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] 
C = []
for i in range(len(A)):
    C.append(A[i] + B[i])

print(A)
print(B)
print(C)

"""
3) Desenvolver uma App em Python para gerar e imprimir uma
lista com os 100 primeiros números inteiros de 1 até 100.
"""
lista = []
for i in range(1,101,1):
    lista.append(i)
print(lista)

"""4) Desenvolver uma App em Python para gerar e imprimir uma
lista com os 50 primeiros números pares de 1 até 100."""

lista = []
for i in range(2,101,2):
    lista.append(i)
print(lista)

