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

    print(raizXey)
    print()
    print()
    return

xeyCalculator()

## Questão 05


# Parte 2 -



# Questão 02 - PT2

number = int(input("Digite um numero: "))

def shNumber(number):
    if ((number%2) == 0 ) :
        print("par")

    else:
        print("impar")

shNumber(number)



# Questão 03 - PT2

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

# Questão 04 - PT2

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


# Questão 06 - PT2
"""
booName = input("Digite o nome de usuario: ")
booAge = int(input("Digite a idade: "))
booConfirm = input("Você concorda com os termos de usuarios e confirma ser mairo de 18 ano(+18)? ")
def booleanAge(booName, booAge, booConfirm):
    if((booAge >= 18) and (booConfirm == "sim")):
        print("Verdade")


    elif((booAge < 18) and (booConfirm == "nao")):
        print("verdade")

    elif((booAge >= 18) and (booConfirm == "nao")):
        print("Falso")

    else:
        print("falso")

    return

booleanAge(booName, booAge, booConfirm)

"""

# Questão 07 - PT2
"""
print("Digite sua sexualidade, responda com as abreviações;")
inputSexuality = input("Feminino(F) / Masculino(M): ")

def sexualideSelect(inputSexuality):
    if (inputSexuality == "F"):
        print("Solteira(SO)")
        print("Casada(CS)")
        print("Divorciada(DA")
        print("Viúva(VV)")
        civilStateF = input("Digite a sua sexualidade conforme a abreviatura:")
        if (civilStateF == "CS"):
            ageMarried = int(input("Digite quantos anos de casada: "))
            print(ageMarried)
            print("Dado computado")
        else:
            print("Dado computado")
    else:
        print("Solteiro(SO)")
        print("Casado(CS)")
        print("Divorciado(DA")
        print("Viúvo(VV)")
        civilStateM = input("Digite a sua sexualidade conforme a abreviatura: ")
        print("Dado computado")

    return

sexualideSelect(inputSexuality)
"""

# Parte 03 -

# Questão 01 - PT3


