"""Escreva um algoritmo para determinar se um dado número N é POSITIVO, NEGATIVO OU NULO

Leia(Número)

Real Número

Se Número > 0 então

  Imprima("Esse número é positivo")

Senão Se Número = 0 então

  Imprima("Esse número é nulo")

Senão então

  Imprima("Esse número é negativo")

Fim- Se
"""

n = float(input("Digite um número: "))

if n > 0:
  print("Esse número é positivo")
elif n == 0:
  print("Esse número é neutro")
else:
  print("Esse número é negativo")