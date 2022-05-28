numero = int(input())
participantes = {}
while numero:
    numero -= 1
    opcoes = input().split()
    participantes[opcoes[0]] = [opcoes[1], opcoes[2], opcoes[3]]
while True:
    try:
        pessoa, presente = input().split()
        if pessoa in participantes:
            if presente in participantes[pessoa]:
                print('Uhul! Seu amigo secreto vai adorar')
            else:
                print('Tente Novamente!')
        else:
            print('essa pessoa n�o indicou presentes!')   
    except:
        break
