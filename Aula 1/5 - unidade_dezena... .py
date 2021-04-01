"""Elaborar um algoritmo a app que leia um número inteiro de quatro dígitos e
imprima, separadamente, a unidade, a dezena, a centena e a milhar.

Leia(numero)

Inteiro Número

Unidade <- Número % 10

Dezena <- (Número mod 100 - Unidade) / 10

Milhar <- Número div 1000

Centena <- numero // 100 - milhar * 10


Imprima(Unidade, Dezena, Centena, Milhar)
"""

#Área das variáveis
numero = int(input("digite um número de 4 digitos: "))

#Corpo do Código
unidade = numero % 10
dezena = int((numero % 100 - unidade) / 10)
milhar = numero // 1000
centena = numero // 100 - milhar * 10 

print(unidade, "dezena:", dezena, "centena:", centena, "milhar:", milhar)