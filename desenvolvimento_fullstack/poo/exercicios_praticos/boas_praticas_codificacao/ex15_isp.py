# ============================================
# EXERCÍCIO 15 – ISP (INTERFACE SEGREGATION PRINCIPLE)
# --------------------------------------------
# Nenhuma classe deve ser forçada a implementar métodos
# que não usa. Deve-se criar interfaces específicass
# ============================================


class Tearful:
    def tear(self):
        pass


class Laughing:
    def laugh(self):
        pass

class Baby(Tearful):
    def tear(self):
        return "O bebe esta choroso!"

class Clown(Laughing, Tearful):
    def laugh(self):
        return "Oh, o palhaco esta risonho!"

    def tear(self):
        return "Oh, o palhaco esta choroso!"  



#  ======================
# TESTANDO
# ======================
if __name__ == "__main__":
    baby = Baby()
    clown = Clown()

    print(baby.tear())
    print(clown.laugh())
    print(clown.tear())