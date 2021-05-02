#Classe responsável pelo tratamento de Datas
from datetime import datetime, timedelta


class Cadastro:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_cadastro()

    def __sub__(self, other):
        return self.momento_cadastro - other

    def mes_cadastro(self):
        meses_ano = (
                "Janeiro", "Fevereiro", "Março","Abril","Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        )
        mes_atual = self.momento_cadastro.month
        return meses_ano[mes_atual - 1]

    def dia_cadastro(self):
        dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
        dia_cadastro = self.momento_cadastro.weekday()
        return dias_semana[dia_cadastro]

    def data_cadastro(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")

    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro