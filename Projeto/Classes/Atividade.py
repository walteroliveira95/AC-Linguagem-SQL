class Atividade():
    def __init__(self, titulo, conteudo, tipo, Professor, extras=None, descricao=None):
        self.titulo = titulo
        self.conteudo = conteudo
        self.tipo = tipo
        self.Professor = Professor
        self.descricao = descricao
        self.extras = extras