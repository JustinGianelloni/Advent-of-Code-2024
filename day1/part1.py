from typing import TextIO

INPUT: str = "input.txt"


# Sort and compare the columns to calculate the answer
def compare_columns(col_a: list[int], col_b: list[int]) -> int:
    col_a.sort()
    col_b.sort()
    length: int = len(col_a)
    i: int = 0
    answer: int = 0
    while i < length:
        answer += abs(col_a[i] - col_b[i])
        i += 1
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
