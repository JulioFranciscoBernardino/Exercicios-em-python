import os



def main():
    notas, frequencias = pega_dados()
    nota_melhor, nota_pior, frequencia_melhor, pior_frequencia, disciplina_melhor_nota, disciplina_pior_nota, disciplina_melhor_frequencia, disciplina_pior_frequencia = trata_dados(notas, frequencias)
    imprime_dados(nota_melhor, nota_pior, frequencia_melhor, pior_frequencia, disciplina_melhor_nota, disciplina_pior_nota, disciplina_melhor_frequencia, disciplina_pior_frequencia)
 
 
    
def pega_dados():
    """Pega os dados do usuario"""
    disciplina_nota = {}
    disciplina_frequencia = {}
    
    while True:
        disciplina = input('Digite o nome da disciplina ou "EXIT" para lançar as frequência: ')
        if disciplina in ['EXIT', 'Exit', 'exit']:
            os.system('cls')
            break
        nota = float(input(f'Digite a nota da disciplina {disciplina}: '))
        disciplina_nota[disciplina] = nota
        
    while True:
        materia = input('Digite o nome da disciplina ou "EXIT" para encerrar: ')
        if materia in ['EXIT', 'Exit', 'exit']:
            os.system('cls')
            break
        frequencia = input(f'Digite a frequência da disciplina {materia} em porcentagem SEM O SIMBULO "%": ')
        if '%' in frequencia:
            print('Erro, não insira o simbulo de porcentagem')   
        else:
            try:
                frequencia = float(frequencia) 
                disciplina_frequencia[materia] = frequencia
            except ValueError:
                print('Erro, insira um valor válido')
                
    return disciplina_nota, disciplina_frequencia


        
def trata_dados(nota, frequencia):
    """Trata os dados passados"""
    melhor_nota = max(nota.values())  # Obtém a maior nota
    pior_nota = min(nota.values())  # Obtém a menor nota
    melhor_frequencia = max(frequencia.values())  # Obtém a maior frequência
    pior_frequencia = min(frequencia.values())  # Obtém a menor frequência
    
    disciplina_melhor_nota = max(nota, key=nota.get)  # Encontra a chave (disciplina) com o valor máximo
    disciplina_pior_nota = min(nota, key=nota.get)  # Encontra a chave (disciplina) com o valor mínimo
    disciplina_melhor_frequencia = max(frequencia, key=frequencia.get)  # Encontra a chave (disciplina) com o valor máximo
    disciplina_pior_frequencia = min(frequencia, key=frequencia.get)  # Encontra a chave (disciplina) com o valor mínimo
        
    return melhor_nota, pior_nota, melhor_frequencia, pior_frequencia, disciplina_melhor_nota, disciplina_pior_nota, disciplina_melhor_frequencia, disciplina_pior_frequencia



def imprime_dados(nota_melhor, nota_pior, frequencia_melhor, pior_frequencia, disciplina_melhor_nota, disciplina_pior_nota, disciplina_melhor_frequencia, disciplina_pior_frequencia):
    """Imprime o estatos de pior e melhor"""
    print(f'Melhor nota da disciplina:{disciplina_melhor_nota} {nota_melhor}')
    print(f'Pior nota da disciplina:{disciplina_pior_nota} {nota_pior}')
    print(f'Melhor frequência da disciplina:{disciplina_melhor_frequencia} {frequencia_melhor}')
    print(f'Pior frequência:{disciplina_pior_frequencia} {pior_frequencia}')   


if __name__ == '__main__':
    main()    