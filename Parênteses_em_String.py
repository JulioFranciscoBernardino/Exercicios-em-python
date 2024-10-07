def verifica_parenteses(expressao):
  """Verifica se os parênteses estão corretamente pareados."""
  aberturas = ['(', '[', '{']
  fechamentos = [')', ']', '}']
  pilha = []

  for caractere in expressao:
    if caractere in aberturas:
      pilha.append(caractere)
    elif caractere in fechamentos:
      if not pilha or aberturas[fechamentos.index(caractere)] != pilha.pop():
        return False
  return not pilha

expressao = input("Digite a expressão: ")
resultado = verifica_parenteses(expressao)

print("Os parênteses estão corretos?" , resultado)