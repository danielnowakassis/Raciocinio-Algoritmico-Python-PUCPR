"""Elaborar um algoritmo a app para calcular e imprimir a raiz quadrada de um
número inteiro e positivo lido.

Leia(Valor)

Inteiro Valor

Raiz <- Valor ** (1/2)

Imprima(Valor)
"""

#importar biblioteca
import math 

#Área das variáveis
numero = int(input("Digite um numero positivo: "))

#Corpo do Código
raiz = math.sqrt(numero)
print("A raiz quadrada desse número é",raiz)

#ou
#Área das variáveis
numero = int(input("Digite um numero positivo: "))

#Corpo do Código
raiz = numero ** (1/2)
print("A raiz quadrada desse número é",raiz)