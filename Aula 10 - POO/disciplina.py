class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome}, Professor: {self.professor}")


# TEMPORARIO
if __name__ == "__main__":
    python = Disciplina('PCP', 'Russi') # Instanciando com a classe Disciplina (D maiúsculo)
    print(python.nome)
    python.exibir_infos()