class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if nums == None or k > len(nums):
            return sorted(nums)
        result = [0 for i in range(k)]
        for i in range(k):
            self.heapInsert(result, nums[i], i)
        for i in range(k, len(nums)):
            if result[0] < nums[i]:
                result[0] = nums[i]
                self.heapify(result, 0, k)
        return sorted(result, reverse=True)

    # 需要使用小顶堆
    # 堆顶是最小元素
    # nums[0]是堆顶
    def heapInsert(self,nums, value, index):
        nums[index] = value
        while index != 0:
            parent = (index - 1) // 2
            if nums[parent] > nums[index]:
                nums[parent], nums[index] = nums[index], nums[parent]
                index = parent
            else:
                break
    def heapify(self, nums, index , heapsize):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        while left < heapsize:
            if nums[left] < nums[index]:
                smallest = left
            if right < heapsize and nums[right] < nums[smallest]:
                smallest = right
            if smallest != index:
                nums[smallest] , nums[index] = nums[index] , nums[smallest]
            else:
                break
            index = smallest
            left = index * 2 + 1
            right = index * 2 + 2
