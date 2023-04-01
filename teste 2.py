num1 = 0
num2 = 1

finder = int(input('Digite um número: '))

while True:
  aux = num2
  num2 = num1 + num2
  num1 = aux
  if num2 == finder:
      print("Pertence a sequencia de Fibonacci")
      break
  if finder < num2:
      print("Não pertence a sequencia de Fibonacci")
      break
