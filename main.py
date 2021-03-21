from banco import banco
from pessoas import pessoa
bancos =[]
pessoas =[]
continuar = True

while(continuar):
    print(f"{30*'-'}Menu{30*'-'}")
    print("1- adicionar banco")
    print("2- listar bancos")
    print("3- cadastrar cliente")
    print("4- listar clientes")
    print("5- adicionar conta ao cliente")
    print("6- depositar")
    print("7- ver saldo")
    print("8- sacar")
    print("0- para sair")
    menu = int(input("Digite a opção: "))
    print(64*'-')

    if menu == 1:
        agencia = len(bancos)+1
        nome = input("Digite o nome do banco: ")
        bancos.append(banco.Banco(agencia,nome))
        print(f"Seu banco foi criado com sucesso! A agencia dele é {agencia}")
    elif menu ==2:
        for i in bancos:
            print(i)

    elif menu ==3:
        agencia = int(input("Digite a agencia do banco: "))
        for i in bancos:
            if i.agencia == agencia:
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))
                if idade >=18:
                    print("Tipo conta:")
                    tipoConta = int(input("1- Conta Corrente     2- Conta Poupanca "))
                    print(i.adicionarCliente(nome,idade,tipoConta))
                    break
                else:
                    print("Não é possivel criar conta para menores de idade")
                    break

    elif menu == 4:
        agencia = int(input("Digite a agencia: "))
        for i in bancos:
            if i.agencia == agencia:
                print(i.exibirClientes())
                break

    elif menu ==5:
        agencia = int(input("Digite a agencia"))
        id = int(input("Digite o ID do cliente"))
        tipoConta = int(input("1- Conta Corrente     2- Conta Poupanca "))
        for i in bancos:
            if i.agencia == agencia:
                i.adicionarConta(id,tipoConta)
                break

    elif menu ==6:
        agencia = int(input("Digite a agencia "))
        nConta = int(input("Digite o numero da conta "))
        quantidade = int(input("Digite a quantidade "))
        for i in bancos:
            if agencia == i.agencia:
                print(i.depositar(nConta,quantidade))

    elif menu == 7:
        agencia = int(input("Digite a agencia "))
        id = int(input("Digite o ID do cliente "))
        nConta = int(input("Digite o numero da conta "))
        for i in bancos:
            if i.agencia == agencia:
                print(i.verSaldo(id,nConta))
    
    elif menu == 8:
        agencia = int(input("Digite a agencia"))
        id = int(input("Digite o ID do cliente"))
        nConta = int(input("Digite o numero da conta"))
        quantidade = int(input("Quanto deseja sacar?"))
        for i in bancos:
            if i.agencia == agencia:
                print(i.sacar(id,nConta,quantidade))

    elif menu ==0:
        continuar = False