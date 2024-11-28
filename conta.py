# Guilherme Ricardo de Paiva e Gabriel Reis de Brito
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
        if (valor <= self.saldo and valor > 0):
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
        elif(valor > self.saldo):
            print(f"Saldo insuficiente. Pobre!!!!!!")
        elif(valor <= 0):
            print("Valor inválido!")
    
    def depositar(self, valor):
        if (self.saldo + valor <= self.limite and valor > 0):
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
        elif(valor > self.limite):
            print(f"Limite insuficiente. Ganancioso.....")
        elif(valor <= 0):
            print("Valor inválido!")

    def emitirExtrato(self):
        print(f"\n----Extrato de {self.cliente.nome}----")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo atual: R${self.saldo}")
        print(f"Data da última alteração: {self.ultimaAlteracao}")

    def emitirHistorico(self):
        for registro in self.historico:
            print(f"{registro['acao'].capitalize()}: R${registro['alteracao']}  -  {registro['data']}")