class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            x = 1.0 / x
            n = -n
        ans = 1
        temp = x
        while n != 0:
            if n % 2 != 0:
                ans = ans * temp
            temp = temp * temp
            n = n // 2
        return  ans