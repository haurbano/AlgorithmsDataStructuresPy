from typing import List


class NumberSumTarget:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in dictionary and index != dictionary.get(complement):
                return [index, dictionary.get(complement)]
            dictionary[nums[index]] = index




