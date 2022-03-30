from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass


class NontermicalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("Non-terminal expression being interpreted ...")
        self._expression.interpret()


class TerminalExpression(AbstractExpression):

    def interpret(self):
        print("Terminal expression being interpreted ...")


if __name__ == "__main__":

    ast = NontermicalExpression(NontermicalExpression(TerminalExpression()))
    ast.interpret()

