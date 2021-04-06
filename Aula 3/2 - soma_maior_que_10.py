"""Construa um Algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo

Leia(Valor1)

Leia(Valor2)

Real Valor1 , Valor2

Soma <- Valor1 + Valor2 

Se Soma > 10 então
  Imprima(Soma)
  
Fim-Se
"""

valor1 = float(input("Entre com um valor numérico: "))
valor2 = float(input("Entre com outro valor numérico:  "))

soma_valores = valor1 + valor2

if soma_valores > 10:
  print(soma_valores)
