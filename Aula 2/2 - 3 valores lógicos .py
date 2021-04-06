
"""Elabore um algoritmo que leia três valores lógicos e imprima o resultado da conjunção do
três.


Imprima("Digite Verdadeiro ou Falso")

Leia(ValorLógico1)

Imprima("Digite Verdadeiro ou Falso")

Leia(ValorLógico2)]

Imprima("Digite Verdadeiro ou Falso")

Leia(ValorLógico3)

Cadeia de caracteres ValorLógico1, ValorLógico2, ValorLógico3



Se ValorLógico1 = "Verdadeiro" então

  ValorLógico1 <- Verdadeiro

Senão Se ValorLógico1 = "Falso" então

  ValorLógico1 <- Falso

Senão então

  Imprima("Digite Verdadeiro ou Falso)

Fim-Se

Se ValorLógico1 = "Verdadeiro" então

  ValorLógico1 <- Verdadeiro

Senão Se ValorLógico1 = "Falso" então

  ValorLógico2 <- Falso

Senão então

  Imprima("Digite Verdadeiro ou Falso)

Fim-Se
  
Se ValorLógico1 = "Verdadeiro" então

  ValorLógico1 <- Verdadeiro

Senão Se ValorLógico1 = "Falso" então

  ValorLógico2 <- Falso

Senão então

  Imprima("Digite Verdadeiro ou Falso)

Fim-se


Imprima(ValorLógico1 e ValorLógico2 e ValorLógico3)

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