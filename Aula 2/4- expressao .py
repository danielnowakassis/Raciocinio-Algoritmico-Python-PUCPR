"""Dada as variáveis lógicas e a expressão abaixo, desenvolva um algoritmo que imprima se o
valor resultante da expressão será verdadeiro o falso.

Lógicos Valor_A, Valor_B, Valor_C, Valo_D, Valor_E, Expressão

Valor_A <-Falso

Valor_B <-Verdadeiro

Valor_C <- Verdadeiro

Valor_D <- Falso

Valor_E <- Falso

Expressão <- (Valor_A ou Valor_B) e (Valor_D e Valor_C) ou nãoValor_E
"""

#Área de constantes e variáveis
valor_A = False
valor_B = True
valor_C = True
valor_D = False
valor_E = False

#Corpo do codigo
expressao = (valor_A or valor_B) and (valor_D and valor_C) or not valor_E
print(expressao)