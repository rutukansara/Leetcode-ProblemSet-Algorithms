class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n+1):
            if i%m!=0:
                num1 += i
            elif i %m==0:
                num2+= i
                # print(i)
        return num1-num2