faturamento_estados = [
  {
    "estado": "SP",
    "porcentagem": 0,
    "valor": 67836.43,
  },
  {
    "estado": "RJ",
    "porcentagem": 0,
    "valor": 36678.66,
  },
  {
    "estado": "MG",
    "porcentagem": 0,
    "valor": 29229.88,
  },
  {
    "estado": "ES",
    "porcentagem": 0,
    "valor": 27165.48,
  },
  {
    "estado": "Outros",
    "porcentagem": 0,
    "valor": 19849.53,
  },
]

faturamento_total = 0

for faturamento in faturamento_estados:
  faturamento_total += faturamento["valor"]

for faturamento in faturamento_estados:
  faturamento["porcentagem"] = (faturamento["valor"] / faturamento_total) * 100

for faturamento in faturamento_estados:
  print(faturamento["estado"])
  print(f'{faturamento["porcentagem"]:.2f}%')
  print("\n")