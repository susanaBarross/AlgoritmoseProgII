from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

a = Aluno(1234 , "Camila", "014587.2021")

a.imprimir()

print()
print("----- AlunoEnsinoMedio ----")

aem = AlunoEnsinoMedio(15478, "Jonas", "12459.2021", 2)
aem.imprimir()

print()
print("---- AlunoGraduacao ----")

ag = AlunoGraduacao(14962, "Pedro", "05487.2021", 8)
ag.imprimir()

