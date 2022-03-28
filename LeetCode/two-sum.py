class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, fst in enumerate(nums):
            for j, scd in enumerate(nums[i+1:]):
                if fst + scd == target:
                    return [i, i+(j+1)]
        return None

s = Solution()
print(s.twoSum([1,2,3,4,5],3))

