""""
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

    return

calculator()
"""
## Questão 02
##
"""
rad1 = float(input("Digite o raio do circulo: "))

def circulo():

    pi = 3.14159
    rad = ((rad1)/2)
    resp = (pi * rad)
    print(resp)

    return

circulo()
"""

##Questão 03
"""
sellerName = input("Nome do vendendor: ")
sellerCarSell = float(input("Quantidade de Carros Vendidos: "))
sellerSaleTotal = float(input("Valor Total das Vendas: "))

## Imprima o salario do vendedor
def sellerSalary():
    sellerSalaryBase = 500
    sellerComission = 50


    xCarComiss = (sellerComission * sellerCarSell) ## Comissão por cada carro vendido
    yCarRent = ((sellerSaleTotal/sellerCarSell)*0.05) ## Calculadora de porcentagem do valor total divido pelos carros
    xCarRent = (sellerCarSell*yCarRent) ## Calculadora de porcentagem total


    salary = (sellerSalaryBase+xCarComiss+xCarRent)


    print("Soldo salarial do: ", sellerName)
    print("Salario desse mes: R$", salary)


    return

sellerSalary()
"""

## Questão 05


