from src.handler import AdditionHandler

OPERATION_HANDLERS = [
    AdditionHandler()
]


class Calculator:
    def validate(self, operation):
        for handler in OPERATION_HANDLERS:
            if operation.operand == handler.eligible_operand:
                return handler.check_operation_is_correct(operation)
