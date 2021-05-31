"""
Desenvolva uma App em Python para ler um conjunto de 20 valores
inteiros digitado no teclado e que gere uma outra lista com a soma dos
elementos equidistantes. Ao final, App deverá imprimir as duas listas.
Exemplo de uma lista com 6 elementos.
Lido lista A = 1, 2, 3, 4, 5, 6
Calculado lista B = 7, 7, 7

lista = []
lista_equidistante = []

Lista lista, lista_equidistante

Para i no Escopo(0, 20, 1):
    inteiro a
    a = Leia("Digite um número: ")
    lista.adicionar(a)
Para j no Escopo(0, 10, 1):
    lista_equidistante.adicionar(lista[j] + lista[-1 - j])
print(lista)
print(lista_equidistante)
"""
lista = []
lista_equidistante = []
for i in range(20):
    a = int(input("Digite um número: "))
    lista.append(a)
for j in range(10):
    lista_equidistante.append(lista[j] + lista[-1 - j])
print(lista)
print(lista_equidistante)


"""2) Desenvolva uma App em Python para somar as duas listas abaixo e gera
uma terceira com o resultado. Ao final, a App deverá imprimir as três listas.
A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54]
B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] 


A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54]
B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] 
C = []

lista A, B, C

Para i no Escopo(0, tamanho(Lista), 1):
    C.adicionar(A[i] + B[i])

Imprima(A)
Imprima(B)
Imprima(C)
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

lista = []

Lista lista 

Para i no Escopo(1,101,1):
    lista.adicionar(i)
Imprima(lista)
"""
lista = []
for i in range(1,101,1):
    lista.append(i)
print(lista)

"""4) Desenvolver uma App em Python para gerar e imprimir uma
lista com os 50 primeiros números pares de 1 até 100.

lista = []

Lista lista

Para i no Escopo(2,101,2):
    lista.adicionar(i)
print(lista)
"""

lista = []
for i in range(2,101,2):
    lista.append(i)
print(lista)

"""5) Desenvolva uma App em Python que leia um número N inteiro
do teclado. Em seguida, leia N números inteiros digitados e
guarde numa lista. Ao final, crie e imprima uma lista com os
valores maiores que 3, os pares, os divisíveis por 5 e a soma dos
ímpares.

n = int(input("Digite o números de digitos que deseja adicionar a lista: "))
soma_impares = 0
lista = []
lista_maior_3 = []
lista_pares = []
lista_5 = []
lista_soma_impares = []

Inteiro n, soma_impares

Lista lista, lista_maior_3, lista_pares, lista_5, lista_soma_impares


Para i no Escopo(0, n, 1):
    num = int(input("Digite um número: "))
    lista.append(num)
for j no Escopo(tamanho(lista)):
    Se lista[j] > 3:
        lista_maior_3.adicionar(lista[j])
    Se lista[j] % 2 == 0:
        lista_pares.adicionar(lista[j])
    Se lista[j] % 5 == 0:
        lista_5.adicionar(lista[j])
    Se lista[j] % 2 != 0:
        soma_impares += lista[j]
lista_soma_impares.adicionar(soma_impares)
Imprima(lista)
Imprima(lista_maior_3)
Imprima(lista_pares)
Imprima(lista_5)
Imprima(lista_soma_impares)
"""

n = int(input("Digite o números de digitos que deseja adicionar a lista: "))
soma_impares = 0
lista = []
lista_maior_3 = []
lista_pares = []
lista_5 = []
lista_soma_impares = []
for i in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)
for j in range(len(lista)):
    if lista[j] > 3:
        lista_maior_3.append(lista[j])
    if lista[j] % 2 == 0:
        lista_pares.append(lista[j])
    if lista[j] % 5 == 0:
        lista_5.append(lista[j])
    if lista[j] % 2 != 0:
        soma_impares += lista[j]
lista_soma_impares.append(soma_impares)
print(lista)
print(lista_maior_3)
print(lista_pares)
print(lista_5)
print(lista_soma_impares)