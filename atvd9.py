aluno = {}

def salvar_arquivo():

    arquivo = open ('C:/Users/vboxuser/Documents/alunos.txt','w',encoding='utf-8')

    arquivo.write(
        f'{aluno['nome']}'+ ';' +
        f'{aluno["idade"]}'  + ';' +
        f'{aluno["curso"]}'+ '\n'
    )

    arquivo.close()

aluno = {}

aluno['nome'] = input ("Informe o nome do aluno: ")
aluno['idade'] = int(input("Informe a sua idade: "))
aluno['curso'] = input("Informe o seu curso: ")
print("Aluno salvo com sucesso!!")
salvar_arquivo()