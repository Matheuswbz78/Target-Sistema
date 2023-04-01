import json

with open('dados.json') as dados:
    faturamento = dados.read()
faturamento = json.loads(faturamento)

menor_valor = maior_valor = float(faturamento[0]["valor"])
menor_valor_dia = maior_valor_dia = media = dias_acima_da_media = 0
valores_dia = []

for faturamento_dia in faturamento:
    dia = int(faturamento_dia["dia"])
    valor = float(faturamento_dia["valor"])
    valores_dia.append(valor)
    media += valor
    if menor_valor > valor:
        menor_valor = valor
        menor_valor_dia = dia
    elif maior_valor < valor:
        maior_valor = valor
        maior_valor_dia = dia

media = media / dia
for val in valores_dia:
    if val > media:
        dias_acima_da_media += 1

print(menor_valor)
print(menor_valor_dia)
print("\n")
print(maior_valor)
print(maior_valor_dia)
print("\n")
print(media)
print("\n")
print(dias_acima_da_media)
