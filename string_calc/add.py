from typing import List


def add(numbers: str) -> int:
    result: int = 0
    if numbers == "":
        return result

    nums: List[int] = numbers.split(",")

    for n in nums:
        result += int(n)

    return result
