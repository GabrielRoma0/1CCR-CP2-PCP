def pode_aprovar(idade, renda, valor):
    return idade >= 18 and valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    numerador = taxa * (1 + taxa) ** parcelas
    denominador = (1 + taxa) ** parcelas - 1
    return valor * (numerador / denominador)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

# Coleta de dados
nome = input('Qual seu nome? ')
idade = int(input('Quantos anos você tem? '))
renda = float(input('Qual sua renda mensal? R$ '))
valor = float(input('Quanto deseja de empréstimo? R$ '))
parcelas = int(input('Em quantas parcelas? (3 a 24) '))

if parcelas < 3 or parcelas > 24:
    print('Erro: número de parcelas deve ser entre 3 e 24.')
elif not pode_aprovar(idade, renda, valor):
    print(f'\nSinto muito, {nome}. Empréstimo NEGADO.')
    if idade <= 18:
        print('- Motivo: idade inferior a 18 anos.')
    if valor > renda * 20:
        print(f'- Motivo: valor excede o limite de R$ {renda * 20:.2f}.')
else:
    taxa = definir_taxa(parcelas)
    pmt = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(pmt, parcelas)
    juros = calcular_juros(total, valor)

    print(f'\nParabéns, {nome}! Empréstimo APROVADO.')
    print(f'Nome do cliente: {nome}')
    print(f'Valor financiado: R$ {valor:.2f}')
    print(f'Taxa de juros: {taxa:.0%} ao mês')
    print(f'Valor da parcela: R$ {pmt:.2f}')
    print(f'Valor total pago: R$ {total:.2f}')
    print(f'Total de juros pagos: R$ {juros:.2f}')