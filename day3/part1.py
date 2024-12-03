import re
from typing import TextIO

INPUT: str = "input.txt"


# Parse the page looking for the required pattern, and then calculate the answer
def parse_page(file: TextIO) -> int:
    pattern: re = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches: list = re.findall(pattern, file.read())
    answer: int = 0
    for x, y in matches:
        answer += int(x) * int(y)
    return answer


# Main function - Read and parse input, and print answer
def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is {answer}.")


if __name__ == "__main__":
    main()
