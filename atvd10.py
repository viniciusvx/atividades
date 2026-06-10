matriz = []

for l in range (3):
    linha = []
    print(f"LINHA: {l}")
    for c in range (3):
        print(f'COLUNA: {c}')
        valor = float(input(f"Informe o {c + 1}º valor: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for linha in range (len(matriz)):
    for coluna in range (len(matriz[linha])):
        soma += matriz[linha][coluna]

print(f"\nDiagonal principal")
print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])

print(f"\nSoma dos elementos")
print(soma)

print("\nMatriz")
print(matriz)