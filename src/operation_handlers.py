"""
This file holds all the operation handler objects
"""


class OperationHandler:
    """
    Base class for all Operation Handlers
    """
    def __init__(self, operand):
        self.eligible_operand = operand

    def check_operation_is_correct(self, operation):
        """
        Method to validate individual operations (to be overridden in all operation handlers)
        :param operation: Instance of operation containing lhs, operand, rhs and result
        :return: boolean representing if the operation is correct or not
        """


class AdditionHandler(OperationHandler):
    """
    Operation handler for Addition operations
    """
    def __init__(self):
        super(AdditionHandler, self).__init__('+')

    def check_operation_is_correct(self, operation):
        result = operation.lhs + operation.rhs
        return result == operation.result


class SubtractionHandler(OperationHandler):
    """
    Operation Handler for Subtraction operations
    """
    def __init__(self):
        super(SubtractionHandler, self).__init__('-')

    def check_operation_is_correct(self, operation):
        result = operation.lhs - operation.rhs
        return result == operation.result


class MultiplicationHandler(OperationHandler):
    """
    Operation Handler for Multiplication operations
    """
    def __init__(self):
        super(MultiplicationHandler, self).__init__('*')

    def check_operation_is_correct(self, operation):
        result = operation.lhs * operation.rhs
        return result == operation.result


class DivisionHandler(OperationHandler):
    """
    Operation Handler for Division operations
    """
    def __init__(self):
        super(DivisionHandler, self).__init__('/')

    def check_operation_is_correct(self, operation):
        result = operation.lhs / operation.rhs
        return result == operation.result
