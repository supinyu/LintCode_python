class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A == None or len(A) < 1:
            return  -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if A[mid] > A[start]:
                if A[mid] == target:
                    return mid
                elif target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[end]:
                if A[mid] == target:
                    return mid
                if target <= A[end] and target > A[mid]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1
