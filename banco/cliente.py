from pessoas import pessoa

class Cliente(pessoa.Pessoa):
    def __init__(self,id,pessoa):
        super().__init__(pessoa.nome,pessoa.idade)
        self.__id = id
        self.__contas = []

    @property
    def id(self):
        return self.__id
    
    @property
    def contas(self):
        return self.__contas
    
    def adicionarConta(self,conta):
        self.__contas.append(conta)