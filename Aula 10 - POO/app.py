from aluno import Aluno
from disciplina import Disciplina

nome_aluno = "Pedro"

aluno1 = Aluno("Joao", "12345", "Ciência da Computação")

prompt_ia = Disciplina("Prompt IA", "Jorge")
sers = Disciplina("Sers", "TicTac")

# Matricular aluno

aluno1.matricular(prompt_ia)
aluno1.matricular(sers)

# Adicionar a nota do aluno de acordo com a disciplina referente
aluno1.adicionar_nota(prompt_ia, 10)
aluno1.adicionar_nota(prompt_ia, 8)
aluno1.adicionar_nota(sers, 5)
aluno1.adicionar_nota(sers, 4)

print (aluno1.calcular_mediad(prompt_ia))
