"""Escreva um Algoritmo que determine todos os divisores de um dado número
N."""
n = int(input("Digite um número: "))
contador = n
if n <= 0:
    print("Digite um  numero maior que 0")
else:
    while contador > 0:
        if n % contador == 0:
            print(contador)
        contador -= 1