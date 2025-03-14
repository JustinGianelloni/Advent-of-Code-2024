import itertools
from typing import TextIO
from itertools import product

INPUT: str = 'input.txt'

def evaluate_expression(expression: str) -> int:
    tokens: list[str] = expression.split()
    result: int = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operator: str = tokens[i]
        number: int = int(tokens[i+1])
        match operator:
            case '+':
                result += number
            case '*':
                result *= number
    return result

def generate_expressions(numbers: list[int]) -> list[str]:
    operators: int = len(numbers) - 1
    combinations: product = itertools.product('+*', repeat=operators)
    expressions: list[str] = []
    for operator in combinations:
        expression: str = str(numbers[0])
        for i in range(1, len(numbers)):
            expression += f' {operator[i-1]} {numbers[i]}'
        expressions.append(expression)
    return expressions

def test_expressions(value: int, values: str) -> int:
    numbers: list[int] = [int(x) for x in values.split()]
    expressions: list[str] = generate_expressions(numbers)
    for expression in expressions:
        if evaluate_expression(expression) == value:
            return value
    return 0

def parse_line(line: str) -> int:
    split: list[str] = line.split(': ')
    value: int = int(split[0])
    return test_expressions(value, split[1])

def parse_file(file: TextIO) -> int:
    lines: list[str] = file.readlines()
    answer: int = 0
    for line in lines:
        answer += parse_line(line)
    return answer

def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_file(file)
    print(f'The answer is: {answer}.')

if __name__ == '__main__':
    main()
