alunos = []
anos = ('1', '2', '3', '4', '5', '6', '7', '8', '9', "1°", "2°", "3°")
turmas = ("A", "B", "C")
quantidade_alunos = 0
def cadastrar_aluno():
    while True:
        print("\n---CADASTRAR ALUNO--- ")
        aluno = {}

        aluno['nome'] = input("Informe o nome do aluno: ")

        try:
            aluno['idade'] = int(input("Informe a idade do aluno: "))
        except ValueError:
            print("Dados inválidos")
            continue

        if aluno["idade"] < 0:
            print("A idade não pode ser menor que 0")
            continue

        aluno['turma'] = input(
            f"Informe a série/turma do {aluno['nome']} : "
)
        
        aluno['nota'] = []

        alunos.append(aluno)
        cadastrar_aluno += 1

        op = input("Deseja cadastrar novamente? [S][N] ").upper()

        if op == "N":
            print("Cadastro realizado!")
            break


def lancar_nota():
    while True:
        print("\n---LANÇAR NOTAS--- ")
        nome_busca = input("Informe o nome do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno['nome'].lower() == nome_busca.lower():

                encontrado = True
                soma = 0

                for c in range(4):
                    nota = float(input(f"Informe a {c+1}ª nota do {aluno['nome']}: "))
                    if nota > 10 and nota <0:
                        print("Nota inválida!")
                        continue
                    aluno['nota'].append(nota)
                    soma += nota

                aluno['media'] = soma / 4

                print("Notas lançadas com sucesso!")
                break

        if not encontrado:
            print("Aluno não encontrado")
            continue

        op = input("Deseja lançar notas novamente? [S][N] ").upper()

        if op == "N":
            print("Lançamento de notas finalizado!")
            break


def consultar_aluno():
    print("\n---CONSULTAR ALUNO--- ")
    nome_busca = input("Informe o nome do aluno que deseja: ")
    encontrado = False

    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca.lower():
            encontrado = True

            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Ano: {aluno['ano']} ano")
            print(f"Turma: {aluno['turma']}")
            print(f"Notas: {aluno['nota']}")
            print(f"Média: {aluno['media']}")

            if aluno['media'] >=7:
                print("Aprovado!")

            elif aluno['media'] >= 5:
                print("Recuperação")

            else:
                print("Reprovado")

    if not encontrado:
        print("Aluno não encontrado")

def relatorio_geral():
    print("\n---RELATÓRIO GERAL--- ")
    print(f"Quantidade de alunos: {quantidade_alunos}")

    

def menu():
    while True:
        op = int(input(
            "1-CADASTRAR 2-LANÇAR NOTA 3-CONSULTAR ALUNO: "
        ))

        if op == 1:
            cadastrar_aluno()

        elif op == 2:
            lancar_nota()

        elif op == 3:
            consultar_aluno()


menu()