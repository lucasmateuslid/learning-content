import math

"""
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
"""
## Questão 05
"""
xAb = input("Digite o que você quiser para o valor de A: ")
yBa = input("Digite um numero inteiro para o valor de B: "))

def inverseValue():


    print(yba.replace(xAb, yba))
    ##Disponibilizar variaves que trocam valores entre si



    return

inverseValue()
"""



# Parte 2 -

# Questão 01 - PT2
"""
xplate = input("Qual o Prato escolhido?: ")
yplate = input("Qual a sobremesa escolhida?: ")
xdrink = input("Qual a bebida?: ")
def restorant():


    def pricipalPlate(xplate):
        xvegetary = ("Vegetariano", "vegetariano", "VEGETARIANO")
        xfish = ("PEIXE", "Peixe", "peixe")
        xchicken = ("FRANGO", "Frango", "frango")
        xmeat = ("CARNE", "Carne", "carne")


        if (xplate == xvegetary):
            xplateValue = 180
            print("Prato Registrado com Sucesso, Prossiga para sobremesa...")

        elif (xplate ==  xfish):
            xplateValue = 230
            print("Prato Registrado com Sucesso, Prossiga para sobremesa...")
        elif (xplate == xchicken) :
            xplateValue = 250
            print("Prato Registrado com Sucesso, Prossiga para sobremesa...")
        elif (xplate == xmeat):
            xplateValue = 350
            print("Prato Registrado com Sucesso, Prossiga para sobremesa...")
        else:
            print("O prato escolhido não consta no banco de dados")

        return (xplate)

    def dessertPlate(yplate):
        yAbacaxi = ("Abacaxi", "ABACAXI", "abacaxi")
        ySorvete = ("Sorvete", "SORVETE", "sorvete")
        yMousse = ("Mousse", "MOUSSE", "mousse")
        yMousseC = ("Mousse de Chocolate", "MOUSSE DE CHOCOLATE", "mousse de chocolate")

        if (yplate == "Abacaxi" or yplate == "ABACAXI" or yplate == "abacaxi") :
            yplateValue =   75
            print("A Sobremesa foi Registrada com Sucesso, Prossiga para a bebida...")
        elif (yplate == ySorvete) :
            yplateValue = 110
            print("A Sobremesa foi Registrada com Sucesso, Prossiga para a bebida...")
        elif (yplate == yMousse) :
            yplateValue = 170
            print("A Sobremesa foi Registrada com Sucesso, Prossiga para a bebida...")
        elif (yplate == yMousseC) :
            yplateValue = 200
            print("A Sobremesa foi Registrada com Sucesso, Prossiga para a bebida...")
        else :
            print("A sobremesa não consta no banco de dados")

        return (yplate)

    def drinkChoice(xdrink):
        zTea = ("Chá", "Cha", "CHÁ", "CHA", "chá", "cha")
        zJuice = ("Suco de Laranja", "SUCO DE LARANJA", "suco de laranja")
        zMelonJuice = ("Suco de Melão", "Suco de Melao", "SUCO DE MELÃO", "SUCO DE MELAO", "suco de melão", "suco de melao")
        zSoda = ("Refrigerante", "REFRIGERANTE", "refrigerante")

        if (xdrink == zTea):
            xdrinkValue = 20

        elif (xdrink == zJuice):
            xdrinkValue = 70

        elif (xdrink == zMelonJuice):
            xdrinkValue = 100

        elif (xdrink == zSoda):
            xdrinkValue = 65

        else:
            print("A bebida escolhida não consta no banco de dados")

        return (xdrink)

    iTotalKCal = (xdrinkValue + yplateValue + xplateValue)



    return()

    restorant()
"""

# Questão 02 - PT2
"""
number = int(input("Digite um numero: "))

def shNumber(number):
    if ((number%2) == 0 ) :
        print("par")

    else:
        print("impar")

shNumber(number)

"""

# Questão 03 - PT2
"""
dayNumber = int(input("Digite um numero de 1 a 7: "))
def dayNNumber(dayNumber):
    if (dayNumber == 1):
        print("Domingo")
    elif (dayNumber == 2):
        print("Segunda-Feira")

    elif (dayNumber == 3):
        print("Terça-Feira")

    elif (dayNumber == 4):
        print("Quarta-Feira")

    elif (dayNumber == 5):
        print("Quinta-Feira")

    elif (dayNumber == 6):
        print("Sexta-Feira")

    elif (dayNumber == 7):
        print("Sabado")

    else:
        print("Numero inferior ou superior a sequencia determinada...")

    return

dayNNumber(dayNumber)
"""
# Questão 04 - PT2
"""
vA = float(input("Digite um numero para A: "))
vB = float(input("Digite um numero para B: "))
vC = float(input("Digite um numero para C: "))

def rarestValue(vA,vB,vC):
    if ((vA > vB) and (vB > vC)):
        print("Os valores maiores são respectivamente;")
        print("A: ", vA)
        print("B", vB)
        print("C: ", vC)

    elif ((vA > vC) and (vC > vB)):
        print("Os valores maiores são respectivamente;")
        print("A: ", vA)
        print("C", vC)
        print("B: ", vB)

    elif((vB > vC) and (vC > vA)):
        print("Os valores maiores são respectivamente;")
        print("B: ", vB)
        print("C", vC)
        print("A: ", vA)

    elif((vB > vA) and (vA > vC)):
        print("Os valores maiores são respectivamente;")
        print("B: ", vB)
        print("A", vA)
        print("C: ", vC)

    elif((vC > vA) and (vA > vB)):
        print("Os valores maiores são respectivamente;")
        print("C: ", vC)
        print("A", vA)
        print("B: ", vB)

    elif((vC > vB) and (vB > vA)):
        print("Os valores maiores são respectivamente;")
        print("C: ", vC)
        print("B", vB)
        print("A: ", vA)

    else:
        print("Os valores são iguais", vA, vB, vC)
        
    return

rarestValue(vA, vB, vC)
"""
"""
# Questão 05 - PT2
xA = float(input("Digite um numero para A: "))
xB = float(input("Digite um numero para B: "))
xC = float(input("Digite um numero para C: "))


def lowestValue(vA, vB, vC):
    if ((xA > xB) and (xB > xC)):
        print("Os valores menores são respectivamente;")
        print("C: ", xC)
        print("B", xB)
        print("A: ", xA)

    elif ((xA > xC) and (xC > xB)):
        print("Os valores menores são respectivamente;")
        print("B: ", xB)
        print("C", xC)
        print("A: ", xA)

    elif ((xB > xC) and (xC > xA)):
        print("Os valores menores são respectivamente;")
        print("A: ", xA)
        print("C", xC)
        print("B: ", xB)

    elif ((xB > xA) and (xA > xC)):
        print("Os valores menores são respectivamente;")
        print("C: ", xC)
        print("A", xA)
        print("B: ", xB)

    elif ((xC > xA) and (xA > xB)):
        print("Os valores menores são respectivamente;")
        print("B: ", xB)
        print("A", xA)
        print("C: ", xC)

    elif ((xC > xB) and (xB > xA)):
        print("Os valores menores são respectivamente;")
        print("A: ", xA)
        print("B", xB)
        print("C: ", xC)

    else:
        print("Os valores são iguais", xA, xB, xC)

    return


lowestValue(xA, xB, xC)
"""

# Questão 06 - PT2

