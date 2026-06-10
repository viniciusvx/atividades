soma = 0
cont = 0
while True:
    numero = int(input("Informe um numero: "))
    soma += numero
    cont += 1
    print("Deseja informar outro numero?")
    print("0 - Não | 1 - Sim")
    op = int(input("Informe a sua opção: "))
    print('=' * 50)

    if op not in (1,0):
        print("Opção inválida")
        continue
    
    if op == 0:
       print(f"A soma dos numeros é de: {soma}")
       media = soma/cont
       print(f"A media dos numeros é de: {media}")
       break