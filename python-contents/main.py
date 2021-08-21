import math


## Questão 01
print("Questão 01 - Calculadora de Média ponderada de Notas!")
print()

## Calculator media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

def calculator():
    an1 = (n1 * 2)
    an2 = (n2 * 3)
    an3 = (n3 * 4)
    an4 = (n4 * 6)
    podnpes = (2+3+4+6)
    ng = ((an1+an2+an3+an4)/podnpes)
    print(ng)
    print()
    print()

    return

calculator()

## Questão 02

print("Questão 02 - Calculo do radio de uma circuferencia" )
print()

rad1 = float(input("Digite o raio do circulo: "))

def circulo():

    pi = 3.14159
    rad = ((rad1)/2)
    resp = (pi * rad)
    print(resp)
    print()
    print()
    return

circulo()

##Questão 03

print("Questão 03 - Calculo salarial de Vendedor de Carros")
print()

sellerName = input("Nome do vendendor: ")
sellerCarSell = float(input("Quantidade de Carros Vendidos: "))
sellerSaleTotal = float(input("Valor Total das Vendas: "))

## Imprima o salario do vendedor
def sellerSalary():



    xCarComiss = (50 * sellerCarSell) ## Comissão por cada carro vendido
    yCarRent = ((sellerSaleTotal/sellerCarSell)*0.05) ## Calculadora de porcentagem do valor total divido pelos carros
    xCarRent = (sellerCarSell*yCarRent) ## Calculadora de porcentagem total


    salary = (500+xCarComiss+xCarRent)


    print("Soldo salarial do: ", sellerName)
    print("Salario desse mes: R$", salary)
    print()
    print()
    return

sellerSalary()

## Questão 04
x1 = float(input("Valor do x1: "))
x2 = float(input("Valor do x2: "))
y1 = float(input("Valor do x3: "))
y2 = float(input("Valor do x4: "))
def xeyCalculator():

    resp1 = (((x2 - x1 ) ** 2) + ((y2 - y1 ) ** 2))
    raizXey = math.pow(resp1, 1/2)

    print()
    print()
    print()
    return

xeyCalculator()

## Questão 05

xAb = input("Digite o que você quiser para o valor de A: ")
yBa = int(input("Digite um numero inteiro para o valor de B: "))

def inverseValue(xAb, yBa):

    return