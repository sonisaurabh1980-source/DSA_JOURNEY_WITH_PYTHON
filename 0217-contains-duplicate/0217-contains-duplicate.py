class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        new = set(nums)
        if len(nums)==len(new):
            return False
        else:
            return True    