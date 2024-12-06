from typing import TextIO

INPUT: str = "input.txt"


# Perform a rule check on an individual update.
# If invalid, attempt to correct it and return the middle page number of the corrected update.
def check_update(rules: list[tuple[int, int]], update: list[int], corrected=False) -> int:
    page: int = 0
    while page < len(update):
        for rule in rules:
            if update[page] != rule[0]:
                continue
            if rule[1] not in update:
                continue
            if update.index(rule[1]) < page:
                update.insert(update.index(rule[0])-1, update.pop(update.index(rule[0])))
                return check_update(rules, update, corrected=True)
        page += 1
    if corrected is True:
        return update[int((len(update)-1)/2)]
    else:
        return 0


# Iterate through the list and perform the rule check
def check_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    answer: int = 0
    for update in updates:
        answer += check_update(rules, update)
    return answer


# Parse the updates
def get_updates(updates: list[str]) -> list[list[int]]:
    parsed_updates: list[list[int]] = list()
    for update in updates:
        parsed_update: list[int] = list()
        split: list[str] = update.split(",")
        for page in split:
            parsed_update.append(int(page))
        parsed_updates.append(parsed_update)
    return parsed_updates


# Parse the page rules
def get_rules(rules: list[str]) -> list[tuple[int, int]]:
    parsed_rules: list[tuple[int, int]] = list()
    for rule in rules:
        split: list[str] = rule.split("|")
        parsed_rules.append((int(split[0]), int(split[1])))
    return parsed_rules


# Parse the page by breaking it into individual lines
def parse_page(file: TextIO) -> int:
    first_half: list[str] = list()
    second_half: list[str] = list()
    flag: bool = False
    for line in file:
        if line.strip() == "":
            flag = True
            continue
        if flag is False:
            first_half.append(line.strip())
        else:
            second_half.append(line.strip())
    rules: list[tuple[int, int]] = get_rules(first_half)
    updates: list[list[int]] = get_updates(second_half)
    return check_updates(rules, updates)


# Main function - Read and parse input, and print answer
def main() -> None:
    file: TextIO = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is {answer}.")


# Main function - Read and parse input, and print answer
if __name__ == "__main__":
    main()
