class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
