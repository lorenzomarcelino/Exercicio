senhas = {}
for b in range(10):
    senha = input('escolha uma musica:')
    senha[-5:] + senha[b : 6]
    senha = senha.replace('a','@')
    senha = senha.replace('E','%')
    senha = senha.replace('e','!')
    senha = senha.replace('i','@')
    senha = senha.replace('o','#')
    senha = senha.replace('u','$')
    senha = senha.replace(' ','')
    senha =  senha.title()
    print(senha)
