class Aluno():
    def __init__(self, Usuario, nome, email, celular, ra, foto=None):
        self.Usuario = Usuario       
        self.nome = nome
        self.email = email
        self.celular = celular
        self.ra = ra
        self.foto = foto