class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        arr = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]

            for p in self.permute(remaining):
                arr.append([current] + p)

        return arr