class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if A == None or len(A) < 1:
            return -1 
        start = 0
        end = len(A) - 1 
        while start + 1 < end:
            mid = start + (end - start)//2
            if A[mid] >  A[mid - 1]:
                start = mid
            elif A[mid + 1] < A[mid]:
                end = mid
            else:
                start = mid
        if A[start] > A[end]:
            return start
        else:
            return end