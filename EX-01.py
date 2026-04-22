codigo_origem = int(input("Digite o código de origem da carga (de 1 a 5): "))
peso_carga_ton = float(input("Digite o peso da carga do caminhão em toneladas: "))
codigo_carga = int(input("Digite o código da carga do caminhão (de 10 a 40): "))

def conversao_peso(peso_carga_ton):
    peso_carga_kg = peso_carga_ton * 1000
    return peso_carga_kg

peso_carga_kg = conversao_peso(peso_carga_ton)


if codigo_carga <= 20:
    preco_carga_final = peso_carga_kg * 100
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_carga_final = peso_carga_kg * 250
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_carga_final = peso_carga_kg * 340

if codigo_origem == 1:
    preco_imposto = preco_carga_final * 0.35
elif codigo_origem == 2:
    preco_imposto = preco_carga_final * 0.25
elif codigo_origem == 3:
    preco_imposto = preco_carga_final * 0.15
elif codigo_origem == 4:
    preco_imposto = preco_carga_final * 0.05
elif codigo_origem == 5:
    preco_imposto = 0

valor_total = preco_carga_final + preco_imposto

print(f"Peso da carga em kg: {peso_carga_kg} kg")
print(f"Preço da carga: R$ {preco_carga_final}")
print(f"Valor do imposto: R$ {preco_imposto}")
print(f"Valor total (carga + imposto): R$ {valor_total}")
