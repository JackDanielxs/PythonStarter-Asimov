# Sistema de locação de veículos - Daniel Marques

import os

class Veiculo:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco

    def detalhes(self):
        print(f"=== Detalhes do veículo ===\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
        print(f"Preço por dia: R${self.preco:.2f}")
        print("------------------")

    def descricao(self, id):
        print(f"[{id}] {self.marca} {self.modelo} ({self.ano}) - R${self.preco:.2f} /dia")


veiculosDisponiveis = []
veiculosAlugados = []

def cadastrarVeiculo():
    os.system("cls" if os.name == "nt" else "clear")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    preco = float(input("Preço por dia: "))
    novo = Veiculo(marca, modelo, ano, cor, preco)
    veiculosDisponiveis.append(novo)
    print("Veículo cadastrado com sucesso!\n")
    input("Pressione Enter para continuar...")

def editarVeiculo():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Editar Veículo ===\n")
    if not veiculosDisponiveis:
        print("Não há veículos disponíveis para editar.\n")
        input("Pressione Enter para continuar...")
        return

    mostrarVeiculo(veiculosDisponiveis)
    escolha = int(input("Digite o número do veículo a editar: "))
    if 0 <= escolha < len(veiculosDisponiveis):
        v = veiculosDisponiveis[escolha]
        print("\nDeixe em branco para manter o valor atual.\n")
        nova_marca = input(f"Marca [{v.marca}]: ") or v.marca
        novo_modelo = input(f"Modelo [{v.modelo}]: ") or v.modelo
        novo_ano = input(f"Ano [{v.ano}]: ") or v.ano
        nova_cor = input(f"Cor [{v.cor}]: ") or v.cor
        novo_preco = input(f"Preço por dia [{v.preco}]: ") or v.preco

        # Atualiza
        v.marca = nova_marca
        v.modelo = novo_modelo
        v.ano = int(novo_ano)
        v.cor = nova_cor
        v.preco = float(novo_preco)

        print("\nVeículo atualizado com sucesso!\n")
    else:
        print("\nEscolha inválida.\n")
    input("Pressione Enter para continuar...")

def excluirVeiculo():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Excluir Veículo ===\n")
    if not veiculosDisponiveis:
        print("Não há veículos disponíveis para excluir.\n")
        input("Pressione Enter para continuar...")
        return

    mostrarVeiculo(veiculosDisponiveis)
    escolha = int(input("Digite o número do veículo a excluir: "))
    if 0 <= escolha < len(veiculosDisponiveis):
        v = veiculosDisponiveis.pop(escolha)
        print(f"\nVeículo {v.marca} {v.modelo} removido com sucesso!\n")
    else:
        print("\nEscolha inválida.\n")
    input("Pressione Enter para continuar...")

def alugarVeiculo():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Alugar Veículo ===\n")
    if not veiculosDisponiveis:
        print("Não há veículos disponíveis no momento.\n")
        input("Pressione Enter para continuar...")
        return

    mostrarVeiculo(veiculosDisponiveis)
    escolha = int(input("Digite o número do veículo a alugar: "))
    if 0 <= escolha < len(veiculosDisponiveis):
        v = veiculosDisponiveis.pop(escolha)
        veiculosAlugados.append(v)
        dias = int(input("Duração do aluguel (em dias): "))
        valorTotal = v.preco * dias
        print(f"\nVocê alugou: {v.marca} {v.modelo}")
        print(f"Valor a pagar: R${valorTotal:.2f}")
    else:
        print("Escolha inválida.\n")
    input("Pressione Enter para continuar...")

def devolverVeiculo():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Devolver Veículo ===\n")
    if not veiculosAlugados:
        print("Não há veículos alugados no momento.\n")
        input("Pressione Enter para continuar...")
        return

    mostrarVeiculo(veiculosAlugados)
    escolha = int(input("Digite o número do veículo a devolver: "))
    if 0 <= escolha < len(veiculosAlugados):
        v = veiculosAlugados.pop(escolha)
        veiculosDisponiveis.append(v)
        print(f"\nVocê devolveu: {v.marca} {v.modelo}")
    else:
        print("Escolha inválida.\n")
    input("Pressione Enter para continuar...")

def mostrarDisponiveis():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Veículos Disponíveis ===\n")
    if not veiculosDisponiveis:
        print("Não há veículos disponíveis no momento.\n")
        input("Pressione Enter para continuar...")
        return

    mostrarVeiculo(veiculosDisponiveis)
    escolha = int(input("Digite o número do veículo para ver detalhes: "))
    if 0 <= escolha < len(veiculosDisponiveis):
        v = veiculosDisponiveis[escolha]
        print("")
        v.detalhes()
    input("Pressione Enter para continuar...")

def mostrarVeiculo(lista):
    i = 0
    for v in lista:
        v.descricao(i)
        i += 1
    print("------------------")

operacoes = {
    "1": "Mostrar veículos disponíveis",
    "2": "Cadastrar veículo",
    "3": "Editar veículo",
    "4": "Excluir veículo",
    "5": "Alugar veículo",
    "6": "Devolver veículo",
    "7": "Sair"
}

while True:

    os.system("cls" if os.name == "nt" else "clear")
    print("=== Sistema de Locação de Veículos ===\n")

    i = 1
    for key, name in operacoes.items():
        print(i, ":", name)
        i += 1
    
    print("\nDigite o código da operação desejada: ")
    operacao = int(input())
    print("")

    if operacao == 1:
        mostrarDisponiveis()
    elif operacao == 2:
        cadastrarVeiculo()
    elif operacao == 3:
        editarVeiculo()
    elif operacao == 4:
        excluirVeiculo()
    elif operacao == 5:
        alugarVeiculo()
    elif operacao == 6:
        devolverVeiculo()
    elif operacao == 7: # Sair do programa
        break