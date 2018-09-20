class Entrega():
    def __init__(self, Aluno, AtividadeVinculada, titulo, resposta, dtEntrega, Professor=None, nota=None, dtAvaliacao=None, status="Entregue", obs=None):
        self.Aluno = Aluno
        self.AtividadeVinculada = AtividadeVinculada
        self.titulo = titulo
        self.resposta = resposta
        self.dtEntrega = dtEntrega
        self.status = status
        self.Professor = Professor
        self.nota = nota
        self.dtAvaliacao = dtAvaliacao
        self.obs = obs