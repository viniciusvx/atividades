alunos = []
matriz_nota = []
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

        aluno['turma'] = input(f"Informe a série/turma do {aluno['nome']}: ")
        

        alunos.append(aluno)

        op = input("Deseja cadastrar novamente? [S][N] ").upper()

        if op == "N":
            print("Cadastro realizado!")
            break

def lancar_nota():
    while True:
        print("\n---LANÇAR NOTAS---\n")

        nome = input("Digite o nome do aluno: ")

        encontrado = False

        for i in range(len(alunos)):
            if alunos[i]['nome'].lower() == nome.lower():

                encontrado = True

                soma = 0
                notas = []

                for x in range(4):
                    msg = f'Informe a {x+1}° nota do aluno: '
                    nota = float(input(msg))

                    notas.append(nota)
                    soma += nota

                alunos[i]['notas'] = notas
                alunos[i]['media'] = soma / 4

                print("Notas lançadas com sucesso!")
                break

        if not encontrado:
            print("Aluno não encontrado!")

        op = input("Deseja continuar? [S][N]: ").upper()
        if op == "N":
            break

def consultar_aluno():
    print("\n---CONSULTAR ALUNO---\n")
    nome_busca = input("Informe o nome do aluno que deseja: ")
    encontrado = False

    for i in range(len(alunos)):
        if alunos[i]['nome'].lower() == nome_busca.lower():
            encontrado = True

            print(f"Nome: {alunos[i]['nome']}")
            print(f"Idade: {alunos[i]['idade']}")
            print(f"Turma: {alunos[i]['turma']}")
            print(f"Notas: {alunos[i]['nota']}")
            print(f"Média: {alunos[i]['media']}")

            if alunos[i]['media'] >=7:
                print("Aprovado!")

            elif alunos[i]['media'] >= 5:
                print("Recuperação")

            else:
                print("Reprovado")

    if not encontrado:
        print("Aluno não encontrado")

def relatorio_geral():
    print("\n---RELATÓRIO GERAL---")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!\n")
        return 
    medias = []
    for i in
    
    print(f'Total de alunos: {len(alunos)}')


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