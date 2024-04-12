def imprimir_tabuleiro(tabuleiro):
  for linha in tabuleiro:
      print(" | ".join(linha))
      print("-" * 9)


def verificar_vencedor(tabuleiro, jogador):
  
  for i in range(3):
      if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
         tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
          return True

  if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
     tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
      return True

  return False


def jogar_jogo_da_velha():
  tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
  jogador_atual = 'X'

  while True:
      imprimir_tabuleiro(tabuleiro)
      linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
      coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

      if tabuleiro[linha][coluna] != " ":
          print("Essa posição já está ocupada. Escolha outra.")
          continue

      tabuleiro[linha][coluna] = jogador_atual

      if verificar_vencedor(tabuleiro, jogador_atual):
          imprimir_tabuleiro(tabuleiro)
          print(f"Parabéns! Jogador {jogador_atual} venceu!")
          break

      if " " not in [posicao for linha in tabuleiro for posicao in linha]:
          imprimir_tabuleiro(tabuleiro)
          print("O jogo empatou!")
          break

      jogador_atual = 'O' if jogador_atual == 'X' else 'X'


print("Bem-vindo ao Jogo da Velha!")
jogar_jogo_da_velha()
