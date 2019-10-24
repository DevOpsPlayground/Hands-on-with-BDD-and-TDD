import json

from src.Calculator import Calculator
from src.Operation import Operation


def main(json_file):
    with open(json_file, 'r') as input_json:
        inputs = (json.load(input_json))["inputs"]
    for string_input in inputs:
        print('Input entered: {}'.format(string_input))
        op = Operation(string_input)
        print(Calculator().validate(op))


if __name__ == '__main__':
    main('test.json')
