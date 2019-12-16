class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums == None or len(nums) < 1:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] <= nums[end]:
                end = end - 1
            else:
                start = start + 1
        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]