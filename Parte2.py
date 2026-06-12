alunos = []
matriz_nota = []
medias = []
aprovado = 0
reprovado = 0
recuperação = 0
def cadastrar_aluno():
    while True:
        aluno = {}
        aluno['notas'] = []
        aluno['media'] = 0

        print(" ---CADASTRAR ALUNO---")
        aluno['nome'] = input("Informe o nome do aluno: ")

        try:
            aluno['idade'] = int(input("Informe a idade do aluno: "))
        except ValueError:
            print("Dados inválidos")
            continue

        aluno['turma'] = input("Qual é a turma do aluno?: ")

        alunos.append(aluno)
        salvar_dados()
        print("Aluno cadastrado com sucesso!!")

        op = input("Deseja cadastrar novamente?: [S][N]").upper()

        if op not in ("S", "N"):
            print("Opção inválida!!")
            continue

        if op == "N":
            break


def lancar_notas():
    global aprovado, reprovado, recuperação

    while True:
        print("--- LANÇAR NOTAS ---")
        nome = input("Informe o nome do aluno que deseja buscar: ")
        encontrado = False

        for i in range(len(alunos)):
            if alunos[i]['nome'].lower() == nome.lower():
                encontrado = True

                notas = []
                soma = 0

                for x in range(4):
                    nota = float(input(f"Informe a {x+1}° nota do aluno {alunos[i]['nome']}: "))

                    if nota > 10 or nota < 0:
                        print("Nota inválida!")
                        continue

                    notas.append(nota)
                    soma += nota

                media_aluno = soma / 4

                if media_aluno >= 7:
                    aprovado += 1
                elif media_aluno >= 5:
                    recuperação += 1
                else:
                    reprovado += 1

                alunos[i]['notas'] = notas
                alunos[i]['media'] = media_aluno

                salvar_dados()
                matriz_nota.append(notas)
                medias.append(media_aluno)

                break

        if not encontrado:
            print("Aluno não encontrado!")

        op = input("Deseja lançar notas novamente? [S/N] ").upper()

        if op not in ("S", "N"):
            print("Opção inválida!")
            continue

        if op == "N":
            break

def consultar():
    while True:
        print(" ---CONSULTAR ALUNO---")
        nome = input("Informe o nome do aluno que deseja encontrar: ")
        encontrado = False

        for x in range(len(alunos)):
            if alunos[x]['nome'].lower() == nome.lower():
                encontrado = True
                print(" ===ALUNO===")
                print(f"NOME: {alunos[x]['nome']}")
                print(f"IDADE: {alunos[x]['idade']}")
                print(f"TURMA: {alunos[x]['turma']}")
                print(f"NOTAS: {alunos[x]['notas']}")
                print(f"MEDIA: {alunos[x]['media']}")

        if not encontrado:
            print("Aluno não encontrado!!")
            return

        op = input("Deseja consultar novamente? [S/N] ").upper()

        if op not in ("S", "N"):
            print("Opção inválida!")
            continue

        if op == "N":
            break

def relatorio():
    print(" ---RELATÓRIO GERAL---")
    print(f'QUANTIDADE DE ALUNOS: {len(alunos)}')

    if len(medias) > 0:
        media_turma = sum(medias) / len(medias)
        print(f"MEDIA DA TURMA: {media_turma}")
    else:
        print("MEDIA DA TURMA: sem dados ainda")

    print(f'APROVADOS: {aprovado}')
    print(f'RECUPERAÇÕES: {recuperação}')
    print(f'REPROVADOS: {reprovado}')

    if len(alunos) > 0:
        melhor_aluno = alunos[0]
        for i in range(1, len(alunos)):
            if alunos[i]['media'] > melhor_aluno['media']:
                melhor_aluno = alunos[i]

        print(f"MELHOR ALUNO: {melhor_aluno['nome']} - {melhor_aluno['media']}")

        pior_aluno = alunos[0]
        for i in range(1, len(alunos)):
            if alunos[i]['media'] < pior_aluno['media']:
                pior_aluno = alunos[i]

        print(f"PIOR ALUNO: {pior_aluno['nome']} - {pior_aluno['media']}")


def salvar_dados():
    arquivo = open("alunos.txt", "w", encoding="utf-8")

    for aluno in alunos:
        arquivo.write(
            f"{aluno['nome']};{aluno['idade']};{aluno['turma']};"
            f"{aluno.get('notas', [])};{aluno.get('media', 0)}\n"
        )

    arquivo.close()

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar aluno")
        print("2 - consultar alunos")
        print("3 - Lançar notas")
        print("4 - Relatório geral")
        print("5 - Salvar dados")
        print("6 - Sair")
        print("==========================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            consultar()

        elif opcao == "3":
            lancar_notas()

        elif opcao == "4":
            relatorio()

        elif opcao == "5":
            salvar_dados()

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()