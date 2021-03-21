import abc

class Conta(abc.ABC):
    def __init__(self,agencia,nConta):
        self._agencia = agencia
        self._nConta = nConta
        self._saldo = 0

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def nConta(self):
        return self._nConta

    @property
    def saldo(self):
        return self._saldo

    @abc.abstractmethod
    def sacar(self,quantidade):
        pass

    def deposito(self,quantidade):
        self._saldo += quantidade
        return "Deposito eftuado com sucesso"