from disciplina import Disciplina
class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina[disciplina.nome] = []

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def calcular_mediad(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len (notas)

    def calcular_media_geral(self) -> float:
        medias = []
        for d in self.disciplinas:
             media_d = self.calcular_mediad(d)
             medias.append(media_d)
        return sum(medias) / len(medias)