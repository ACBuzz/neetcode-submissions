class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     seen = set() #defining a variable seen to be set to set(). set() 
     for n in nums:
        if n in seen:
            return True
        seen.add(n)
    
     return False 

    