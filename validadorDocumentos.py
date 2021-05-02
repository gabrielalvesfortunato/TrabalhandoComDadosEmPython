# Conjunto de classes responsáveis por validar e formatar documentos (CPF, CNPJ)
from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Cpf(documento)
        if len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!!!")


class Cpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!!")

    def __str__(self):
        return self.formata()

    @staticmethod
    def valida(documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    def formata(self):
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)


class Cnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!!")

    def __str__(self):
        return self.formata()

    @staticmethod
    def valida(documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def formata(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)