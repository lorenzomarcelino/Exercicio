# (Dicionários e String) Uma turma foi dividida em 3 grupos com 3
# pessoas cada. Escreva um programa que lê o nome do grupo e as alturas das
# três pessoas de cada grupo. Essas alturas são armazenadas em um dicionário,
# onde a chave é o nome do grupo. Por fim, deverá ser mostrado um dicionário,
# onde a chave é o nome do grupo e o valor é a média de alturas (com duas casas
# decimais). Também deve ser apresentado o nome do grupo que obteve a maior
# média de alturas (com a primeira letra maiúscula).

dic = {}
altura = []
dic2 = {}

for i in range(3):
    altura1 = 0.0
    altura2= 0.0
    altura3 = 0.0
    nome = input('digite o nome do grupo: ')
    altura1 = (float(input('digite a altura: ')))
    altura2 = (float(input('digite a altura: ')))
    altura3 = (float(input('digite a altura: ')))
    dic.update({nome: [altura1, altura2, altura3]})
    altura = [altura1, altura2, altura3,]
    media = sum(altura)/ 3
    dic2[nome] = "%.2f" % media

print(dic2)
maior_media = max(dic, key = dic.get)
print('o nome do grupo que obteve a maior média de alturas é: {}'.format(maior_media).title())
