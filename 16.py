# 16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

# Pergunte a quantidade de cigarros fumados por dia
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))

# Pergunte quantos anos ele já fumou
anos_fumando = int(input("Quantos anos você já fumou? "))

# Calcule o total de cigarros fumados
total_cigarros = cigarros_por_dia * 365 * anos_fumando

# Calcule o tempo de vida perdido em minutos
tempo_perdido_minutos = total_cigarros * 10

# Converta o tempo de vida perdido de minutos para dias
tempo_perdido_dias = tempo_perdido_minutos / 1440

# Exiba o resultado
print(f"Você perderá aproximadamente {tempo_perdido_dias:.2f} dias de vida.")