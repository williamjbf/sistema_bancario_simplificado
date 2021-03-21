from banco import cliente
from pessoas import pessoa
from banco.contas import contaCorrente,contaPoupanca
class Banco():
    def __init__(self,agencia,nome):
        self.__agencia = agencia
        self.__nome = nome
        self.__contas = []
        self.__clientes = []

    @property
    def agencia(self):
        return self.__agencia
    @property
    def nome(self):
        return self.__nome
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def contas(self):
        return self.__contas

    def __str__(self):
        temp = str(self.__agencia) + ':' + self.__nome
        return temp

    def adicionarCliente(self,nome,idade,tipoConta):
        novaPessoa = pessoa.Pessoa(nome,idade)
        if tipoConta == 1:
            novoCliente = cliente.Cliente(len(self.__clientes)+1,novaPessoa)
            novaConta = contaCorrente.ContaCorrente(self.__agencia,len(self.__contas)+1)
            novoCliente.adicionarConta(novaConta)
            self.__contas.append(novaConta)
        elif tipoConta ==2:
            novoCliente = cliente.Cliente(len(self.__clientes)+1,novaPessoa)
            novaConta = contaPoupanca.ContaPoupanca(self.__agencia,len(self.__contas)+1)
            novoCliente.adicionarConta(novaConta)
            self.__contas.append(novaConta)
        self.__clientes.append(novoCliente)
        return f"o seu id é:{len(self.__clientes)+1} e o numero da sua conta é {len(self.__contas)+1}"
    
    def adicionarConta(self,idCliente,tipoConta):
        for i in self.__clientes:
            if i.id == idCliente:
                if tipoConta == 1:
                    novaConta = contaCorrente.ContaCorrente(self.__agencia,len(self.__contas)+1)
                    i.adicionarConta(novaConta)
                    self.__contas.append(novaConta)
                elif tipoConta ==2:
                    novaConta = contaPoupanca.ContaPoupanca(self.__agencia,len(self.__contas)+1)
                    i.adicionarConta(novaConta)
                    self.__contas.append(novaConta)
        return False

    def exibirClientes(self):
        elementos =''
        for i in self.__clientes:
            elementos += str(i.id) +':' + i.nome + '\n'
            for x in i.contas:
                elementos += str(x.nConta) + ':' + str(x.tipoConta) + '\n'
            elementos += 20*'-'
        return elementos
    
    def depositar(self,nConta,quantidade):
        for i in self.__contas:
            if i.nConta == nConta:
                return i.deposito(quantidade)
        return "Está conta não pertence a esse banco"
    
    def verSaldo(self,id,nConta):
        for i in self.__clientes:
            if i.id == id:
                for x in i.contas:
                    if x.nConta == nConta:
                        return x.saldo
                return "Está conta não pertence ao Cliente"
        return "Cliente não pertence a esse banco"
    
    def sacar(self,id,nConta,quantidade):
        for i in self.__clientes:
            if i.id == id:
                for x in i.contas:
                    if x.nConta == nConta:
                        return x.sacar(quantidade)
                return "Está conta não pertence ao Cliente"
        return "Cliente não pertence a esse banco"
                        