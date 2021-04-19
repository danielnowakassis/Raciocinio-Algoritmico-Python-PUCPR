"""Criar um Algoritmo que leia um número (NUM), e depois leia NUM números
inteiros e imprima o menor deles

num <- int(input("Digite um número: "))
num_inicial <- num
menor <- 0
Inteiros num, num_inicial, menor

Enquanto num > 0 faça
    Leia(Número)
    Se número < 0 então
        Imprima("Digite números maiores que 0")
        abandone
    Se num_inicial = num and menor == 0 então
        menor = numero
    Se numero < menor então 
        menor = numero
    num -= 1
print(menor)




"""
num = int(input("Digite um número: "))
num_inicial = num
menor = 0

while num > 0:
    numero = int(input("Digite um número para comparação: "))
    if numero < 0:
        print("Digite números maiores que 0")
        exit(0)
    if num_inicial == num and menor == 0:
        menor = numero
    if numero < menor:
        menor = numero
    num -= 1
print(menor)
