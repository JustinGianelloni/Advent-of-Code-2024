from typing import TextIO

INPUT: str = "input.txt"


# Evaluate if the numbers in the report are increasing/decreasing "gradually"
def is_gradual(report: list[int]) -> bool:
    length: int = len(report)
    i: int = 1
    while i < length:
        diff: int = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False
        i += 1
    return True


# Evaluate if the numbers in the report are decreasing
def is_decreasing(report: list[int]) -> bool:
    length: int = len(report)
    i: int = 1
    while i < length:
        if not report[i] - report[i-1] < 0:
            return False
        i += 1
    return True


# Evaluate if the numbers in the report are increasing
def is_increasing(report: list[int]) -> bool:
    length: int = len(report)
    i: int = 1
    while i < length:
        if not report[i] - report[i-1] > 0:
            return False
        i += 1
    return True


# Evaluate each line to determine if it is "safe"
def is_report_safe(report: list[int]) -> bool:
    if is_increasing(report) is False and is_decreasing(report) is False:
        return False
    if is_gradual(report) is False:
        return False
    return True


# Run each report once as-is, and then without each value until true or all possibilities exhausted
def is_report_really_safe(line: str) -> bool:
    report: list[int] = [int(item) for item in line.split(" ")]
    if is_report_safe(report):
        return True
    length: int = len(report)
    i: int = 0
    while i < length:
        tweaked_report: list[int] = list(report)
        tweaked_report.pop(i)
        if is_report_safe(tweaked_report):
            return True
        i += 1
    return False


# Parse the page by breaking it into individual lines
def parse_page(file: TextIO) -> int:
    lines: list[str] = file.readlines()
    answer: int = 0
    for line in lines:
        if is_report_really_safe(line):
            answer += 1
    return answer


# Main function - Read and parse input, and print answer
def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is {answer}.")


# Main function - Read and parse input, and print answer
if __name__ == "__main__":
    main()
