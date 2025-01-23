# Method 1: Using Dict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for k,v in count.items():
            if v==1:
                return k

# Method 2: Using bitwise operations
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones,two = 0,0
        for num in nums:
            ones = (ones^num) & ~ two
            two = (two^num) & ~ ones
        return ones


        