# (Arquivo e Tratamento de Exceções – 30 pontos) Um professor armazena em
# um arquivo texto “classe.txt” o número e o nome de cada aluno da turma da
# disciplina sob sua responsabilidade. Por questão de segurança, ele prefere
# armazenar as notas obtidas pelos alunos em cada prova em um outro arquivo
# texto (notas.txt), onde cada linha contém o número do aluno e os valores das
# notas de 4 provas. Escreva um programa que permita consultar as notas de cada
# aluno a partir do seu nome ou do seu número. Seu programa deve receber o
# nome ou número como entrada e buscar e imprimir a linha correspondente ao
# nome no arquivo “notas.txt”. Trate possíveis exceções.

def isnumber(value):
    try:
        int(value)
    except ValueError:
         return False
    return True
try:
    file = open("classe.txt", "r")
    file2 = open("notas.txt", "r")

    contador = 0
    cont = file2.readlines()
    limite = len(cont)

    print('0 - parar o programa')
    print('1 - Buscar por nome')
    print('2 - Buscar por numero')
    while True:
        opcao = input('Digite sua Opção: ')
        if isnumber(opcao) == True:
            opcao = int(opcao)
        
            if opcao == 0:
                break

            elif opcao == 1:
                nome = input('Qual o nome do aluno? ').title()
                for linha in file:
                    if nome in linha:
                        n1 = (linha.strip())
                        n2 = int(n1[0])
                        if n2 > limite:
                            print('numero do aluno nao encontrado')
                        else:
                            print(cont[n2 - 1])
                    else:
                        contador += 1        
                    if contador == limite:
                        print('nome nao encontrado')

            elif opcao == 2:
                num = input('Qual o numero do aluno? ')
                if isnumber(num) == True:
                    num = int(num)
                    if num <= 0:
                        print('numero nao encontrado')
                    else:
                        if num > limite:
                            print('numero do aluno nao encontrado')
                        else:
                            print(cont[num - 1])
                else:
                    print('nao é um numero')

        else:
            print('opção invalida')

    file.close()
    file2.close()

except FileNotFoundError:
    print("O Arquivo não foi encontrado.")
