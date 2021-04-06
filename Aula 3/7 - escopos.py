"""Construir um Algoritmo que leia um número e imprima se ele é igual a 5, a 200, a 400, se está no intervalo entre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores

Leia(Número)

inteiro Número

Se Número = 5 ou Número = 200 ou número = 400 então

  Imprima("Esse Número é igual a 5, 200 ou 400

Senão Se Número >= 500 e Número <=1000 então

  Imprima("Esse número está entre 500 e 1000")

Senão então 

  Imprima("Esse número não está em nenhum dos escopos")

Fim-Se
"""

n = int(input("Digite um número inteiro: "))

if n == 5 or n == 200 or n == 400:
  print("Esse número é igual a 5, 200 ou 400")
elif n >= 500 and n <= 1000:
  print("Esse Número está entre 500 e 1000")
else:
  print("O número não está em nenhum dos escopos")