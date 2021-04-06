"""
GRUPO 12: 

Daniel Nowak Assis

Gabrielle Louise Ferreira de Melo

Thomas Rempel

Mikael da Silva

1) Uma P.A. (progressão aritmética) fica
determinada pela sua razão (r) e pelo primeiro
termo(a1). Escreva um Algoritmo e,
posteriormente, uma app em Python que seja
capaz de determinar qualquer termo de uma P.A.,
dado a razão e o primeiro termo, que serão lidos
do teclado.

Leia(PrimeiroTermo)

Leia(Razão)

Leia(EnésimoTermo)

inteiro PrimeiroTermo, Razão, EnésimoTermo

ProgressãoAritmética <- PrimeiroTermo + (EnésimoTermo - 1) * Razão

Imprima(ProgressãoAritmética)
"""

#Área das variáveis
primeiro_termo = int(input("Entre com o primeiro termo da PA: "))
razao = int(input("entre com a razão da PA: "))
enesimo= int(input("Qual termo deseja saber? "))

#Corpo do código
pa = primeiro_termo + (enesimo - 1) * razao

print("O termo n*", enesimo, " da PA com razao", razao, "com primeiro termo", primeiro_termo, "é", pa)

"""2) Considere que o número de uma placa de
veículo é composto por quatro algarismos.
Construa um Algoritmo e, posteriormente, uma
app em Python que leia este número e apresente
o algarismo correspondente à casa das centenas.

Leia(NúmeroPlaca)

inteiro NúmeroPlaca

CentenaPlaca <- (Placa div 100) - ((Placa div 1000) * 10)

Imprima(CentenaPlaca)
"""

#Área das variáveis
placa = int(input("Entre com o número da placa de 4 digitos: "))

#Corpo do Código
centena_placa = (placa // 100) - ((placa // 1000) * 10)
  
print("O algarismo correspondente à casa das centenas do número", placa,"é", centena_placa)

"""Escreva um Algoritmo que leia dois números
reais e imprima a média aritmética entre esses
dois valores com a seguinte mensagem “MEDIA”
antes do resultado.

Leia(PrimeiroNúmero)

Leia(SegundoNúmero)

Média <- (PrimeiroNúmero + SegundoNúmero) / 2

Imprima("MEDIA")

Imprima(Média)
"""

#Área das variáveis
primeiro_numero = float(input("Entre com um número: "))
segundo_numero = float(input("Entre com outro número "))

#Corpo do Código 
media = (primeiro_numero + segundo_numero) / 2

print("MEDIA", media)

"""Construa uma Algoritmo e, posteriormente, uma app em
Python para realizar a soma de uma P.A . de n termos, com o
primeiro a1 e o último an, sendo n, a1 e an lidos do teclado

Leia(PrimeiroTermo)

Leia(ÚltimoTermo)

Leia(EnésimoTermo)

inteiro PrimeiroTermo, UltimoTermo, EnésimoTermo

SomaTermos = ((PrimeiroTermo + ÚltimoTermo) * EnésimoTermo) / 2 

Imprima(SomaTermos)
"""

#Área das variáveis
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
ultimo_termo = int(input("Digite o último termo da PA: "))
n = int(input("Digite o enésimo ultimo termo da PA: "))

soma_termos = ((primeiro_termo + ultimo_termo) * n) / 2 

print("A soma de termos da PA até o termo número", n, "é", soma_termos)