""" Escreva um Algoritmo que imprima os 100 primeiros números ímpares.

Contador = 10

Inteiro Contador

Enquanto Contador > 0 faça
    Leia(NúmeroUsuário)
    Imprima(NúmeroUsuário / 2)
    Contador = Contador - 1



 """
#corpo do código
n = 10
while n > 0:
    j = int(input("Digite um número: "))
    print(j/2)
    n -= 1
