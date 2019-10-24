from src.Calculator import Calculator
from src.Operation import Operation

if __name__ == '__main__':
    op = Operation('2 + 2 = 4')
    print(Calculator().validate(op))
