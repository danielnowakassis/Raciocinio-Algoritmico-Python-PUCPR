A = True
B = False
C = False
D = True
E = True
F = False

Resultado = (A or B) and (not C) and (D and E) or (not F)
print(Resultado)

#2

LimiteSuperiorMáximo = 20
Divisor =  5
ContadorNumérico = 1

while ContadorNumérico <= LimiteSuperiorMáximo:
        if ContadorNumérico % Divisor == 0:
              print(ContadorNumérico,", ")
        ContadorNumérico = ContadorNumérico + 2

#if (valorLido % 2) = 0:
#   print("erro")

"""Desenvolva uma código em Python que determine todos os divisores de um dado número N inteiro lido do teclado, no intervalo entre 1 e N.
"""

"""Escreva um Algoritmo que determine todos os divisores de um dado número
N."""
n = int(input("Digite um número: "))
contador = n
if n <= 0:
    print("Digite um  numero maior que 0")
else:
    while contador > 0:
        if n % contador == 0:
            print(contador)
        contador -= 1
#(número mod 10) div 10
VolorCalculado  = (27 % 10) // 10
print(VolorCalculado)


lista = []

for i in range(200):
    if i % 2 == 0:
        lista.append(i)
print(lista)
print(len(lista))
lista = []

"""Desenvolva uma código em Python que calcule a seguinte séria para N termos. N deve ser lido do teclado. 
S = 2/N + 4/(N-1) + 6/(N-2) + 8/(N-3) + ... + (2*N)/1
"""
#Área das variáveis
n = int(input("digite o valor de n: "))
soma_dividendo = 2
i=0
serie = 0
#Corpo do Código
while n - i > 0:
    serie = serie +  ((i + soma_dividendo) / (n - i))
    soma_dividendo += 1
    i += 1
print("Essa serie, com n igual a", n, "é igual a", serie)












