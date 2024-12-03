from typing import TextIO

INPUT: str = "input.txt"


# Get a dictionary with the frequency of each number
def get_frequency(col: list[int]) -> dict[int, int]:
    freq: dict[int, int] = dict()
    for num in col:
        try:
            freq[num] += 1
        except KeyError:
            freq[num] = 1
    return freq


# Multiply each number in the left column by its frequency in the right to calculate the answer.
def compare_columns(col_a: list[int], col_b: list[int]) -> int:
    freq: dict[int, int] = get_frequency(col_b)
    answer: int = 0
    for num in col_a:
        try:
            answer += num * freq[num]
        except KeyError:
            pass
    return answer


# Split the lines into two lists of integers
def split_columns(lines: list[str]) -> int:
    col_a: list[int] = list()
    col_b: list[int] = list()
    for line in lines:
        split: list[str] = line.split("   ")
        col_a.append(int(split[0]))
        col_b.append(int(split[1]))
    return compare_columns(col_a, col_b)


# Parse the page by breaking it into individual lines
def parse_page(file: TextIO) -> int:
    lines: list[str] = file.readlines()
    return split_columns(lines)


# Main function - Read and parse input, and print answer
def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is {answer}.")


if __name__ == "__main__":
    main()
