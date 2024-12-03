import re
from typing import TextIO

INPUT: str = "input.txt"


# Parse the page looking for the required pattern, and then calculate the answer
def parse_page(file: TextIO) -> int:
    pattern: re = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern, file.read())
    answer: int = 0
    flag: bool = True
    for match in matches:
        if match.group(0) == "do()":
            flag = True
        elif match.group(0) == "don't()":
            flag = False
        elif match.group(0).startswith("mul") and flag is True:
            x: int = int(match.group(1))
            y: int = int(match.group(2))
            answer += x * y
    return answer


# Main function - Read and parse input, and print answer
def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is {answer}.")


if __name__ == "__main__":
    main()
