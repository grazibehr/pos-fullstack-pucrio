# ============================================
# EXERCÍCIO 08 – FUNÇÕES EM PYTHON
# Objetivos:
# - Criar funções com e sem parâmetros
# - Utilizar retorno (return)
# - Chamar funções dentro de um programa
# ============================================

def saudacao():
    print("Olá! Seja bem-vindo ao exercício de funções, Fulana!")
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
def somar(a, b):
    return a + b

def menu():
    print("\n=== MENU DE OPERAÇÕES ===")
    print("1 - Saudação")
    print("2 - Apresentar")
    print("3 - Somar números")
    print("0 - Sair")

opcao = ""
while opcao != "0":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saudacao()

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        apresentar(nome, idade)

    elif opcao == "3":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = somar(num1, num2)
        print("Resultado da soma:", resultado)

    elif opcao == "0":
        print("Encerrando...")
    else:
        print("Opção inválida. Tente novamente.")
