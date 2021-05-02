import requests # Biblioteca Python para trabalhar com HTTP

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.__cep = cep
        else:
            raise ValueError("CEP Inválido!!!!")

    def __str__(self):
        return self.formata_cep()

    @property
    def cep(self):
        return self.__cep

    @staticmethod
    def valida_cep(cep):
        if len(str(cep))==8:
            return True
        else:
            return False

    def formata_cep(self):
        return f"Cep: {self.__cep[:5]}-{self.__cep[5:]}"

    def busca_cep(self):
        url = f'https://viacep.com.br/ws/{self.__cep}/json/'
        request = requests.get(url)
        dados = request.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )