from typing import List


def extract_numbers(mix_nums: str) -> List[int]:
    all_nums: List[int] = []

    num_strs = mix_nums.split('\n')
    for ns in num_strs:
        all_nums.extend(list(map(int, ns.split(','))))

    return all_nums


def add(numbers: str) -> int:
    result: int = 0
    if numbers == "":
        return result

    nums = extract_numbers(numbers)

    for n in nums:
        result += n

    return result
