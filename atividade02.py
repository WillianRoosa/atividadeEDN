# 1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

#* Valor em reais: R$ 100.00
#* Taxa do dólar: R$ 5.20
#* Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$ {:.2f}".format(valor_reais))
print("Valor da conversão em dólares: $ {:.2f}".format(valor_dolar))
print("Valor da conversão em euros: € {:.2f}".format(valor_euro))

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Porcentagem de desconto: {}%".format(porcentagem_desconto))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final: R$ {:.2f}".format(preco_final))

# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Notas do aluno:")
print("Nota 1: {:.2f}".format(nota1))
print("Nota 2: {:.2f}".format(nota2))
print("Nota 3: {:.2f}".format(nota3))
print("Média final: {:.2f}".format(media))

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros
consumo_medio = distancia_percorrida / combustivel_gasto
print("Distância percorrida: {} km".format(distancia_percorrida))
print("Combustível gasto: {} litros".format(combustivel_gasto))
print("Consumo médio: {:.2f} km/l".format(consumo_medio))