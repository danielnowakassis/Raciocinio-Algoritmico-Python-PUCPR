"""Elabore um algoritmo que leia duas cadeias de caracteres e imprima se a igualdade é falsa ou
verdadeira.

Leia(Cadeia1)
Leia(Cadeia2)

Cadeias_de_caracteres Cadeia1, Cadeia2

Comparacao <- Cadeia1 = Cadeia 2

Imprima(Comparacao)
"""

#Área de constantes e variáveis
cadeia1 = str(input('Digite algo: '))
cadeia2 = str(input('Digite algo novamente: '))

#Corpo do código
comparacao = cadeia1 == cadeia2 
print("O que você entrou primeiro é igual ao que você entrou depois? ", comparacao)