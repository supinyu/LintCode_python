class Solution:
    """
    @param m: m pillars of your temple.
    @param woods: length of n different wood
    @return: return the maximum height of the temple.
    """

    def buildTemple(self, m, woods):
        # write your code here.
        if m < 1 or len(woods) < 1:
            return 0
        start = min(woods)
        end = max(woods)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.helper(woods, mid) < m:
                end = mid
            else:
                start = mid
        if self.helper(woods, start) >= m:
            return start
        else:
            return end

    def helper(self, woods, eachlen):
        count = 0
        for wood in woods:
            count = count + wood // eachlen
        return count