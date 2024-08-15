import random
j = int(input("Digite o número de linhas da matriz A: "))
k = int(input("Digite o número de colunas da matriz A: "))
m = int(input("Digite o número de linhas da matriz B: "))
n = int(input("Digite o número de colunas da matriz B: "))
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