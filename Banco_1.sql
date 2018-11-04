use Projeto
drop database teste2
create database teste2
use teste2

CREATE TABLE Usuario(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_IDusuario PRIMARY KEY (ID),
LOGIN VARCHAR (10) NOT NULL CONSTRAINT "UQ_LOGIN" UNIQUE(LOGIN),
SENHA VARCHAR (16) NOT NULL CONSTRAINT chksenha CHECK (LEN (senha) >=8),
DTExpiração DATE CONSTRAINT dfdataexpiração DEFAULT '01/01/1900')

CREATE TABLE Coordenador(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_IDcoordenador PRIMARY KEY(ID),
id_usuario SMALLINT,
nome VARCHAR (30),
email VARCHAR (30) CONSTRAINT "uq_email" UNIQUE(email) NOT NULL,
celular TINYINT CONSTRAINT "uq_celular" UNIQUE (celular) NOT NULL,
CONSTRAINT fkid_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario(ID));

CREATE TABLE Aluno(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_IDaluno PRIMARY KEY (ID),
id_usuario SMALLINT,
NOME VARCHAR (30),
EMAIL VARCHAR (30) CONSTRAINT "UQ_EMAIL_ALUNO" UNIQUE (EMAIL) NOT NULL,
CELULAR TINYINT CONSTRAINT "UQ_CELULAR_ALUNO" UNIQUE (CELULAR) NOT NULL,
RA TINYINT,
FOTO VARCHAR (255)
CONSTRAINT fkid_usuario_ALUNO FOREIGN KEY (id_usuario) REFERENCES Usuario(ID));

CREATE TABLE Professor(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_ID_PROFESSOR PRIMARY KEY (ID),
ID_USUARIO SMALLINT,
EMAIL VARCHAR (30) CONSTRAINT "UQ_EMAIL_PROFESSOR" UNIQUE (EMAIL) NOT NULL,
CELULAR TINYINT CONSTRAINT "UQ_CELULAR_PROFESSOR" UNIQUE (CELULAR) NOT NULL,
APELIDO VARCHAR (10)
CONSTRAINT fkid_usuario_professor FOREIGN KEY (id_usuario) REFERENCES Usuario(ID)); 

CREATE TABLE Disciplina(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_ID_DISCIPLINA PRIMARY KEY (ID),
NOME VARCHAR (30) CONSTRAINT "UQ_NOME_DISCIPLINA" UNIQUE (NOME) NOT NULL,
DATA DATE CONSTRAINT DFDATA DEFAULT (GETDATE()),
STATUS BIT CONSTRAINT "STATUS_CHECK" CHECK (STATUS = 1 OR STATUS = 0)
CONSTRAINT "STATUS_DEFAULT" DEFAULT 1,
PlanoDeEnsino VARCHAR (30),
CargaHoraria TINYINT CONSTRAINT "cargahoraria_CHECK" CHECK (cargahoraria = 40 OR cargahoraria = 80),
competencias VARCHAR (30),
habilidades VARCHAR (30),
ementa VARCHAR (30),
ConteudoProgramatico VARCHAR (30),
BibliografiaBasica VARCHAR (30),
BibliografiaComplementar VARCHAR (30),
PercentualPratico SMALLINT CONSTRAINT "percentualpratico_CHECK" CHECK (percentualpratico >= 0 OR percentualpratico <=100),
PercentualTeorico SMALLINT CONSTRAINT "percentualteorico_CHECK" CHECK (percentualteorico >= 0 OR percentualteorico <=100),
IDCoordenador SMALLINT,
CONSTRAINT fk_id_Coordenador FOREIGN KEY (IDCoordenador) REFERENCES Coordenador(ID)); 

CREATE TABLE Curso(
	ID SMALLINT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_IDCURSO PRIMARY KEY(ID),
	Nome VARCHAR(50) NOT NULL UNIQUE
)

CREATE TABLE DisciplinaOfertada(
	ID SMALLINT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_ID_DISCIPLINAOFERTADA PRIMARY KEY(ID),
	IdCoordenador SMALLINT NOT NULL CONSTRAINT fkid_coordenador_disciplinaofertada FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID),
	DtInicioMatricula DATE NULL,
	DtFimMatricula DATE NULL,
	IdDisciplina SMALLINT NOT NULL CONSTRAINT fkid_disciplina_disciplinaofertada FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(ID),
	IdCurso SMALLINT NOT NULL CONSTRAINT fkid_curso_disciplinaofertada FOREIGN KEY (IdCurso) REFERENCES Curso(ID),
	Ano SMALLINT NOT NULL CONSTRAINT Ano_CHECK CHECK (Ano BETWEEN 1900 AND 2100),
	Semestre TINYINT NOT NULL CONSTRAINT Semestre_CHECK CHECK(Semestre = 1 OR Semestre = 2),
	Turma CHAR (4) NOT NULL ,
	idProfessor SMALLINT NULL CONSTRAINT fkid_professor_disciplinaofertada FOREIGN KEY (IdProfessor) REFERENCES Professor(ID),
	Metodologia VARCHAR(250) NULL,
	Recursos VARCHAR(100),
	CriterioAvaliacao VARCHAR(100),
	PlanoDeAula VARCHAR(100)
);

CREATE TABLE SolicitacaoMatricula (
id TINYINT IDENTITY (1,1) NOT NULL CONSTRAINT pk_id_solicitacaomatricula PRIMARY KEY (id),
idAluno SMALLINT NOT NULL CONSTRAINT idaluno_fk FOREIGN KEY (idAluno) REFERENCES Aluno(id),
IdDisciplinaOfertada SMALLINT NOT NULL CONSTRAINT pk_iddiscisplinaofertada FOREIGN KEY (iddisciplinaofertada) REFERENCES DisciplinaOfertada(id),
DtSolicitacao DATE NOT NULL CONSTRAINT dfdtsolicitacao DEFAULT (GETDATE()),
idcoordenador SMALLINT NULL CONSTRAINT fk_idcoordenador FOREIGN KEY (idcoordenador) REFERENCES Coordenador(id),
status VARCHAR(10) NOT NULL CONSTRAINT  status_CHECK_solicitacaomatricula CHECK (status = 'solicitada' OR status = 'aprovada' OR status = 'rejeitada' OR status = 'cancelada')
CONSTRAINT status_default_solicitacaomatricula  DEFAULT ('solicitada'));

CREATE TABLE Atividade(
id SMALLINT NOT NULL CONSTRAINT  pk_id_atividade PRIMARY KEY (id),
titulo VARCHAR (20) NOT NULL CONSTRAINT uq_titulo UNIQUE (titulo),
descrição VARCHAR (255),
conteudo VARCHAR (255),
tipo VARCHAR (15) NOT NULL CONSTRAINT tipo_CHECK CHECK (tipo = 'resposta aberta' OR tipo = 'teste'),
extra VARCHAR (255),
idprofessor SMALLINT NOT NULL CONSTRAINT fk_idprofessor FOREIGN KEY (idprofessor) REFERENCES Professor(id));

CREATE TABLE AtividadeVinculada(
id SMALLINT NOT NULL CONSTRAINT	pk_id_atividadevinculada PRIMARY KEY (id),
idatividade SMALLINT NOT NULL CONSTRAINT fk_idatividadevinculada FOREIGN KEY (idatividade) REFERENCES Atividade(id) CONSTRAINT uq_idatividade UNIQUE (idatividade),
idprofessor SMALLINT NOT NULL CONSTRAINT fk_idprofessor_atividadevinculada FOREIGN KEY (idprofessor)REFERENCES Professor(id),
iddisciplinaofertada SMALLINT NOT NULL CONSTRAINT fk_iddisciplinaofertada_atividadevinculada FOREIGN KEY (iddisciplinaofertada) REFERENCES DisciplinaOfertada(id),
rotulo VARCHAR (4) NOT NULL CONSTRAINT uq_rotulo UNIQUE (rotulo),
Status VARCHAR (15) NULL CONSTRAINT status_CHECK_atividadevinculada CHECK (status = 'disponibilizada'OR status = 'aberta' OR status = 'fechada' OR status = 'fechada' OR status = 'encerrada' OR status = 'prorrogada'),
DtInicioRespostas  DATETIME NOT NULL,
DtFimRespostas DATETIME NOT NULL );

CREATE TABLE Entrega(
id SMALLINT NOT NULL IDENTITY(1,1) CONSTRAINT pkid_entrega PRIMARY KEY (id),
idAluno SMALLINT NOT NULL CONSTRAINT fkid_entrega_aluno FOREIGN KEY (idaluno) REFERENCES Aluno(id),
idatividade SMALLINT NOT NULL CONSTRAINT fkid_entrega_atividade FOREIGN KEY (idatividade) REFERENCES Atividade(id),
titulo VARCHAR(50) NOT NULL,
respota VARCHAR(250) NOT NULL,
dtentrega DATETIME NOT NULL CONSTRAINT df_dtentrega DEFAULT (GETDATE()),
status VARCHAR (9) NOT NULL CONSTRAINT df_status DEFAULT 'entregue' CONSTRAINT ck_status CHECK (status = 'entregue' OR status = 'corrigido'),
idprofessor SMALLINT NULL CONSTRAINT fkid_entrega_professor FOREIGN KEY (idprofessor) REFERENCES Professor(id),
nota FLOAT (2)NULL CONSTRAINT ck_nota CHECK (nota BETWEEN 0 AND 10),
dtavaliacao DATETIME NULL,
obs VARCHAR (150) NULL);
