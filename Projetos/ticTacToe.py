import random

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Jogador humano é X

    def print_board(self):
        print("\n")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)
        print("\n")

    def is_winner(self, player):
        b = self.board
        # Linhas, colunas e diagonais
        return any(
            all(cell == player for cell in row) for row in b
        ) or any(
            all(b[r][c] == player for r in range(3)) for c in range(3)
        ) or all(
            b[i][i] == player for i in range(3)
        ) or all(
            b[i][2 - i] == player for i in range(3)
        )

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def make_move(self, row, col, player):
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def get_empty_cells(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

    def computer_move(self):
        # Movimento aleatório do computador
        row, col = random.choice(self.get_empty_cells())
        self.make_move(row, col, "O")
        print(f"Computador jogou em ({row}, {col})")

    def play(self):
        print("Bem-vindo ao Jogo da Velha!")
        while True:
            self.print_board()

            if self.current_player == "X":
                try:
                    row = int(input("Escolha a linha (0-2): "))
                    col = int(input("Escolha a coluna (0-2): "))
                except ValueError:
                    print("Entrada inválida.")
                    continue

                if 0 <= row <= 2 and 0 <= col <= 2:
                    if not self.make_move(row, col, "X"):
                        print("Posição ocupada. Tente novamente.")
                        continue
                else:
                    print("Coordenadas fora do intervalo.")
                    continue
            else:
                self.computer_move()

            if self.is_winner(self.current_player):
                self.print_board()
                if self.current_player == "X":
                    print("Você venceu!")
                else:
                    print("O computador venceu!")
                break
            elif self.is_full():
                self.print_board()
                print("Empate!")
                break

            self.current_player = "O" if self.current_player == "X" else "X"

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
