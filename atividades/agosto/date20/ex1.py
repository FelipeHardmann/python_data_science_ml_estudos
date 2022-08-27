class ContaCorrente:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
        self.lista = []

    def consultarSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
        self.lista.append(f'(+){valor:.2f}')
    
    def sacar(self, valor):
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        self.__saldo -= valor
        self.lista.append(f'(-){valor:.2f}')
        return 'Saque realizado'
    
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
        return 'Transferência realizada com sucesso'

    def listar(self):
        print('----EXTRATO----')
        print(self.titular)
        for mov in self.lista:
            print(mov)
        print(f'Saldo: {self.consultarSaldo}')