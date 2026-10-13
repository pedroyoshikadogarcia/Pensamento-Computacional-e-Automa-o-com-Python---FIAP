class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.disciplinas = []
        self.notas = {}

    def adicionar_nota(self, disciplina, nota):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)

        if disciplina.nome not in self.notas:
            self.notas[disciplina.nome] = []

        self.notas[disciplina.nome].append(nota)

a = Aluno("João")
d1 = Disciplina("Python", "Prof. Ana")
d2 = Disciplina("Python", "Prof. Carlos")

a.adicionar_nota(d1, 8)
a.adicionar_nota(d2, 6)
a.adicionar_nota(d1, 10)

print(len(a.disciplinas), len(a.notas), a.notas["Python"])