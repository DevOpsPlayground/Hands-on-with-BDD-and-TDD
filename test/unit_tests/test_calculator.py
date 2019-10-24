from unittest import TestCase

from assertpy import assert_that

from src.Calculator import Calculator
from src.Operation import Operation
from src.operation_handlers import *


class TestOperation(TestCase):
    def test_parse(self):
        parse_parameters = [
            ("1 + 1 = 2", 1, 1, '+', 2),
            ("10 + 10 = 20", 10, 10, '+', 20),
            ("1 - 1 = 2", 1, 1, '-', 2),
            ("10 * 10 = 20", 10, 10, '*', 20),
            ("050 / 10 = 5", 50, 10, '/', 5)
        ]
        for string_input, lhs, rhs, operand, result in parse_parameters:
            with self.subTest(input=string_input):
                operation = Operation(string_input)
                assert_that(operation.lhs).is_equal_to(lhs)
                assert_that(operation.rhs).is_equal_to(rhs)
                assert_that(operation.operand).is_equal_to(operand)
                assert_that(operation.result).is_equal_to(result)

    def test_parse_error_validation(self):
        parameters = [
            "1+1=3",
            "domdomvd",
            "1     +       1   = 2"
        ]
        for parameter in parameters:
            with self.subTest(input=parameter):
                assert_that(Operation).raises(ValueError).when_called_with(parameter)


class TestHandlers(TestCase):
    def test_addition_handler(self):
        parameters = [
            ('1 + 1 = 2', True),
            ('2 + 20 = 4', False),
            ('5 + 7 = 2', False)
        ]

        for string_input, expected in parameters:
            with self.subTest(input=string_input):
                op = Operation(string_input)
                assert_that(AdditionHandler().check_operation_is_correct(op)).is_equal_to(expected)

    def test_subtraction_handler(self):
        parameters = [
            ('10 - 1 = 9', True),
            ('12 - 2 = 4', False),
            ('15 - 7 = 2', False)
        ]

        for string_input, expected in parameters:
            with self.subTest(input=string_input):
                op = Operation(string_input)
                assert_that(SubtractionHandler().check_operation_is_correct(op)).is_equal_to(expected)

    def test_multiplication_handler(self):
        parameters = [
            ('1 * 1 = 1', True),
            ('2 * 12 = 4', False),
            ('5 * 7 = 2', False)
        ]

        for string_input, expected in parameters:
            with self.subTest(input=string_input):
                op = Operation(string_input)
                assert_that(MultiplicationHandler().check_operation_is_correct(op)).is_equal_to(expected)

    def test_division_handler(self):
        parameters = [
            ('1 / 1 = 1', True),
            ('2 / 2 = 4', False),
            ('5 / 7 = 2', False)
        ]

        for string_input, expected in parameters:
            with self.subTest(input=string_input):
                op = Operation(string_input)
                assert_that(DivisionHandler().check_operation_is_correct(op)).is_equal_to(expected)


class TestCalculator(TestCase):
    def test_validate(self):
        input_parameters = [
            ('295 - 4 = 291', True),
            ('7 * 4 = 28', True),
            ('10 / 5 = 2', True),
            ('2950 - 4 = 2946', True),
            ('70 * 4 = 28', False),
            ('10 / 50 = 2', False),
            ('295 - 4 = 95', False),
            ('7 * 404 = 28', False),
            ('10 / 123 = 2', False),
            ('295 - 444 = 291', False),
            ('71 + 4 = 75', True),
            ('10 - 5 = 5', True),
        ]
        for string_input, expected in input_parameters:
            with self.subTest(input=string_input):
                op = Operation(string_input)
                assert_that(Calculator().validate(op)).is_equal_to(expected)
