from exame_raio_x import ExameRaioX
from exame_sangue import ExameSangue

class AprovaExame:
    def aprovar_solicitacao_exame(self, tipo_exame: any):
        tipo_exame.verifica_condicoes_exame()

exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()
aprovador = AprovaExame()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)