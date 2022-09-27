from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index, number in enumerate(nums):
        for i in range(index + 1, len(nums)):
            if number + nums[i] == target:
                return [index, i]
