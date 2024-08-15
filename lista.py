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

