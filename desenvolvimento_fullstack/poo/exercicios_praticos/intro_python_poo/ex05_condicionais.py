# ============================================
# EXERCÍCIO 05 – CONDICIONAIS (if, elif, else)
# Objetivos:
# - Solicitar dados do usuário via input()
# - Praticar estruturas condicionais
# - Exibir mensagens com base em regras
# ============================================

# Verificação de idade
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem exatamente 18 anos")
else:
    print("Maior de idade")
