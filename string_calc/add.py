from typing import List


def extract_delimeter(mix_nums: str) -> str:
    delim = ','
    if len(mix_nums) >= 3:
        if mix_nums.startswith("//"):
            delim = mix_nums[2]

    return delim


def extract_numbers(mix_nums: str) -> List[int]:
    all_nums: List[int] = []

    delimeter = extract_delimeter(mix_nums)

    num_strs = mix_nums.strip('//'+delimeter).split('\n')

    for ns in num_strs:
        if ns:
            all_nums.extend(list(map(int, ns.split(delimeter))))

    return all_nums


def add(numbers: str) -> int:
    result: int = 0
    if numbers == "":
        return result

    nums = extract_numbers(numbers)
    neg_nums = []

    for n in nums:
        if n < 0:
            neg_nums.append(str(n))
        else:
            result += n

    if len(neg_nums):
        raise ValueError(f"negative numbers not allowed <{','.join(neg_nums)}>")

    return result
