# ============================================
# EXERCÍCIO 03 – TRABALHANDO COM STRINGS
# Objetivos:
# - Descobrir o tamanho da string
# - Fatiar (substring)
# - Verificar conteúdo com operador `in`
# - Alterar para maiúsculas/minúsculas
# ============================================


frase = "Python é incrível!"

print("Tamanho:", len(frase))

# 2. Substrings
print("Primeiros 6 caracteres:", frase[:6])
print("Último caractere:", frase[-1])

# 3. Verificação com operador `in`
print("Python está na frase?", "Python" in frase)

# 4. Alteração de maiúsculas/minúsculas
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Capitalizado:", frase.capitalize())
