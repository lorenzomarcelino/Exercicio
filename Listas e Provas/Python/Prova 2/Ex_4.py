# [Matrizes] Segundo pesquisas recentes, as três profissões
# na área de tecnologia mais requisitadas são: desenvolvedor Java,

# arquiteto de software e cientista de dados. Para cada uma dessas
# profissões deverá ser cadastrado o salário médio, tempo mínimo de
# experiência e o valor da hora de trabalho. Desenvolva um programa
# utilizando matrizes que faça esse cadastro e, na sequência:
# a) Mostre a matriz na tela com os valores;
# b) A média salarial das três profissões;
# c) A soma dos valores da diagonal principal da matriz (valores em preto);

matriz =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
media = 0
soma_diagonal = 0

matriz [0][0] = (float(input('Digite o salario médio de um desenvolvedor Java: ')))
matriz [1][0] = (float(input('Digite o salario médio de um arquiteto de software: ')))
matriz [2][0] = (float(input('Digite o salario médio de um cientista de dados: ')))

matriz [0][1] = (float(input('Digite o tempo minimo de experiencia de um desenvolvedor Java: ')))
matriz [1][1] = (float(input('Digite o tempo minimo de experiencia de um arquiteto de software: ')))
matriz [2][1] = (float(input('Digite o tempo minimo de experiencia de um cientista de dados: ')))

matriz [0][2] = (float(input('Digite o valor da hora de trabalho de um desenvolvedor Java: ')))
matriz [1][2] = (float(input('Digite o valor da hora de trabalho de um arquiteto de software: ')))
matriz [2][2] = (float(input('Digite o valor da hora de trabalho de um cientista de dados: ')))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end="")
    print()

for l in range(0, 3):
    media += matriz[l][0]
print('A media salarial das tres profissoes e: ', media)

for i in range(3):
    soma_diagonal += matriz [i][i]

print('A soma dos valores da diagonal principal da matriz e: ', soma_diagonal)
