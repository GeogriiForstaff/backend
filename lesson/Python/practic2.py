'leetcod 1. Two Sum'


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        output = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)

        return output