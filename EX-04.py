import sys

def calcular_valor_hora_extra(horas_extras, salario_base):
    return horas_extras * salario_base * 0.015

def calcular_descontos(faltas, salario_base):
    return faltas * salario_base * 0.02

def calcular_bonus(cargo, bonus):
    if bonus.upper() == 'S':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    else:
        return 0

def cargo_final(cargo):
    if cargo == 1:
        return 'Gerente'
    elif cargo == 2:
        return 'Analista'
    elif cargo == 3:
        return 'Assistente'
    elif cargo == 4:
        return 'Estagiário'

nome = input('Digite seu nome: ')

cargo =  int(input('''
Informe seu cargo:
[1] Gerente
[2] Analista
[3] Assistente
[4] Estagiário
'''))
if cargo == 1:
    print('Cargo SALVO')
elif cargo == 2:
    print('Cargo SALVO')
elif cargo == 3:
    print('Cargo SALVO')
elif cargo == 4:
    print('Cargo SALVO')

else:
    print('Opção Inválida')
    sys.exit()

salario_base = float(input('Informe seu salário: R$'))

horas_extras = float(input('Informe a quantidade de horas extras trabalhadas no mês: '))
faltas = float(input('Informe o total de faltas no mês: '))

bonus = str(input('Recebeu salário bônus? [S] ou [N] '))
if bonus.upper() == 'S' or bonus.upper() == 'N':
    print('Resposta Válida!')
else:
    print('Resposta Inválida!')
    sys.exit()


total_valor_hora_extra = calcular_valor_hora_extra(horas_extras, salario_base)
total_desconto = calcular_descontos(faltas, salario_base)
recebeu_bonus = calcular_bonus(cargo, bonus)
acrescimos = total_valor_hora_extra + recebeu_bonus
salario_bruto = salario_base - total_desconto + total_valor_hora_extra + recebeu_bonus

print(f'''
========= PERFIL PESSOAL FINAL =========

NOME: {nome}
CARGO: {cargo_final(cargo)}
SALÁRIO BASE: R${salario_base}

BÔNUS: R${recebeu_bonus}
VALOR HORAS EXTRAS: R${total_valor_hora_extra}
TOTAL DE ACRÉSCIMOS: R${acrescimos}
TOTAL DE DESCONTOS: R${total_desconto}

SALÁRIO BRUTO: R${salario_bruto:.2f}

========================================
''')







