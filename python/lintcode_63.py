class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """

    def search(self, A, target):
        # write your code here
        if A == None or len(A) < 1:
            return False
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return True
            if A[mid] > A[start]:
                if target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[end]:
                if target <= A[end] and target > A[mid]:
                    start = mid
                else:
                    end = mid
            else:
                start = start + 1
        if A[start] == target:
            return True
        elif A[end] == target:
            return True
        else:
            return False
