"""1) Criar um Algoritmo que imprima todos os números de 1 até 100, inclusive, e
a soma de todos eles. 

n <- 100
soma <- 0
Inteiros n, soma

Enquanto n > 0 faça
    Imprima(n)
    soma <- soma + n 
    n <- n - 1
Imprima("Soma de todos os números é", soma)

"""
#corpo do código 
n = 100
soma = 0
while n > 0:
    print(n)
    soma = soma + n 
    n -= 1
print("Soma de todos os números é", soma)