soma = 0
for x in range (5):
    numero = float(input(f"Informe o {x+1}º numero: "))
    soma += numero

print(f"A soma dos numeros é de: {soma}")
media = soma/5
print(f"A media dos numeros é de: {media}")