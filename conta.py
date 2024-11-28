from datetime import datetime

class Conta:
    historico = [];
    saldo = 0.0;
    ultimaAlteracao = datetime.today().strftime('%d/%m/%Y - %H:%M:%S')

    def __init__(self, cliente, numero, saldo, limite):
        self.cliente = cliente
        self.numero = numero
        self.limite = limite
        self.saldo += saldo

    def sacar(self, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
            ultimaAlteracao = datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
            alteracao = {
                'acao': 'sacar',
                'alteracao': valor,
                'data': ultimaAlteracao,
                'novoValor': self.saldo
            }
            self.historico.append(alteracao)
            print(f"Sacado R${valor} na conta.")
        else:
            print(f"Saldo insuficiente. Pobre!!!!!!")
    
    def depositar(self, valor):
        if (self.saldo + valor <= self.limite):
            self.saldo += valor
            ultimaAlteracao = datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
            alteracao = {
                'acao': 'depositar',
                'alteracao': valor,
                'data': ultimaAlteracao,
                'novoValor': self.saldo
            }
            self.historico.append(alteracao)
            print(f"Depositado R${valor} na conta.")
        else:
            print(f"Limite insuficiente. Ganancioso.....")

    def emitirExtrato(self):
        print(f"\n----Extrato de {self.cliente.nome}----")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo atual: R${self.saldo}")
        print(f"Data da última alteração: {self.ultimaAlteracao}")

    def emitirHistorico(self):
        for registro in self.historico:
            print(f"{registro['acao'].capitalize()}: R${registro['alteracao']}  -  {registro['data']}")