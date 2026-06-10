nome_aluno = input("Informe o nome do aluno: ")
soma = 0
for x in range (4):
  nota = float(input(f"Digite a {x+1}º nota do {nome_aluno}: "))
  soma += nota

media = soma/4

if media <5:
  print("Reprovado")

elif media >= 5 and media <=6.9:
  print("Recuperação")

elif media >= 7:
  print('Aprovado')