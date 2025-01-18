class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            
            if target < nums[mid]:
                right = mid - 1

        return left