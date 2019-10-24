"""
This file holds the Operation class
"""


import re


class Operation:
    """
    Operation class which parses expressions to attributes lhs, operand, rhs and result
    """
    def __init__(self, string_input):
        self.lhs, self.operand, self.rhs, self.result = self.parse_input(string_input)

    def parse_input(self, string_input):
        """
        Method which splits the expression to lhs, operand, rhs and result to initialize Operation
        :param string_input: String containing expression passed into Calculator
        :return: lhs, operand, rhs and result
        """
        pattern = re.compile('(\\d+) ([+-/*]) (\\d+) = (\\d+)')
        if not pattern.match(string_input) and not None:
            raise ValueError('String Input is in the wrong format')
        parsed_input = pattern.match(string_input)
        lhs = int(parsed_input.group(1))
        operand = parsed_input.group(2)
        rhs = int(parsed_input.group(3))
        result = int(parsed_input.group(4))
        return lhs, operand, rhs, result
