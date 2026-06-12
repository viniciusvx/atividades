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

        if aluno['nome'] == "":
            print("O nome não pode ser vazio!")
            continue

        try:
            aluno['idade'] = int(input("Informe a idade do aluno: "))
        except ValueError:
            print("Dados inválidos")
            continue

        aluno['turma'] = input("Qual é a turma do aluno?: ")

        if aluno['turma'] == "":
            print("A turma não pode ser vazia!")
            continue

        alunos.append(aluno)
        salvar_dados()
        print("Aluno cadastrado com sucesso!!")

        op = input("Deseja cadastrar novamente? [S/N]: ").upper()

        if op == "N":
            break
        elif op != "S":
            print("Opção inválida!")


def lancar_notas():
    global aprovado, reprovado, recuperação

    if len(alunos) == 0:
        print("Não há alunos cadastrados!")
        return

    while True:
        print("--- LANÇAR NOTAS ---")
        nome = input("Informe o nome do aluno: ")
        encontrado = False

        for i in range(len(alunos)):
            if alunos[i]['nome'].lower() == nome.lower():
                encontrado = True

                if len(alunos[i]['notas']) > 0:
                    print("Notas já lançadas para esse aluno!")
                    break

                notas = []
                soma = 0

                for x in range(4):
                    while True:
                        try:
                            nota = float(input(f"Informe a {x+1}ª nota: "))

                            if nota < 0 or nota > 10:
                                print("Nota deve ser entre 0 e 10!")
                                continue

                            notas.append(nota)
                            soma += nota
                            break

                        except ValueError:
                            print("Digite um número válido!")

                media = soma / 4

                if media >= 7:
                    aprovado += 1
                elif media >= 5:
                    recuperação += 1
                else:
                    reprovado += 1

                alunos[i]['notas'] = notas
                alunos[i]['media'] = media

                matriz_nota.append(notas)
                medias.append(media)

                salvar_dados()
                break

        if not encontrado:
            print("Aluno não encontrado!")

        op = input("Deseja continuar lançando notas? [S/N]: ").upper()
        if op == "N":
            break


def consultar():
    if len(alunos) == 0:
        print("Não há alunos cadastrados!")
        return

    while True:
        nome = input("Informe o nome do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno['nome'].lower() == nome.lower():
                encontrado = True
                print("\n--- ALUNO ---")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Turma: {aluno['turma']}")
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {aluno['media']}")

        if not encontrado:
            print("Aluno não encontrado!")

        op = input("Deseja consultar outro? [S/N]: ").upper()
        if op == "N":
            break


def relatorio():
    if len(alunos) == 0:
        print("Não há alunos cadastrados!")
        return

    print("\n--- RELATÓRIO GERAL ---")
    print(f"Total de alunos: {len(alunos)}")

    if len(medias) > 0:
        print(f"Média da turma: {sum(medias)/len(medias):.2f}")
    else:
        print("Média da turma: sem dados")

    print(f"Aprovados: {aprovado}")
    print(f"Recuperação: {recuperação}")
    print(f"Reprovados: {reprovado}")

    if len(alunos) > 0:
        melhor = alunos[0]
        pior = alunos[0]

        for aluno in alunos:
            if aluno['media'] > melhor['media']:
                melhor = aluno
            if aluno['media'] < pior['media']:
                pior = aluno

        print(f"Melhor aluno: {melhor['nome']} ({melhor['media']})")
        print(f"Pior aluno: {pior['nome']} ({pior['media']})")


def salvar_dados():
    if len(alunos) == 0:
        print("Não há dados para salvar!")
        return

    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['nome']}; {aluno['idade']}; {aluno['turma']};"
                f"{aluno.get('notas', [])}; {aluno.get('media', 0)}\n"
            )
def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Consultar aluno")
        print("3 - Lançar notas")
        print("4 - Relatório")
        print("5 - Salvar dados")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            consultar()
        elif opcao == 3:
            lancar_notas()
        elif opcao == 4:
            relatorio()
        elif opcao == 5:
            salvar_dados()
        elif opcao == 6:
            break
        else:
            print("Opção inválida!")


menu()