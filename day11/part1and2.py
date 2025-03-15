from typing import TextIO
from collections import Counter

INPUT: str = 'input.txt'

def get_blink_limit() -> int:
    return int(input('Enter the number of blinks: '))

def evaluate_value(value: int) -> list[int]:
    if value == 0:
        return [1]
    if len(str(value)) % 2 == 0:
        str_val: str = str(value)
        index: int = len(str_val) // 2
        return [int(str_val[:index]), int(str_val[index:])]
    return [value * 2024]

def parse_values(values: Counter, limit: int) -> int:
    for _ in range(limit):
        number: Counter = Counter()
        for value, count in values.items():
            evaluated_values: list[int] = evaluate_value(value)
            for x in evaluated_values:
                number[x] += count
        values=number
    return sum(values.values())

def parse_file(file: TextIO) -> int:
    limit: int = get_blink_limit()
    values: list[int] = [int(x) for x in file.readline().split()]
    return parse_values(Counter(values), limit)

def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_file(file)
    print(f'The answer is {answer}.')

if __name__ == '__main__':
    main()
