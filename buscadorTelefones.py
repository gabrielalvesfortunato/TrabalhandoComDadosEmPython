# Classe responsavel por encontrar telefones em textos
import re


class BuscadorTelefones:

    def __init__(self, texto):
        texto = str(texto)
        if len(texto) > 0:
            self.texto = texto
        else:
            raise ValueError("SEM CONTEÚDO PARA A BUSCA!!!!!")

    def __str__(self):
        if len(self.buscar_telefones()) > 0:
            return f'Telefones encontrados: {self.buscar_telefones()}\n'\
                   f'Quantidade de Telefones Encontrados: {len(self.buscar_telefones())}'
        else:
            return f'NÃO FORAM ENCONTRADOS TELEFONES NO TEXTO!!!'

    @staticmethod
    def padrao_busca():
        padrao_telefones = "\(?\d{2,3}\)?[ ]?\d{1}[ ]?\d{4,5}-?\d{4}[ ]?[.]?|"\
                           "\(?\d{2,3}\)?[ ]?\d{4,5}-?\d{4}[ ]?[.]?|\d{4,5}-?\d{4}[ ]?[.]?"
        return padrao_telefones

    def buscar_telefones(self):
        telefones =  re.findall(self.padrao_busca(), self.texto)
        return telefones