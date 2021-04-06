"""Escreva um Algoritmo que leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo

Leia(Número)

inteiro Número

Se Número >= 0 então

  Imprima(Número ** (1/2))
  
Senão então

  Imprima(Número ** 2)

Fim-Se
"""

n = int(input("Digite um número: "))

if n >= 0:
  print("A raiz quadrada do número é ",n ** (1/2))
else:
  print("Esse número ao quadrado é", n ** 2)