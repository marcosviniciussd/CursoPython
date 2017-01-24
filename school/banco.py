class Conta:

    def __init__(self, agencia, conta, titular):

        self.agencia = agencia
        self.conta = conta
        self.titular = titular
        self.__saldo = 0


    def saca(self, valor):
        
        self.__saldo -= valor;


    def deposita(self, valor):

        self.__saldo += valor

    def get_saldo(self):

        return self.__saldo

