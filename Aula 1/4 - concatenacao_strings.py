"""Elaborar um algoritmo a app para ler duas cadeias de carecteres e imprimir
a concatenação de ambas.

Leia(PrimeiroCaracter)

Leia(SegundoCaracter)

Inteiro PrimeiroCaracter,SegundoCaracter

Concatenação <- PrimeiroValor ** 2

Imprima(Concatenacao)
"""

#Área das variáveis
primeiro_caracter = str(input('insira um caracter: '))
segundo_caracter = str(input('insira outro caracter: '))

#Corpo do Código
concatenacao = primeiro_caracter + segundo_caracter
print("A concatenação entre esses 2 caracteres é ", concatenacao)

