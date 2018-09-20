class Disciplina():
    def __init__(self, Coordenador, nome, data, planoDeEnsino, cargaHoraria, competencias, habilidades, ementa, conteudoProgramatico, bibliografiaBasica, bibliografiaComplementar, percentualPratico, percentualTeorico, status="Aberta"):
        self.Coordenador = Coordenador
        self.nome = nome
        self.data = data
        self.status = status
        self.planoDeEnsino = planoDeEnsino
        self.cargaHoraria = cargaHoraria
        self.competencias = competencias
        self.habilidades = habilidades
        self.ementa = ementa
        self.conteudoProgramatico = conteudoProgramatico
        self.bibliografiaBasica = bibliografiaBasica
        self.bibliografiaComplementar = bibliografiaComplementar
        self.percentualPratico = percentualPratico
        self.percentualTeorido = percentualTeorico