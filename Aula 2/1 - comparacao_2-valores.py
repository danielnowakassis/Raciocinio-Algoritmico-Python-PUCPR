"""
Elabore um algoritmo que leia dois valores inteiros e retorne se a afirmativa de que o
primeiro valor é maior ou igual ao segundo é falsa ou verdadeira.

Leia(Valor1)

Leia (Valor2)

Inteiros Valor1, Valor2


Booleano = Valor1 ≥ Valor2

Imprima(Booleano)
"""


#Area das constantes e variáveis
valor1 = int(input("Entre com um valor inteiro: "))
valor2 = int(input("Entre com outro valor inteiro: "))

#corpo do código
booleano = valor1 >= valor2

print('O primeiro valor é maior que o segundo é', booleano)