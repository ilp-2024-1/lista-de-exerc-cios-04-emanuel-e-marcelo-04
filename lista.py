#Questão_01
numeros = []
for i in range(10):
  entrada = int(input("digite um numero inteiro e aperte enter (dez vezes):"))
  numeros += [entrada]
pares = 0
for entrada in numeros:
  if entrada % 2 == 0 and entrada != 0:  # Verifica se o número é par e diferente de zero
    pares += 1
if pares > 0:
  print("Qtd valores par:", pares)
else:
  print("Não há valores pares")

#Questão_03

numeros = []
for i in range(10):
  entrada = int(input("digite um numero inteiro e aperte enter (dez vezes):"))
  numeros += [entrada]
pares = 0
for entrada in numeros:
  if entrada % 2 == 0 and entrada != 0:  # Verifica se o número é par e diferente de zero
    pares += 1
if pares > 0:
  print("Quantidade de valores par:", pares)
else:
  print("Não há valores pares")

#Questão_05

qnt_valores = int(input("Digite a quantidade de valores: "))
menor = 0
maior = 0
soma = 0

valor = int(input(f"Digite o valor 1: "))
menor = valor
maior = valor
soma = valor

for i in range(1, qnt_valores):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    soma += valor
media = soma / qnt_valores
print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média aritmética:", media)

#Questão_07

qnt_valores = int(input("Digite a quantidade de valores: "))
menor = 0
maior = 0
soma = 0

valor = int(input(f"Digite o valor 1: "))
menor = valor
maior = valor
soma = valor

for i in range(1, qnt_valores):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    soma += valor
media = soma / qnt_valores
print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média aritmética:", media)

#Questão_09

texto = input("Digite o texto: ")
palavras = texto.split()
contagem = {}
for palavra in palavras:
  nova = ''
  for letra in palavra:
    if letra not in ".,!?;:-":
      nova += letra.lower()
  if nova in contagem:
    contagem[nova] += 1
  else:
    contagem[nova] = 1
primeira_vez = True
for palavra in contagem:
  contagem = contagem[palavra]
  if primeira_vez:
    primeira_vez = False
    print(f"{palavra}={contagem}", end="")
  else:
    print(f"; {palavra}={contagem}", end="")

#Questão_11

m = int(input("Digite o número de linhas (m): "))
n = int(input("Digite o número de colunas (n): "))
matriz = [[0 for _ in range(n)] for _ in range(m)]
print("Digite os valores da matriz (", m * n, "valores separados por espaço):")
entrada = input()
valores = map(int, entrada.split())
k = 0
for i in range(m):
  for j in range(n):
    matriz[i][j] = next(valores)
    k += 1
print("Matriz:")
for linha in matriz:
  print(*linha)
print("\nSoma de cada linha:")
for i in range(m):
  soma_linha = sum(matriz[i])
  print(*matriz[i], "=", soma_linha)