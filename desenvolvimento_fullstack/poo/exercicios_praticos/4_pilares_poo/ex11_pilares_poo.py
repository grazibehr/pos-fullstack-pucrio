# ============================================
# EXERCICIO 11 – PILARES DA POO (Python)
# --------------------------------------------
# Encapsulamento • Abstração • Herança • Polimorfismo
# ============================================

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi
from typing import Protocol


# ===================== Encapsulamento =====================
class Conta:
    def __init__(self, saldo_inicial: float = 900.0) -> None:
        self.__saldo = float(saldo_inicial)

    @property
    def saldo(self) -> float:
        return self.__saldo

    def deposita(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Depósito precisa ser > 0")
        self.__saldo += valor

    def saca(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Saque precisa ser > 0")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor


# ====================== Abstração =========================
class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


@dataclass
class Circulo(Forma):
    raio: float

    def area(self) -> float:
        return pi * self.raio**2


@dataclass
class Retangulo(Forma):
    largura: float
    altura: float

    def area(self) -> float:
        return self.largura * self.altura


# ================= Herança & Polimorfismo =================
class Animal:
    def falar(self) -> None:
        print("...")


class Cachorro(Animal):
    def falar(self) -> None:
        print("Au!")


# -------- Polimorfismo sem herança  ----------
class TemArea(Protocol):
    def area(self) -> float:
        ...


def imprimir_area(figura: TemArea) -> None:
    """Aceita qualquer coisa que tenha .area()."""
    print("Área:", figura.area())


if __name__ == "__main__":
    print(">>> Testes rápidos dos 4 pilares <<<")

    # Encapsulamento
    conta = Conta(100)
    conta.deposita(50)
    try:
        conta.saca(200)
    except ValueError as e:
        print("Erro no saque:", e)
    print("Saldo final:", conta.saldo)

    # Herança / Polimorfismo
    rex = Cachorro()
    rex.falar()

    # Abstração + Polimorfismo
    imprimir_area(Circulo(2))
    imprimir_area(Retangulo(3, 4))
