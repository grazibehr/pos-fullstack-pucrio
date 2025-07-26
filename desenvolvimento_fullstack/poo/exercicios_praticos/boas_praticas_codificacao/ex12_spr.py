# ============================================
# EXERCICIO 12 – SPR (SINGLE RESPONSABILITY PRINCIPLE)
# --------------------------------------------
#  Crie classes com responsabilidades diferentes utilizando o principio SRP
# ============================================


class User:
   def __init__(self, name):
        self.__name = name

   @property
   def name(self):
        return self.__name


class UserRepository:
   def save(self, user):
        text = f"Salvando usuário: {user.name}"

        width = len(text) + 4 
        print("")
        print("+" + "-" * (width - 2) + "+")
        print("| " + text + " |")
        print("+" + "-" * (width - 2) + "+")
        # TABELINHA EM VOLTA DO TEXTO 

# Testando
u = User("Grazi")
repo = UserRepository()
repo.save(u)  # imprime "Salvando usuário: Grazi"

