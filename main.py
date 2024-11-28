from conta import Conta
from cliente import Cliente
import time

def cadastro():
    nome = input("Insira seu nome: ")
    cpf = input("Insira seu CPF: ")
    numero = int(input("Insira o número da sua conta: "))
    saldo = float(input("Insira o saldo da sua conta: "))
    limite = float(input("Insira o limite da sua conta: "))
    cliente = Cliente(nome, cpf)
    conta = Conta(cliente, numero, saldo, limite)
    return conta

sair = False

conta = cadastro()

while sair == False:
    print("\n> Smart Bank <")
    print("------------------------")
    print(f"Olá, {conta.cliente.nome}!\n")
    print("Sacar: Digite 1")
    print("Depositar: Digite 2")
    print("Emitir histórico: Digite 3")
    print("Emitir extrato: Digite 4")
    print("Sair: Digite 5")
    print("------------------------")
    acao = int(input("Ação: "))

    match acao:
        case 1:
            valor = float(input("Insira um valor de saque: R$ "))
            conta.sacar(valor)
        case 2:
            valor = float(input("Insira um valor de depósito: R$ "))
            conta.depositar(valor)
        case 3:
            conta.emitirHistorico()
        case 4:
            conta.emitirExtrato()
        case 5:
            print("\nSaindo de sua conta...")
            time.sleep(3)
            print("Seção encerrada!")
            sair = True