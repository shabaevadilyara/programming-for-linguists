"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import (BinaryOp, Digit, OpFactory, Op, ReversePolishNotation,
                                                           CloseBracket, OpenBracket)
from data_structures.queue_ import Queue_
from data_structures.stack import Stack


class ReversePolishNotationConverterState:
    """
    Class to store the state of RPN convert process
    """
    def __init__(self, expression_in_infix_notation: str):
        """
        :param expression_in_infix_notation: string with expression in infix notation
        """
        self.expression_in_infix_notation = Queue_(expression_in_infix_notation)
        self.expression_in_postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def pop_from_stack_until_opening_bracket(self):
        """
        Help function
        :return:
        """
        while not ReversePolishNotationConverter.is_open_bracket(self.stack.top()):
            self.expression_in_postfix_notation.put(self.stack.top())
            self.stack.pop()
        self.stack.pop()


class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """
    point = '.'

    @staticmethod
    def convert(expression_in_infix_notation: str) -> ReversePolishNotation:
        """
        Main method of the class.
        Convert an infix expression to reverse polish notation

        :return: ReversePolishNotation object
        """
        state = ReversePolishNotationConverterState(expression_in_infix_notation)

        while not state.expression_in_infix_notation.empty():
            character = state.expression_in_infix_notation.top()

            if ReversePolishNotationConverter.is_part_of_digit(character):
                digit = ReversePolishNotationConverter.read_digit(state)
                state.expression_in_postfix_notation.put(digit)
                continue

            operator = OpFactory.get_op_by_symbol(character)
            if ReversePolishNotationConverter.is_open_bracket(operator):
                state.stack.push(operator)
                state.expression_in_infix_notation.get()
                continue
            if ReversePolishNotationConverter.is_close_bracket(operator):
                state.pop_from_stack_until_opening_bracket()
                state.expression_in_infix_notation.get()
                continue
            if ReversePolishNotationConverter.is_binary_operation(operator):
                ReversePolishNotationConverter.pop_from_stack_until_prioritizing(operator, state)
                state.expression_in_infix_notation.get()
            else:
                raise Exception(character)
        while not state.stack.empty():
            state.expression_in_postfix_notation.put(state.stack.top())
            state.stack.pop()
        return state.expression_in_postfix_notation

    @staticmethod
    def pop_from_stack_until_prioritizing(operator: Op, state: ReversePolishNotationConverterState):
        """
        Help function to move elements from stack to state elements (operators)
        until element on the top of the stack  has less priority then current operator
        :param operator: Instance of Op class - current operator
        :param state: State of the RPN convert process
        """
        while (not state.stack.empty() and
               ReversePolishNotationConverter.is_binary_operation(state.stack.top()) and
               state.stack.top() > operator):
            state.expression_in_postfix_notation.put(state.stack.top())
            state.stack.pop()

        state.stack.push(operator)

    @staticmethod
    def read_digit(state) -> Digit:
        """
        Method to read a digit from self._infix_notation

        :param state: expression in Reverse Polish Notation Format
        :return: Instance of Digit class
        """
        digit = state.expression_in_infix_notation.top()
        state.expression_in_infix_notation.get()
        while (not state.expression_in_infix_notation.empty()
               and ReversePolishNotationConverter.is_part_of_digit(state.expression_in_infix_notation.top())):
            digit += state.expression_in_infix_notation.get()
        return Digit(digit)

    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        """
        Help function to check if symbol is a part of floating point number
        :param character: current symbol
        :return: True if character can be part of a digit, else False
        """
        return character.isdigit() or character == ReversePolishNotationConverter.point

    @staticmethod
    def is_open_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is open bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the open bracket operator else False
        """
        return isinstance(operator, OpenBracket)

    @staticmethod
    def is_close_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is close bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the close bracket operator else False
        """
        return isinstance(operator, CloseBracket)

    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is binary operator

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the binary operator else False
        """
        return isinstance(operator, BinaryOp)
