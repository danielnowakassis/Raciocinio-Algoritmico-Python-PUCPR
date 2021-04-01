"""Elaborar um algoritmo para ler dois valores reais e multiplicar um pelo outro, imprimindo o resultado.

Leia(PrimeiroValor)

Leia(SegundoValor)

Inteiro PrimeiroValor,SegundoValor

Multiplicação <- PrimeiroValor * SegundoValor

Imprima(Multiplicação)
"""

#Área das variáveis
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
#Corpo do Código
multiplicacao_valores = primeiro_valor * segundo_valor
print("A multiplicação entre os 2 valores é", multiplicacao_valores)
