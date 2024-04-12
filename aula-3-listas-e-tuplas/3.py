def verifica_parenteses(expressao):
  pilha = []

  for caractere in expressao:
      if caractere == '(':
          pilha.append(caractere)
      elif caractere == ')':
          if not pilha:
              return False  
          pilha.pop()

  return not pilha  


expressao1 = "(())"
expressao2 = "()()(()())"
expressao3 = "( ) )"

print(expressao1, " - ", "OK" if verifica_parenteses(expressao1) else "Erro")
print(expressao2, " - ", "OK" if verifica_parenteses(expressao2) else "Erro")
print(expressao3, " - ", "OK" if verifica_parenteses(expressao3) else "Erro")
