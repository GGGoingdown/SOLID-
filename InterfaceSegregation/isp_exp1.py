from abc import ABC, abstractmethod

""" 
如果LattleMachine繼承CoffeeMachine的interface.
則會導致 make_cappuccino 與 make_espresso interface被強制繼承
好的做法是把不同的咖啡品項作為不同的interface
讓咖啡機器去繼承專屬的interface
"""
# class CoffeeMachine(ABC):
#     def make_lattle(self) -> None:
#         raise NotImplementedError

#     def make_cappuccino(self) -> None:
#         raise NotImplementedError

#     def make_espresso(self) -> None:
#         raise NotImplementedError


class LattleInterface(ABC):
    @abstractmethod
    def make_lattle(self) -> None:
        pass


class CappuccinoInterface(ABC):
    @abstractmethod
    def make_cappuccino(self) -> None:
        pass


class EspressoInterface(ABC):
    @abstractmethod
    def make_espresso(self) -> None:
        pass


class LattleMachine(LattleInterface):
    def make_lattle(self) -> None:
        print("Make some lattle !!")


class CoolCoffeeMachine(LattleInterface, CappuccinoInterface, EspressoInterface):
    def make_lattle(self) -> None:
        print("Make some better lattle !!")

    def make_espresso(self) -> None:
        print("Make some better espresso !!")

    def make_cappuccino(self) -> None:
        print("Make some better cappuccino !!")


if __name__ == "__main__":
    lattle_machine = LattleMachine()
    lattle_machine.make_lattle()

    cool_machine = CoolCoffeeMachine()
    cool_machine.make_lattle()
    cool_machine.make_cappuccino()
