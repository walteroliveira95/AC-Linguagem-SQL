class DisciplinaOfertada():
    def __init__(self, Coordenador, Disciplina, Curso, ano, semestre, turma, Professor=None, metodologia=None, recursos=None, criterioAvaliacao=None, planoDeAulas=None, dtInicioMatricula=None, dtFimMatricula=None):
        self.Coordenador = Coordenador
        self.dtInicioMatricula = dtInicioMatricula
        self.dtFimMatricula = dtFimMatricula
        self.Disciplina = Disciplina
        self.Curso = Curso
        self.ano = ano
        self.semestre = semestre
        self.turma = turma
        self.Professor = Professor
        self.metodologia = metodologia
        self.recursos = recursos
        self.criterioAvaliacao = criterioAvaliacao
        self.planoDeAulas = planoDeAulas