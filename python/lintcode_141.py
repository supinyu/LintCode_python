class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        else:
            return start