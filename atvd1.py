while True:
    nome = input("Informe o seu nome: ")

    try:
        idade = int(input(f"Olá,{nome} Informe a sua idade: "))

        if idade < 0:
            print("Idade inválida")
            continue
            
    except ValueError:
        print("Digite apenas numeros") 
        continue

    cidade = input("Informe o nome da sua cidade: ")
    break

print(f"NOME: {nome}")
print(f'IDADE: {idade}')
print(f'CIDADE: {cidade}')