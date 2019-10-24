"""
This file holds the Calculator class which represents our feature/product
"""

from src.operation_handlers import AdditionHandler, SubtractionHandler, MultiplicationHandler, DivisionHandler


class Calculator:
    """
    Calculator class which has a validate method.
    The method passes operations to their appropriate handlers for validation
    """

    def __init__(self):
        self.operation_handlers = [
            AdditionHandler(),
            SubtractionHandler(),
            MultiplicationHandler(),
            DivisionHandler()
        ]

    def validate(self, operation):
        """
        Method to use applicable operation handler to evaluate if operation is right or not
        :param operation: operation object containing lhs, operand, rhs and result
        :return: boolean representing if operation is correct or not
        """
        for handler in self.operation_handlers:
            if operation.operand == handler.eligible_operand:
                return handler.check_operation_is_correct(operation)
