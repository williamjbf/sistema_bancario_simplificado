from banco.contas import conta

class ContaPoupanca(conta.Conta):
    def __init__(self,agencia,nConta,):
        super().__init__(agencia,nConta)
        self.__tipoConta = "Conta Poupanca"

    def sacar(self,quantidade):
        if quantidade <= self._saldo:
            self._saldo -= quantidade
            return True
        else:
            return False
        
    @property
    def tipoConta(self):
        return self.__tipoConta