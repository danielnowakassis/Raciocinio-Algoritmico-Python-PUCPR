"""Escreva um algoritmo que leia e imprima 10 números fornecidos pelo usuário. No entanto, se o usuário entrar com o número 6,
interrompa o processo e Fnalize a execução 

Contador = 1 

Inteiro Contador

Enquanto Contador < 10 faça
    Leia(Número_Usuário)
    Se Número_Usuário ≠ 6 então
        abandone
    Contador = Contador + 1

"""


#corpo do código
n = 1
while n < 10:
    user = int(input("Digite um número: "))
    if user == 6:
        break
    n += 1  

