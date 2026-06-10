nomes = []

for i in range (5):
    nome = input(f"Informe o {i+1}º nome: ")
    nomes.append(nome)

for nome in nomes:
    print(f"Nome: {nome}")
    print('=' * 20)