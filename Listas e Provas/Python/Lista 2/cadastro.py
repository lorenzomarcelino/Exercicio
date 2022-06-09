import csv
file = open('Chamada_05032021.csv', 'r')
linhas = file.readlines()[1:]

lista = []
for line in linhas:
    data = line.split(',')
    name = (data[2] + ',' + data[3]).replace('"', '')
    sexo = data[4]
    idade = []
    idade = data[5]
    lista.append(sexo)

n_male = lista.count('male')
n_female= lista.count('female')
print('o numero de homens é', n_male)
print('o numero de mulheres é ', n_female)

if sexo == 'male':
 v_max_male = max(idade, key=int)
 print(v_max_male)
