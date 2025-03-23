import math
from typing import TextIO

INPUT: str = 'input.txt'
TARGET: int = 2000

def mix(value: int, secret: int) -> int:
    return value ^ secret

def prune(secret: int) -> int:
    return secret % 16777216

def step_1(secret: int) -> int:
    return prune(mix(secret * 64, secret))

def step_2(secret: int) -> int:
    return prune(mix(math.floor(secret / 32), secret))

def step_3(secret: int) -> int:
    return prune(mix(secret * 2048, secret))

def evolve(secret: int) -> int:
    secret = step_1(secret)
    secret = step_2(secret)
    secret = step_3(secret)
    return secret

def generate_target(secret: int) -> int:
    for _ in range(TARGET):
        secret = evolve(secret)
    return secret

def parse_file(file: TextIO) -> int:
    answer: int = 0
    lines: list[int] = [int(x) for x in file.readlines()]
    for line in lines:
        answer += generate_target(line)
    return answer

def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_file(file)
    print(f'The answer is: {answer}.')

if __name__ == '__main__':
    main()
