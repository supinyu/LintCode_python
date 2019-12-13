class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]

