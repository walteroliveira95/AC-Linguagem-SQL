from django.contrib import admin

from .models import Aluno, Atividade, Coordenador, Curso, Disciplina, Mensagem, Professor, User

admin.site.register(User)
admin.site.register(Aluno)
admin.site.register(Atividade)
admin.site.register(Coordenador)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Mensagem)
admin.site.register(Professor)
