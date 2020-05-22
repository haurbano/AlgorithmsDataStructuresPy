from typing import List


class NumberSumOrderedList:
    dic = {}

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for index in range(len(numbers)):
            num = numbers[index]
            dic[num] = index
            complement = target - num
            if complement in dic and index != dic[complement]:
                return [index, dic[complement]]
            else:
                complementIndex = self.findIndexOf(numbers, complement, 0, len(numbers) - 1)
                if complementIndex != -1 and index != complementIndex:
                    return [index, complementIndex]

    def findIndexOf(self, numbers: List[int], num: int, start: int, end: int) -> int:
        if start > end:
            return -1
        else:
            mid = int((start + end) / 2)
            value = numbers[mid]
            #dict[value] = mid
            if value > num:
                self.findIndexOf(numbers, num, mid + 1, end)
            elif value < num:
                self.findIndexOf(numbers, num, start, mid - 1)
            else:
                return mid
