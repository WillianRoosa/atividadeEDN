# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).
def classificar_idade():
    print("Classificador de Idade\n")
    while True:
        entrada = input("Digite a sua idade (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break
        try:
            idade = int(entrada)
            if idade < 0:
                print("Idade inválida. Por favor, insira uma idade positiva.")
            elif idade <= 12:
                print("Você é uma Criança.")
            elif idade <= 17:
                print("Você é um Adolescente.")
            elif idade <= 59:
                print("Você é um Adulto.")
            else:
                print("Você é um Idoso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
classificar_idade()

# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"
def calcular_imc():
    print("\nCalculadora de IMC\n")
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para peso e altura.")
calcular_imc()

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def conversor_temperatura():
    print("\nConversor de Temperatura\n")
    print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)\n")
    try:
        temp = float(input("Digite a temperatura a ser convertida: "))
        unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
        unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

        if unidade_origem == 'C':
            if unidade_destino == 'F':
                resultado = celsius_para_fahrenheit(temp)
            elif unidade_destino == 'K':
                resultado = celsius_para_kelvin(temp)
            else:
                print("Unidade de destino inválida.")
                return
        elif unidade_origem == 'F':
            if unidade_destino == 'C':
                resultado = fahrenheit_para_celsius(temp)
            elif unidade_destino == 'K':
                resultado = fahrenheit_para_kelvin(temp)
            else:
                print("Unidade de destino inválida.")
                return
        elif unidade_origem == 'K':
            if unidade_destino == 'C':
                resultado = kelvin_para_celsius(temp)
            elif unidade_destino == 'F':
                resultado = kelvin_para_fahrenheit(temp)
            else:
                print("Unidade de destino inválida.")
                return
        else:
            print("Unidade de origem inválida.")
            return

        print(f"A temperatura convertida é: {resultado:.2f} {unidade_destino}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para a temperatura.")
conversor_temperatura()

# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
def verificar_ano_bissexto():
    print("\nVerificador de Ano Bissexto\n")
    try:
        ano = int(input("Digite um ano para verificar se é bissexto: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro para o ano.")
verificar_ano_bissexto()