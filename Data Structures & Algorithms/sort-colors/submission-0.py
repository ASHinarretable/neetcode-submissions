class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        mid = 0

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 
        while mid <= r:
            if nums[mid] ==0:
                swap(l ,mid)
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, r) 
                r-= 1       