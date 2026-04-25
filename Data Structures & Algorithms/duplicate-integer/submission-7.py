class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        for noom in nums:
            if noom in myset:
                return True
            myset.add(noom)
        return False