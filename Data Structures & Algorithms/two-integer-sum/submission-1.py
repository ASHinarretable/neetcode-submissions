class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            #hashMap.append(nums[i])
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i