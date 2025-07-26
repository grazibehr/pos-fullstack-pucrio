# ============================================
# EXERCÍCIO 14 – LSP (LISKOV SUBSTITUTION PRINCIPLE)
# --------------------------------------------
# As subclasses devem poder substituir a classe base
# sem alterar o comportamento esperado.
# ============================================

class Felidae:
    def meow(self):
        print("Esse Felideo mia ;3")

class Cat(Felidae):
    def meow(self):
        print("Esse gato esta miando ;3")  

class Tiger(Felidae):
    def meow(self):
        print("Esse tigre esta miando ;3")

def make_felidae_meow(felidae: Felidae):
    felidae.meow()


# ======================
# TESTANDO
# ======================
if __name__ == "__main__":
    felidaes = [Cat(), Tiger()]

    for f in felidaes:
       make_felidae_meow(f)    