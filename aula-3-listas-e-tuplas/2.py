def jogo_da_forca(palavra):
  letras_corretas = []
  chances = 7
  palavra = palavra.upper()
  palavra_escondida = ['_' for _ in palavra]

  while chances > 0 and '_' in palavra_escondida:
      letra = input("Digite uma letra: ").upper()

      if letra in letras_corretas:
          print("Você já tentou essa letra. Tente outra.")
          continue

      if letra in palavra:
          print("Letra correta!")
          letras_corretas.append(letra)
          for i in range(len(palavra)):
              if palavra[i] == letra:
                  palavra_escondida[i] = letra
      else:
          chances -= 1
          print(f"Letra incorreta! Você tem {chances} chances restantes.")

      print(' '.join(palavra_escondida))

  if '_' not in palavra_escondida:
      print("Parabéns! Você ganhou!")
  else:
      print("Você perdeu. A palavra correta era:", palavra)

palavra_secreta = "Python"
print("Bem-vindo ao jogo da forca!")
jogo_da_forca(palavra_secreta)
