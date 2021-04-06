"""Construa um Algoritmo que determine(imprima) se um dado número N inteiro (recebido por meio do teclado) é Par ou Ímpar

Leia(Número)

inteiro Número

Se Número mod 2 = 0 então

  Imprima("Esse número é par")

Senão Se Número = 0 então

  Imprima("Esse número é neutro")

Senão então

  Imprima("Esse número é ímpar")

Fim-Se
"""

n = int(input("Digite um número: "))

if n % 2 == 0:
  print("Esse número é par")
if n == 0:
  print("Esse número é neutro")
else:
  print("Esse número é Impar")