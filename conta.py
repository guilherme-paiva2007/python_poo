from datetime import datetime

class Conta:
    historico = [];
    saldo = 0.0;
    ultimaAlteracao = datetime.today().strftime('%d/%m/%Y - %H:%M:$S')

    def __init__(self, cliente, numero, limite):
        self.cliente = cliente
        self.numero = numero
        self.limite = limite

    def sacar(self, valor):
        if (valor <= self.saldo):
            saldo -= valor
            ultimaAlteracao = datetime.today.strftime('%d/%m/%Y - %H:%M:$S')
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
            saldo += valor
            ultimaAlteracao = datetime.today.strftime('%d/%m/%Y - %H:%M:$S')
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
        print(f"\tNúmero da conta: {self.numero}")
        print(f"\tSaldo atual: {self.saldo}")
        print(f"\tData da última alteração: {self.ultimaAlteracao}\n")

    def emitirHistorico(self):
        print(self.historico)
