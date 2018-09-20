class SolicitacaoMatricula():
    def __init__(self, Aluno, DisciplinaOfertada, dt_solicitacao, Coordenador=None, status="Solicitada"):
        self.Aluno = Aluno
        self.DisciplinaOfertada = DisciplinaOfertada
        self.dt_solicitacao = dt_solicitacao
        self.Coordenador = Coordenador
        self.status = status