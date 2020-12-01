from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField


class CPF(object):
    @staticmethod
    def is_valid(cpf):
        cpf_field = BRCPFField()

        try:
            cpf_field.clean(cpf)
            return True
        except ValidationError:
            return False

    @staticmethod
    def get_digits(cpf):
        if cpf:
            return cpf.replace('.', '').replace('-', '')

        return None

    @staticmethod
    def add_zeros(cpf):
        if cpf:
            zeros = (11 - len(str(cpf))) * "0"
            return "%s%s" % (zeros, cpf)

        return None
