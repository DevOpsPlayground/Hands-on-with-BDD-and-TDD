   
1. We add our gherkin to the calculator.feature file

        Feature: Calculator
        Scenario Outline: Expression Validation
            Given I am a user of the Calculator App
            When I enter <expression>
            Then The output is <expected>
        
        
        Examples: Math Expressions
            |   expression              |   expected|
            |   2 + 1 = 3               |   True    |
            |   2 + 10 = 12             |   True    |
            |   2 + 11 = 13             |   True    |
            |   2 + 101 = 3             |   False   |
            |   2 + 1093 = 12           |   False   |

2. We now have to write implementations for the steps of our feature file e.g. for When I enter '2+1=3'

        @given(u'I am a user of the Calculator App')
        def step_impl(context):
            context.Calculator = Calculator()

        @when(u'I enter {expression}')
        def step_impl(context, expression):
            op = Operation(expression)
            context.output = context.Calculator.validate(op)
        
        
        @then(u'The output is {expected}')
        def step_impl(context, expected):
            assert_that(str(context.output)).is_equal_to(expected)

3. Now that we have our steps, change directory on terminal to features and run the feature test with the commands

        'cd test/features'
        'PYTHONPATH=../.. behave'
        
4. The tests predictably fail as we haven't built/developed this product/feature

5. So we are going to do this development under our src folder

8. Its at this point where TDD is usually introduced alongside BDD and that's why we have our unit_tests folder and the test_addition_teacher.py file in it.

9. We can write tests to help us along developing the each bit (unit) of our overall feature

10. Let's say we want our Calculator to look like this and be a class:

           OPERATION_HANDLERS = [
                AdditionHandler(),
                SubtractionHandler(),
                MultiplicationHandler(),
                DivisionHandler()
            ]


        class Calculator:
            def validate(self, operation):
                for handler in OPERATION_HANDLERS:
                    if operation.operand == handler.eligible_operand:
                        return handler.check_operation_is_correct(operation)
                        
  The validate method there is what would do all the magic. So let's start building out our functionality
  
  We are setting up different handler classes for each mathematical expression
  
11. Let's start with addition and write a test for what we want from our AdditionHandler class

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


IMPORTANT COMMANDS:
-   Run Unit tests with Coverage.. (Go to the unit test directory first)
        
           PYTHONPATH=../.. coverage run --source=../../src -m unittest discover -v  && coverage report -m


NOTES:
- The branch 'solution' of this repo has a solution to this exercise which you can go through in your own time
          
    
   