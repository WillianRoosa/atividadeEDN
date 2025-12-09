# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.
# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def calculadora():
    while True:
        print("Operações disponíveis: +, -, *, / | Digite 'sair' para encerrar")
        operacao = input("Digite a operação desejada: ")
        if operacao == 'sair':
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
            else:
                print("Operação inválida.")
                continue

            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
calculadora()

def calcular_media_turma():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, digite uma nota válida.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")
calcular_media_turma()

def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)


while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if senha_forte(senha):
        print("Senha forte!")
        break
    else:
        print(
            "Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
        
        
def analisar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.")
            else:
                impares += 1
                print(f"{numero} é ímpar.")
        except ValueError:
            print("Digite um número válido.")

    print(f"\nTotal de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
analisar_numeros()