class Mensagem():
    def __init__(self, Aluno, Professor, assunto, referencia, conteudo, status, dtEnvio, dtResposta=None, resposta=None):
        self.Aluno = Aluno
        self.Professor = Professor
        self.assunto = assunto
        self.referencia = referencia
        self.conteudo = conteudo
        self.status = status
        self.dtEnvio = dtEnvio
        self.dtResposta = dtResposta
        self.resposta = resposta