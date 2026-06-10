alunos = []
series = ('1', '2', '3', '4', '5', '6', '7', '8', '9', "1°", "2°", "3°")
turmas = ("A", "B", "C")
notas = []
matriz_nota = []

def cadastrar_aluno ():
    while True:  
        aluno = {}

        aluno['nome'] = input("Informe o nome do aluno: ")
        
        try:
         aluno['idade'] = int(input("Informe a idade do aluno: "))
        except ValueError:
            print("Dados inváldos")
            return None
        
        if aluno["idade"] < 0:
           print("A idade não pode ser menor que '0' ")
           return None
        
        aluno['serie'] = input(f"Informe a serie do {aluno['nome']} (ensino fundamental: 1 a 9) | (ensino medio: 1° a 3°): ")
        if aluno['serie'] not in series:
           print("Numero de serie inválido")
           return
        
        aluno['turma'] = input(F"Informe a turma do {aluno['nome']}: ").upper()
        if aluno['turma'] not in turmas:
           print("Turma inválida")
           return
        
        alunos.append(aluno)
        op = input("Deseja cadastrar novamente? [S][N]").upper()

        if op not in ('S','N'):
           print("Opção inválida!")
           return None

        if op == "N":
           
           print("Cadastro realizado!")
           break

def lancar_nota():
   nome_busca = input("Informe o nome do aluno que deseja: ")
   soma = 0 

   for aluno in alunos:
      if aluno['nome'] == nome_busca:
        for l in range (len(alunos)):
            linha = []
            
            for c in range (len(alunos)):
                for x in range (4):
            
                    nota = float(input(f"informe a {x+1}º nota do {aluno['nome']}: "))
                    soma += nota
                    notas.append(nota)
                    linha.append(nota)
                matriz_nota.append(linha)
        print(matriz_nota)

def menu():
   while True:
    op = int(input("1-CADASTRAR 2-LANÇAR NOTA"))

    if op == 1:
        cadastrar_aluno()

    elif op == 2:
       lancar_nota()


menu()