"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import Op, ReversePolishNotation, Digit
from data_structures.stack.stack import Stack


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()

    def calculate(self, rpn_expression: ReversePolishNotation) -> float:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
        for element in rpn_expression:
            if isinstance(element, Op):
                res = self._calculate_value(element)
                self.stack.push(res)
            else:
                self.stack.push(element)
        return self.stack.top().digit

    def _calculate_value(self, operator: Op) -> Digit:
        first = self.stack.top()
        self.stack.pop()
        second = self.stack.top()
        self.stack.pop()
        return operator(first, second)

