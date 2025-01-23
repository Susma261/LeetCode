# Method 1: Using XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result ^= num
        return result

# Method 2: Using Set

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=set()
        for i in range(len(nums)):
            if nums[i] in count:
                count.remove(nums[i])
            else:
                count.add(nums[i])
        return count.pop()

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)

# Method 3: Using Dict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        for k,v in count.items():
            if v == 1:
                return k



        