alunos = []
notas_matriz = []

# -----------------------------
# CADASTRAR ALUNO
# -----------------------------
def cadastrar_aluno():
    aluno = {}

    aluno['nome'] = input("Nome do aluno: ")
    aluno['idade'] = int(input("Idade: "))
    aluno['turma'] = input("Turma: ")

    alunos.append(aluno)

    notas = []
    print("\nAgora digite as 4 notas:")
    for i in range(4):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    notas_matriz.append(notas)

    print("\nAluno cadastrado com sucesso!\n")


# -----------------------------
# LANÇAR NOTAS (EDITAR)
# -----------------------------
def lancar_notas():
    nome = input("Digite o nome do aluno: ")

    for i in range(len(alunos)):
        if alunos[i]['nome'].lower() == nome.lower():

            print("Digite as novas 4 notas:")
            notas = []

            for j in range(4):
                nota = float(input(f"Nota {j+1}: "))
                notas.append(nota)

            notas_matriz[i] = notas
            print("Notas atualizadas!\n")
            return

    print("Aluno não encontrado!\n")


# -----------------------------
# CONSULTA INDIVIDUAL
# -----------------------------
def consultar_aluno():
    nome = input("Digite o nome do aluno: ")

    for i in range(len(alunos)):
        if alunos[i]['nome'].lower() == nome.lower():

            notas = notas_matriz[i]
            media = sum(notas) / len(notas)

            print("\n--- DADOS DO ALUNO ---")
            print(f"Nome: {alunos[i]['nome']}")
            print(f"Idade: {alunos[i]['idade']}")
            print(f"Turma: {alunos[i]['turma']}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.2f}")

            if media >= 7:
                print("Situação: Aprovado")
            elif media >= 5:
                print("Situação: Recuperação")
            else:
                print("Situação: Reprovado")

            print()
            return

    print("Aluno não encontrado!\n")


# -----------------------------
# RELATÓRIO GERAL
# -----------------------------
def relatorio_geral():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!\n")
        return

    medias = []
    aprovados = recuperacao = reprovados = 0

    melhor = pior = 0

    for i in range(len(alunos)):
        media = sum(notas_matriz[i]) / 4
        medias.append(media)

        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1

        if media > medias[melhor]:
            melhor = i
        if media < medias[pior]:
            pior = i

    media_turma = sum(medias) / len(medias)

    print("\n--- RELATÓRIO GERAL ---")
    print(f"Total de alunos: {len(alunos)}")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Melhor aluno: {alunos[melhor]['nome']} ({medias[melhor]:.2f})")
    print(f"Pior aluno: {alunos[pior]['nome']} ({medias[pior]:.2f})")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}\n")


# -----------------------------
# SALVAR EM TXT
# -----------------------------
def salvar_txt():
    arquivo = open("alunos.txt", "w", encoding="utf-8")

    for i in range(len(alunos)):
        media = sum(notas_matriz[i]) / 4

        arquivo.write(
            f"{alunos[i]['nome']};"
            f"{alunos[i]['idade']};"
            f"{alunos[i]['turma']};"
            f"{notas_matriz[i]};"
            f"{media:.2f}\n"
        )

    arquivo.close()
    print("Dados salvos em alunos.txt\n")


# -----------------------------
# MATRIZ DE NOTAS
# -----------------------------
def mostrar_matriz():
    print("\n--- MATRIZ DE NOTAS ---")

    for i in range(len(alunos)):
        print(f"{alunos[i]['nome']} -> {notas_matriz[i]}")


# -----------------------------
# MENU
# -----------------------------
while True:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Lançar notas")
    print("3 - Consultar aluno")
    print("4 - Relatório geral")
    print("5 - Mostrar matriz de notas")
    print("6 - Salvar dados em TXT")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        cadastrar_aluno()
    elif op == "2":
        lancar_notas()
    elif op == "3":
        consultar_aluno()
    elif op == "4":
        relatorio_geral()
    elif op == "5":
        mostrar_matriz()
    elif op == "6":
        salvar_txt()
    elif op == "0":
        break
    else:
        print("Opção inválida!")