use Projeto
drop database teste2
create database teste2
use teste2


create table Usuario(
ID smallint IDENTITY (1,1) not null constraint PK_IDusuario PRIMARY KEY (ID),
LOGIN varchar (10) not null CONSTRAINT "UQ_LOGIN" UNIQUE(LOGIN),
SENHA varchar (16) not null constraint chksenha check (len (senha) >=8),
DTExpiração DATE CONSTRAINT dfdataexpiração DEFAULT '01/01/1900')

CREATE TABLE  COORDENADOR(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_IDcoordenador PRIMARY KEY(ID),
id_usuario smallint,
nome varchar (30),
email varchar (30) constraint "uq_email" unique(email)not null,
celular tinyint constraint "uq_celular" unique (celular) not null,
constraint fkid_usuario foreign key (id_usuario) references Usuario(ID));

CREATE TABLE ALUNO (
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_IDaluno PRIMARY KEY (ID),
id_usuario smallint,
NOME VARCHAR (30),
EMAIL VARCHAR (30) CONSTRAINT "UQ_EMAIL_ALUNO" UNIQUE (EMAIL) NOT NULL,
CELULAR TINYINT CONSTRAINT "UQ_CELULAR_ALUNO" UNIQUE (CELULAR)NOT NULL,
RA TINYINT,
FOTO VARCHAR (255)
constraint fkid_usuario_ALUNO foreign key (id_usuario) references Usuario(ID));

CREATE TABLE PROFESSOR (
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_ID_PROFESSOR PRIMARY KEY (ID),
ID_USUARIO SMALLINT,
EMAIL VARCHAR (30) CONSTRAINT "UQ_EMAIL_PROFESSOR" UNIQUE (EMAIL) NOT NULL,
CELULAR TINYINT CONSTRAINT "UQ_CELULAR_PROFESSOR" UNIQUE (CELULAR)NOT NULL,
APELIDO VARCHAR (10)
constraint fkid_usuario_professor foreign key (id_usuario) references Usuario(ID)); 

CREATE TABLE DISCIPLINA(
ID SMALLINT IDENTITY (1,1) NOT NULL CONSTRAINT PK_ID_DISCIPLINA PRIMARY KEY (ID),
NOME VARCHAR (30) CONSTRAINT "UQ_NOME_DISCIPLINA" UNIQUE (NOME) NOT NULL,
DATA DATE CONSTRAINT DFDATA DEFAULT (GETDATE()),
STATUS VARCHAR (7) CONSTRAINT "STATUS_CHECK" CHECK (STATUS = 'ABERTA' OR STATUS = 'FECHADA')
CONSTRAINT "STATUS_DEFAULT" DEFAULT 'ABERTA',
PlanoDeEnsino varchar (30),
CargaHoraria tinyint constraint "cargahoraria_check" check (cargahoraria = 40 or cargahoraria = 80),
competencias varchar (30),
habilidades varchar (30),
ementa varchar (30),
ConteudoProgramatico varchar (30),
BibliografiaBasica varchar (30),
BibliografiaComplementar varchar (30),
PercentualPratico smallint constraint "percentualpratico_check" check (percentualpratico >= 0 or percentualpratico <=100),
PercentualTeorico smallint constraint "percentualteorico_check" check (percentualteorico >= 0 or percentualteorico <=100),
IDCoordenador smallint,
constraint fk_id_Coordenador foreign key (IDCoordenador) references coordenador(ID)); 

CREATE TABLE CURSO(
	ID SMALLINT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_IDCURSO PRIMARY KEY(ID),
	Nome Varchar(50) NOT NULL UNIQUE
)

CREATE TABLE DisciplinaOfertada(
	ID SMALLINT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_ID_DISCIPLINAOFERTADA PRIMARY KEY(ID),
	IdCoordenador SMALLINT NOT NULL CONSTRAINT fkid_coordenador_disciplinaofertada FOREIGN KEY (IdCoordenador) REFERENCES COORDENADOR(ID),
	DtInicioMatricula DATETIME NULL,
	DtFimMatricula DATETIME NULL,
	IdDisciplina SMALLINT NOT NULL CONSTRAINT fkid_disciplina_disciplinaofertada FOREIGN KEY (IdDisciplina) REFERENCES DISCIPLINA(ID),
	IdCurso SMALLINT NOT NULL CONSTRAINT fkid_curso_disciplinaofertada FOREIGN KEY (IdCurso) REFERENCES Curso(ID),
	Ano SMALLINT NOT NULL CONSTRAINT Ano_check CHECK (Ano between 1900 and 2100),
	Semestre tinyint NOT NULL CONSTRAINT Semestre_check CHECK(Semestre = 1 or Semestre = 2),
	Turma CHAR NOT NULL ,
	idProfessor SMALLINT NULL CONSTRAINT fkid_professor_disciplinaofertada FOREIGN KEY (IdProfessor) REFERENCES PROFESSOR(ID),
	Metodologia VARCHAR(250) NULL,
	Recursos VARCHAR(100),
	CriterioAvaliacao VARCHAR(100),
	PlanoDeAula VARCHAR(100)
);


create table SolicitacaoMatricula (
id tinyint identity (1,1) not null constraint pk_id_solicitacaomatricula primary key (id),
idAluno smallint not null constraint idaluno_fk foreign key (idAluno) references aluno(id),
IdDisciplinaOfertada smallint not null constraint pk_iddiscisplinaofertada foreign key (iddisciplinaofertada) references disciplinaofertada(id),
DtSolicitacao date not null constraint dfdtsolicitacao default (getdate()),
idcoordenador smallint null constraint fk_idcoordenador foreign key (idcoordenador) references coordenador(id),
status varchar(10) not null constraint  status_check_solicitacaomatricula check (status = 'solicitada' or status = 'aprovada' or status = 'rejeitada' or status = 'cancelada')
constraint status_default_solicitacaomatricula  default ('solicitada'));

create table atividade(
id smallint not null constraint  pk_id_atividade primary key (id),
titulo varchar (20) not null constraint uq_titulo unique (titulo),
descrição varchar (255),
conteudo varchar (255),
tipo varchar (15) not null constraint tipo_check check (tipo = 'resposta aberta' or tipo = 'teste'),
extra varchar (255),
idprofessor smallint not null constraint fk_idprofessor foreign key (idprofessor) references professor(id));

create table atividadevinculada(
id smallint not null constraint	pk_id_atividadevinculada primary key (id),
idatividade smallint not null constraint fk_idatividadevinculada foreign key (idatividade) references atividade(id) constraint uq_idatividade unique (idatividade),
idprofessor smallint not null constraint fk_idprofessor_atividadevinculada foreign key (idprofessor)references professor(id),
iddisciplinaofertada smallint not null constraint fk_iddisciplinaofertada_atividadevinculada foreign key (iddisciplinaofertada) references disciplinaofertada(id),
rotulo varchar (4) not null constraint uq_rotulo unique (rotulo),
Status varchar (15) null constraint status_check_atividadevinculada check (status = 'disponibilizada'or status = 'aberta' or status = 'fechada' or status = 'fechada' or status = 'encerrada' or status = 'prorrogada'),
DtInicioRespostas  datetime not null,
DtFimRespostas datetime not null );

create table entrega(
id smallint not null identity(1,1) constraint pkid_entrega primary key (id),
idAluno smallint not null constraint fkid_entrega_aluno foreign key (idaluno) references aluno(id),
idatividade smallint not null constraint fkid_entrega_atividade foreign key (idatividade) references atividade(id),
titulo varchar(50) not null,
respota varchar(250) not null,
dtentrega datetime not null constraint df_dtentrega default (getdate()),
status varchar (9) not null constraint df_status default 'entregue' constraint ck_status check (status = 'entregue' or status = 'corrigido'),
idprofessor smallint null constraint fkid_entrega_professor foreign key (idprofessor) references professor(id),
nota float (2)null constraint ck_nota check (nota between 0 and 10),
dtavaliacao datetime null,
obs varchar (150) null);

create table mensagem (
id smallint not null identity (1,1) constraint pk_mensagem primary key (id),
id_aluno smallint not null constraint fkid_aluno_mensagem foreign key (id_aluno) references aluno(id),
id_professor smallint not null constraint fkid_aluno_professor foreign key (id_professor) references professor(id),
assunto varchar (100) not null,
referencia varchar (150) not null,
conteudo varchar(250) not null,
status varchar(10) not null constraint df_status_mensagem default 'enviado' constraint ck_status_mensagem check (status = 'enviado' or status ='lido' or status = 'respondido'),
dtenvio datetime not null constraint dt_envio default (getdate()),
dtresposta datetime null,
resposta varchar (250) null);
