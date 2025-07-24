# ============================================
# 🧪 EXERCÍCIO 07 – LAÇOS DE REPETIÇÃO (LOOPS)
# Objetivos:
# - Utilizar o laço while para repetições com condição
# - Utilizar o laço for com range() e listas
# - Aplicar as instruções break e continue
# - Praticar lógica de contagem e iteração
# ============================================

contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1

print("\nTabuada do 3:")
for i in range(1, 11):
    if i == 5:
        continue  # pula o 5
    if i == 8:
        break     # para no 8
    print(f"3 x {i} = {3 * i}")

nomes = ["Grazi", "Ana", "Bruno", "João", "Carlos"]
print("\nLista de nomes:")
for nome in nomes:
    if nome == "Bruno":
        continue  # pula Bruno
    if nome == "João":
        break     # para ao chegar no João
    print("Olá,", nome)
