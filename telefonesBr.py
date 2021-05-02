# Classe responsavel por validar o formato e aplicar mascara a numeros de telefone (padrao nacional)
import re


class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero Incorreto!!!")

    def __str__(self):
        return self.formata_telefone()

    @staticmethod
    def valida_telefone(telefone):
        padrao = "(\d{2,3})(\d{2})(\d{5})(\d{4})"
        resultado = re.findall(padrao, telefone)
        if resultado:
            return True
        else:
            return False

    def formata_telefone(self):
        padrao = padrao = "(\d{2,3})(\d{2})(\d{5})(\d{4})"
        resultado = re.search(padrao, self.numero)
        numero_formatado = f"+{resultado.group(1)} ({resultado.group(2)}) " \
                           f"{resultado.group(3)}-{resultado.group(4)}"
        return numero_formatado