
"""Elabore um algoritmo que leia três valores lógicos e imprima o resultado da conjunção do
três.

Leia(valor1)
Leia(valor2)
Leia(valor3)

Cadeia de caractéres valor1, valor2, valor3
Se valor1 = "True" então:
    valor1 <- True
Senão se valor1 = "False" então:
    valor1 <- False
Senão então:
    Imprima("Digite True ou False")

Se valor2 = "True" então:
    valor2 <- True
Senão se valor2 = "False" então:
    valor2 <- Falset
Senão então:
    Imprima("Digite True ou False")

Se valor3 = "True" então:
    valor3 <- True
Senão se valor3 = "False" então:
    valor3 <- False
Senão então:
    Imprima("Digite True ou False")
"""

#Área de constantes e variáveis
valor1 = (input('Digite True or False: ')).strip().lower()
valor2 = (input('Digite True or False: ')).strip().lower()
valor3 = (input('Digite True or False: ')).strip().lower()

#Corpo do código
if valor1 == "true":
    valor1 = True
elif valor1 == "false":
    valor1 = False
else:
    print("Digite True ou False")
    exit()

if valor2 == "true":
    valor2 = True
elif valor2 == "false":
    valor2 = False
else:
    print("Digite True ou False")
    exit()

if valor3 == "true":
    valor3 = True
elif valor3 == "false":
    valor3 = False
else:
    print("Digite True ou False")
    exit()


conjuncao = valor1 and valor2 and valor3
print("a conjunção dos valores lógicos é", conjuncao)