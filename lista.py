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


  ## Questão 02

tamanho = int(input("Digite o tamanho das listas: "))
lista1 = []
lista2 = []

print("Digite os valores para a primeira lista: ")
for i in range(tamanho):
  lista1.append(int(input(f"Valor {i+1}: ")))
print("Digite os valores para a segunda lista: ")
for i in range(tamanho):
  lista2.append(int(input(f"Valor {i+1}: ")))

soma_pares_lista1 = 0
soma_impares_lista1 = 0
soma_pares_lista2 = 0
soma_impares_lista2 = 0
for numero in lista1:
  if numero % 2 == 0:
    soma_pares_lista1 += numero
  else:
    soma_impares_lista1 += numero
for numero in lista2:
  if numero % 2 == 0:
    soma_pares_lista2 += numero
  else:
    soma_impares_lista2 +=numero

print(f"Soma dos pares da lista 1: {soma_pares_lista1}")
print(f"Soma dos ímpares da lista 1: {soma_impares_lista1}")
print(f"Soma dos pares das lista 2: {soma_pares_lista2}")
print(f"Soma dos ímpares da lista 2: {soma_impares_lista2}")

if soma_pares_lista1 + soma_impares_lista1 > soma_pares_lista2 + soma_impares_lista2:
  print("A soma dos elementos da lista 1 é maior.")
elif soma_pares_lista1 + soma_impares_lista1 < soma_pares_lista2 + soma_impares_lista2:
  print("A soma dos elementos da lista 2 é maior.")
else:
  print("As somas dos elementos das listas são iguais.")


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


  ## Questão 04

tamanho = int(input("Digite a quantidade de elementos dos arrays: "))
lista1 = []
lista2 = []

print("Digite os valores para a primeira lista:")
for i in range(tamanho):
  lista1.append(int(input(f"Valor {i+1}: ")))
print("Digite os valores para a segunda lista:")
for i in range(tamanho):
  lista2.append(int(input(f"Valor {i+1}: ")))

lista_resultante = [0] * (tamanho * 2)
indice = 0
for i in range(tamanho):
  lista_resultante[indice] = lista1[i]
  indice += 1
  lista_resultante[indice] = lista2[i]
  indice += 1

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista resultante:", lista_resultante)

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

#Questão_13

A = [[0 for _ in range(3)] for _ in range(3)]
B = [[0 for _ in range(3)] for _ in range(3)]
C = [[0 for _ in range(3)] for _ in range(3)]

print("Digite os valores da matriz A (9 valores separados por espaço e com 3 linhas):")
for i in range(3):
  linha = input().split()
  for j in range(3):
    A[i][j] = int(linha[j])

print("Digite os valores da matriz B (9 valores separados por espaço e com 3 linhas):")
for i in range(3):
  linha = input().split()
  for j in range(3):
    B[i][j] = int(linha[j])

for i in range(3):
  for j in range(3):
    C[i][j] = max(A[i][j], B[i][j])

print("Matriz C:")
for i in range(3):
  print(*C[i])

#Questão_15
import random
m = int(input("Digite o número de linhas (m, entre 2 e 10): "))
n = int(input("Digite o número de colunas (n, entre 2 e 10): "))
if not 2 <= m <= 10 or not 2 <= n <= 10:
  print("As dimensões devem estar entre 2 e 10.")
  exit()
matriz = [[random.randint(100, 999) for _ in range(n)] for _ in range(m)]
print("Matriz:")
for linha in matriz:
  print(*linha)
maior_valor = matriz[0][0]
menor_valor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)
for i in range(m):
  for j in range(n):
    if matriz[i][j] > maior_valor:
      maior_valor = matriz[i][j]
      pos_maior = (i, j)
    if matriz[i][j] < menor_valor:
      menor_valor = matriz[i][j]
      pos_menor = (i, j)
print(f"Menor valor: {menor_valor} ({pos_menor[0]}, {pos_menor[1]})")
print(f"Maior valor: {maior_valor} ({pos_maior[0]}, {pos_maior[1]})")

#Questão_17
import random
j = int(input("Digite o número de linhas da matriz A (j): "))
k = int(input("Digite o número de colunas da matriz A (k): "))
m = int(input("Digite o número de linhas da matriz B (m): "))
n = int(input("Digite o número de colunas da matriz B (n): "))
min_valor = int(input("Digite o valor mínimo para os números aleatórios: "))
max_valor = int(input("Digite o valor máximo para os números aleatórios: "))
if k != m:
  print("O produto matricial não é possível, pois o número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")
  A = [[random.randint(min_valor, max_valor) for _ in range(k)] for _ in range(j)]
  for linha in A:
    print(*linha)
  B = [[random.randint(min_valor, max_valor) for _ in range(n)] for _ in range(m)]
  for linha in B:
    print(*linha)
  exit()
A = [[random.randint(min_valor, max_valor) for _ in range(k)] for _ in range(j)]
B = [[random.randint(min_valor, max_valor) for _ in range(n)] for _ in range(m)]
C = [[0 for _ in range(n)] for _ in range(j)]
for i in range(j):
  for l in range(n):
    for k in range(m):
      C[i][l] += A[i][k] * B[k][l]
print("Matriz A:")
for linha in A:
  print(*linha)
print("Matriz B:")
for linha in B:
  print(*linha)
print("Matriz Resultante:")
for linha in C:
  print(*linha)