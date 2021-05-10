"""1) Criar um Algoritmo que imprima a soma entre dois valores quaisquer
digitados pelo usuário. Utilizar uma função para fazer a soma.

Inteiro Soma(Número1, Número2)
    Soma <- Número1 + Número2
    retorne Soma

Leia(Número_teclado1)
Leia(Número_teclado2)
Imprima(Soma(Número_teclado1, NNúmero_teclado2))
"""
#Corpo do código
def soma(a, b):
  soma = a + b
  return soma

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
print(soma(num1, num2))


"""
2) Criar um Algoritmo que apresenta a divisão entre dois valores quaisquer
digitados pelo usuário. Utilizar uma função para fazer a divisão.

Real Divisão(Número1, Número2)
    Divisão <- Número1 / Número2
    retorne Divisão

Leia(Número_teclado1)
Leia(Número_teclado2)
Imprima(Divisão(Número_teclado1, Número_teclado2))
"""
#Corpo do código
def divisao(a, b):
  divisao = a / b
  return divisao

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 == 0 or num2 == 0:
  print("Divisão por zero é indefinida") 
print(divisao(num1, num2))


"""
3) Criar um Algoritmo que, a partir dos valores de peso (em kg) e de altura
(em m) de uma pessoa digitados pelo usuário, imprima o IMC daquela
pessoa e também sua classificação conforme a diretriz de saúde abaixo.
Utilizar duas funções: uma para calcular e retornar o IMC, e outra para
obter e retornar à classificação de peso do indivíduo 

Inteiro IMC(Peso, Altura)
    IMC <- Peso / (Altura ** 2)
    retorne IMC

Leia(PesoPessoa)
Leia(AlturaPessoa) 
Se IMC(PesoPessoa, AlturaPessoa) > 0 and IMC(PesoPessoa, AlturaPessoa) <= 18.5 então
  print("Você está abaixo do peso")
if IMC(PesoPessoa, AlturaPessoa) > 18.5 and IMC(PesoPessoa, AlturaPessoa) < 25 então
  print("Você tem um peso saudável")
if IMC(PesoPessoa, AlturaPessoa) > 25 então
  print("Você está acima do peso")
else:
  print("digite um valor valido")
""" 

def imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

peso_pessoa = float(input("Digite seu peso(em Kg) : "))
altura_pessoa = float(input("Digite sua altura(em m) : "))
if imc(peso_pessoa, altura_pessoa) > 0 and imc(peso_pessoa, altura_pessoa) <= 18.5:
  print("Você está abaixo do peso")
if imc(peso_pessoa, altura_pessoa) > 18.5 and imc(peso_pessoa, altura_pessoa) < 25:
  print("Você tem um peso saudável")
if imc(peso_pessoa, altura_pessoa) > 25:
  print("Você está acima do peso")
else:
  print("digite um valor valido")

"""
4) Cria r um Algoritmo que , a partir dos coeficien tes ʻaʼ, ʻbʼ e ʻcʼ de uma equação do 2º. grau digitados pelo usuário, apresenta na tela quantas raízes reais
existem e quais são seus valores. Utilizar uma única função para resolver o
problema. Obs.: utilize a função str() para converter um número em texto. 
# variaveis
real a,b,c
caracter result
 
imprima("entre com o valor de a:")
leia(a)
imprima("entre com o valor de b:")
leia(b)
imprima("entre com o valor de c:")
leia(c)
 
se a == 0 então
  imprima("não é uma equação do segundo grau")
senão
  imprma(segundo_grau(a,b,c))
fim se
"""
#funcao 
def segundo_grau(a,b,c) :
  delta = (b2 - 4 * a * c)
  if delta < 0 :
    resultado = "raiz imaginária"
  elif delta == 0 :
    x1 = (-b/2*a)
    resultado = "x1 = x2 = " +  str(x1)
  else :
    x1 = (-b + (delta * 0.5))/ (2 * a)
    x2 = (-b - (delta * 0.5))/ (2 * a)
    resultado = "x1 = " +  str(x1) + " " + "x2 = " + str(x2)
  return resultado

# variaveis

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))
c = float(input("entre com o valor de c:"))

if a == 0 :
  print("não é uma equação do segundo grau")
else :
  print(segundo_grau(a,b,c))


print("fim")
""" 
5) Criar um Algoritmo que calcula e apresenta na tela a média entre N valores
inteiros de idade (em anos) lidos do usuário. Utilize uma única função para
calcular e retornar a média. 
 
NúmeroPessoas = int(input("De quantas pessoas deseja saber a media entre elas? "))
NúmeroPessoasInicial = NúmeroPessoas
Enquanto NúmeroPessoas > 0 faça
    Leia(Idade)
    soma <- soma + Idade
    n <- n - 1
Real Média(soma, NúmeroPessoasInicial):
  Média = soma / NúmeroPessoasInicial
  retorne Média

Imprima(Média(Idade))
"""
n = int(input("De quantas pessoas deseja saber a media entre elas? "))
n_inicial = n
while n > 0:
    idade = int(input("Qual a idade da pessoa?"))
    soma = soma + idade
    n -= 1
def media(soma ,n_inicial):
  media = soma / n_inicial
  return media

print("A media das idades dessas pessoas é", media(soma, n_inicial))

"""
6) Criar um Algoritmo que, a partir de dois números quaisquer e também de
uma operação aritmética (+, -, *, /), digitados pelo usuário, apresenta na tela o
resultado do cálculo solicitado. Utilize quatro funções, uma para cada função
matemática. Exemplos de execução


Real soma(n1, n2):
  soma <-  n1 + n2
  print(soma)
Real sub(n1, n2):
  sub <- n1 - n2
  Imprima(sub)
Real mult(n1, n2):
  mult <-  n1 * n2
def div(n1, n2):
  if n1 = 0 ou n2 = 0:
    print("Divisão por zero é indefinida")
  else:
    div = n1 / n2
    Imprima(div)


Leia(num1) 
Leia(operação)
Leia(num2)

Se operação == "+" então
  soma(num1, num2)
Senão se operação == "-" então
  sub(num1, num2)
Senão se operação == "*" então
  mult(num1, num2)
Senão se operação == "/" então
  div(num1, num2)
Senão:
  Imprima("Digite um valor lógico válido")
"""


def soma(n1, n2):
  soma = n1 + n2
  print(soma)
def sub(n1, n2):
  sub = n1 - n2
  print(sub)
def mult(n1, n2):
  mult = n1 * n2
def div(n1, n2):
  if n1 == 0 or n2 == 0:
    print("Divisão por zero é indefinida")
  else:
    div = n1 / n2
    print(div)


num1 = float(input("Digite um número"))
operacao = str(input("Digite o operador lógico [+, -, *, /]"))
num2 = float(input("Digite outro número:"))

if operacao == "+":
  soma(num1, num2)
elif operacao == "-":
  sub(num1, num2)
elif operacao == "*":
  mult(num1, num2)
elif operacao == "/":
  div(num1, num2)
else:
  print("Digite um valor lógico válido")