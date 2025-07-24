# ============================================
# EXERCICIO 09 – CLASSES E OBJETOS
# --------------------------------------------
# Objetivos:
# - Criar classes com __init__ e __str__
# - Instanciar objetos e acessar atributos
# - Imprimir representações textuais de objetos
# ============================================

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo}, escrito por {self.autor}"

livro_1 = Livro("O Morro dos Ventos Uivantes", "Emily Bronte")
livro_2 = Livro("O Tempo e o Vento", "Érico Veríssimo")

print(livro_1)
print(livro_2)
