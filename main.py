from conta import Conta
from cliente import Cliente

def cadastro():
    nome = input("Insira seu nome: ")
    cpf = input("Insira seu CPF: ")
    numero = int(input("Insira o número da sua conta: "))
    saldo = float(input("Insira o saldo da sua conta: "))
    limite = float(input("Insira o limite da sua conta: "))
    cliente = Cliente(nome, cpf)
    conta = Conta(cliente, numero, saldo, limite)
    return conta

def menu(conta):
    print("\nSmart Bank")
    print("------------------------")
    print(f"Olá, {conta.cliente.nome}!")
    print(f"Número da conta: {conta.numero}")
    print(f"Saldo: {conta.saldo}")

sair = False

conta = cadastro()
menu(conta)

while sair == False:
    print("------------------------")
    print("Sacar: Digite 1")
    print("Depositar: Digite 2")
    print("Emitir histórico: Digite 3")
    print("Emitir extrato: Digite 4")
    print("Sair: Digite 5")
    print("------------------------")
    acao = int(input("Ação: "))

    match acao:
        case 1:
            float(input("Insira um valor de saque: R$ "))
        case 2:
            float(input("Insira um valor de depósito: R$ "))
        case 3:
            conta.emitirHistorico()
        case 4:
            conta.emitirExtrato()
        case 5:
            sair = True