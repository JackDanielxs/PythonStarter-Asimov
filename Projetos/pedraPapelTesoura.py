import random
import os

# Opções possíveis
MOVES = ["pedra", "papel", "tesoura"]

# Placar
placar_player = 0
placar_cpu = 0

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_placar():
    print("================")
    print("\nPLACAR:")
    print(f"Você: {placar_player}")
    print(f"Computador: {placar_cpu}")
    print("================")

def mostrar_opcoes():
    print("\nESCOLHA SEU LANCE:")
    print("0 - Pedra | 1 - Papel | 2 - Tesoura")

def obter_jogada_player():
    while True:
        try:
            escolha = int(input("Digite o número da sua jogada: "))
            if escolha in [0, 1, 2]:
                return MOVES[escolha]
            else:
                print("Escolha inválida. Digite 0, 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def jogada_computador():
    return random.choice(MOVES)

def decidir_vencedor(jogada_player, jogada_cpu):
    global placar_player, placar_cpu

    if jogada_player == jogada_cpu:
        return "d"  # empate

    vence = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if vence[jogada_player] == jogada_cpu:
        placar_player += 1
        return "p"  # player venceu
    else:
        placar_cpu += 1
        return "c"  # computador venceu

def mostrar_resultado(jogada_player, jogada_cpu, vencedor):
    print("\n================")
    print(f"Sua jogada: {jogada_player.upper()}")
    print(f"Jogada do computador: {jogada_cpu.upper()}")

    if vencedor == "p":
        print("Você venceu!")
    elif vencedor == "c":
        print("Você perdeu!")
    else:
        print("Empate!")
    print("================")

def jogar_novamente():
    while True:
        escolha = input("Jogar novamente? (s/n): ").strip().lower()
        if escolha in ["s", "n"]:
            return escolha == "s"
        else:
            print("Digite 's' para sim ou 'n' para não.")

def main():
    limpar_tela()
    print("================")
    print("Pedra, papel e tesoura - Daniel Marques")

    while True:
        mostrar_placar()
        mostrar_opcoes()

        jogada_player = obter_jogada_player()
        jogada_cpu = jogada_computador()
        vencedor = decidir_vencedor(jogada_player, jogada_cpu)

        mostrar_resultado(jogada_player, jogada_cpu, vencedor)

        if not jogar_novamente():
            break
        limpar_tela()

if __name__ == "__main__":
    main()
