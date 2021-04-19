"""Criar um Algoritmo que leia um número (NUM), e depois leia NUM números
inteiros e imprima o maior deles. Suponha que todos os números lidos serão
positivos

Leia(num)
maior = 0

Inteiro num, maior

Enquanto num > 0 faça
  Leia(numero)
  Se numero < 0 então
    Imprima("digite números maiores que zero")
    abandone
  if numero > maior:
    maior <- numero 
  num = num - 1
Imprima("o maior número digitado foi", maior)

"""
num = int(input("Digite um número: "))
maior = 0
while num > 0:
  numero = int(input("Digite um número para comparação: "))
  if numero < 0:
    print("digite números maiores que zero")
    exit()
  if numero > maior:
    maior = numero 
  num -= 1
print("o maior número digitado foi", maior)