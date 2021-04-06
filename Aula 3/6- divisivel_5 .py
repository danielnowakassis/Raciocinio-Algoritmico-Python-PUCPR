"""Escreva um Algoritmo que leia um número e informe se ele é ou não divisível por 5

Leia(Número)

inteiro Número 

Se Número mod 5 = 0 então
  Imprima("Esse número é divisível por 5")

Fim-Se
"""

n = int(input("Entre com um número inteiro:"))

if n % 5 == 0:
  print("Esse número é divisível por 5")