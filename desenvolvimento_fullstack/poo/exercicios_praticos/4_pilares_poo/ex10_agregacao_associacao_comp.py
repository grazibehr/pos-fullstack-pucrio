# ============================================
# EXERCÍCIO 10 – ASSOCIAÇÃO, AGREGAÇÃO E COMPOSIÇÃO
# --------------------------------------------
# Objetivos:
# - Praticar os três tipos de relacionamento entre objetos
# - Reforçar encapsulamento e responsabilidades
# - Escrever e rodar testes simples
# ============================================

from __future__ import annotations
from typing import Optional, List, Tuple

# ------------------------- COMPOSIÇÃO ------------------------- #
class Boletim:
    def __init__(self) -> None:
        self._notas: dict[str, float] = {}

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        if not 0 <= nota <= 10:
            raise ValueError("Nota precisa estar entre 0 e 10")
        self._notas[disciplina] = float(nota)

    def media(self) -> float:
        return sum(self._notas.values()) / len(self._notas) if self._notas else 0.0

    def __repr__(self) -> str:
        return f"Boletim(notas={self._notas})"


# ------------------------- ASSOCIAÇÃO ------------------------- #
class Professor:
    def __init__(self, nome: str, registro: str):
        self.nome = nome
        self.registro = registro
        self._orientandos: List[Aluno] = []

    @property
    def orientandos(self) -> Tuple[Aluno, ...]:
        return tuple(self._orientandos)

    def _adicionar_orientando(self, aluno: "Aluno") -> None:
        if aluno not in self._orientandos:
            self._orientandos.append(aluno)

    def _remover_orientando(self, aluno: "Aluno") -> None:
        if aluno in self._orientandos:
            self._orientandos.remove(aluno)

    def __repr__(self) -> str:
        return f"Professor({self.nome!r})"


class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self._orientador: Optional[Professor] = None
        self._boletim = Boletim()

    @property
    def orientador(self) -> Optional[Professor]:
        return self._orientador

    def definir_orientador(self, professor: Optional[Professor]) -> None:
        if self._orientador is not None:
            self._orientador._remover_orientando(self)
        self._orientador = professor
        if professor is not None:
            professor._adicionar_orientando(self)

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        self._boletim.adicionar_nota(disciplina, nota)

    def media(self) -> float:
        return self._boletim.media()

    def __repr__(self) -> str:
        orient = self._orientador.nome if self._orientador else None
        return f"Aluno({self.nome!r}, orientador={orient!r}, media={self.media():.2f})"


# ------------------------- AGREGAÇÃO ------------------------- #
class Turma:
    def __init__(self, codigo: str, professor_responsavel: Professor):
        self.codigo = codigo
        self.professor_responsavel = professor_responsavel
        self._alunos: List[Aluno] = []

    def adicionar_aluno(self, aluno: Aluno) -> None:
        if aluno not in self._alunos:
            self._alunos.append(aluno)

    def remover_aluno(self, aluno: Aluno) -> None:
        if aluno in self._alunos:
            self._alunos.remove(aluno)

    @property
    def alunos(self) -> Tuple[Aluno, ...]:
        return tuple(self._alunos)

    def __repr__(self) -> str:
        return f"Turma({self.codigo!r}, alunos={[a.nome for a in self._alunos]})"


def _sep(titulo: str) -> None:
    print("\n" + "-" * 60)
    print(titulo)
    print("-" * 60)


def demo() -> None:
    _sep("1) Criando professores e alunos")
    prof1 = Professor("Dr. House", "P001")
    prof2 = Professor("Dra. Ana", "P002")

    a1 = Aluno("Grazi", "A001")
    a2 = Aluno("Bruno", "A002")
    a3 = Aluno("Ana", "A003")
    print(prof1, prof2)
    print(a1, a2, a3)

    _sep("2) Associação: definindo orientadores")
    a1.definir_orientador(prof1)
    a2.definir_orientador(prof2)
    # a3 fica sem orientador
    print(a1, a2, a3)

    _sep("3) Professores veem orientandos (bidirecional)")
    print("Prof1 orientandos:", prof1.orientandos)
    print("Prof2 orientandos:", prof2.orientandos)

    _sep("4) Agregação: criando turma e adicionando alunos")
    turma = Turma("INF-101", prof1)
    turma.adicionar_aluno(a1)
    turma.adicionar_aluno(a2)
    turma.adicionar_aluno(a3)
    print(turma)

    _sep("5) Composição: adicionando notas")
    a1.adicionar_nota("POO", 9.0)
    a1.adicionar_nota("Algoritmos", 8.5)
    a2.adicionar_nota("POO", 7.0)
    a3.adicionar_nota("POO", 10.0)
    print(a1, a2, a3)

    _sep("6) Troca/remover orientador")
    a1.definir_orientador(prof2)   # troca
    a2.definir_orientador(None)    # remove
    print("Prof1 orientandos:", prof1.orientandos)
    print("Prof2 orientandos:", prof2.orientandos)
    print(a1, a2, a3)

    _sep("7) Deletando a turma: alunos sobrevivem")
    del turma
    print("Turma deletada.\nAlunos ainda existem:")
    print(a1, a2, a3)

    _sep("8) Boletim pertence ao aluno (composição)")
    print("Média de a1:", a1.media())
    # Se deletar o aluno, não faz sentido acessar o boletim:
    # del a1
    # print(a1.media())  # erro


# ------------------------- TESTES RÁPIDOS ------------------------- #
def run_tests() -> None:
    print("Rodando testes rápidos...\n")

    prof = Professor("Prof Teste", "PT")
    aluno = Aluno("Aluno Teste", "AT")
    aluno.definir_orientador(prof)
    assert aluno.orientador is prof
    assert aluno in prof.orientandos
    aluno.definir_orientador(None)
    assert aluno.orientador is None
    assert aluno not in prof.orientandos

    prof2 = Professor("Prof2", "P2")
    turma = Turma("T01", prof2)
    turma.adicionar_aluno(aluno)
    assert aluno in turma.alunos
    turma.remover_aluno(aluno)
    assert aluno not in turma.alunos

    aluno2 = Aluno("Aluno Nota", "AN")
    aluno2.adicionar_nota("POO", 8.0)
    aluno2.adicionar_nota("Alg", 10.0)
    assert abs(aluno2.media() - 9.0) < 1e-6

    prof_a = Professor("P1", "1")
    prof_b = Professor("P2", "2")
    aluno3 = Aluno("A", "A")
    aluno3.definir_orientador(prof_a)
    assert aluno3 in prof_a.orientandos and aluno3 not in prof_b.orientandos
    aluno3.definir_orientador(prof_b)
    assert aluno3 in prof_b.orientandos and aluno3 not in prof_a.orientandos

    print("✅ Tudo certo!\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        demo()