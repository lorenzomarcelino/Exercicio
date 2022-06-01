def ClassificaAluno(nota, faltas):
    if faltas <= 10 and nota >= 7 and nota < 9.5:
        return "APROVADO"
    elif faltas <= 10 and nota >= 9.5:
        return "APROVADO COM LOUVOR"
    elif faltas > 10:
        return "REPROVADO POR FALTAS"
    else:
        return "REPROVADO"
    

n = float(input())
f = int(input())
print(ClassificaAluno(n, f))
