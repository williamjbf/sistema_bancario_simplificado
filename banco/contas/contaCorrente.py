from banco.contas import conta

class ContaCorrente(conta.Conta):
    def __init__(self,agencia,nConta,):
        super().__init__(agencia,nConta)
        self.__tipoConta = "Conta Corrente"
        self.__limite = 2000

    def sacar(self,quantidade):
        if quantidade <= self._saldo:
            self._saldo -= quantidade
            return "Saque efetuado com sucesso"
        else:
            return "Não foi possivel sacar"
    
    @property
    def tipoConta(self):
        return self.__tipoConta