# [Vetores e Condicionais] Um roubo aconteceu na cidade de
# Recife e, você foi contratado para desenvolver um programa que possa
# ajudar a identificar uma das pessoas envolvidas. Desenvolva uma solução
# que faça 5 perguntas para apenas uma pessoa sobre o roubo, sendo elas:
# “Conhece a vítima do roubo?”
# “Esteve no local do roubo?”
# “Mora perto da vítima?”
# “A vítima lhe devia?”
# “Já trabalhou com a vítima?”

# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como
# “Ladrão”. Caso contrário, ela será classificada como “Inocente”.


# [Vetores e Condicionais] Um roubo aconteceu na cidade de
# Recife e, você foi contratado para desenvolver um programa que possa
# ajudar a identificar uma das pessoas envolvidas. Desenvolva uma solução
# que faça 5 perguntas para apenas uma pessoa sobre o roubo, sendo elas:
# “Conhece a vítima do roubo?”
# “Esteve no local do roubo?”
# “Mora perto da vítima?”
# “A vítima lhe devia?”
# “Já trabalhou com a vítima?”

# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como
# “Ladrão”. Caso contrário, ela será classificada como “Inocente”.

resposta = []

print('Responda as perguntas com s ou n')

resposta.append(input('Conhece a vitima do roubo?'))
resposta.append(input('Esteve no local do roubo?'))
resposta.append(input('Mora perto da vitima?'))
resposta.append(input('A vitima lhe devia?'))
resposta.append(input('Ja trabalhou com a vitima?'))

positiva = resposta.count('s')

if positiva == 2:
    print('Suspeita')
elif positiva >= 3 and positiva <= 4:
    print('Cumplice')
elif positiva == 5:
    print('Ladrao')
else:
    print('Inocente')
