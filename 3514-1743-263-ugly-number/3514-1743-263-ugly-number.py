class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n//2:
                n /= p
        return n == 1