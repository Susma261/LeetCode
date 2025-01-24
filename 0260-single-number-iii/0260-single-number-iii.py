# Method 1: Using XOR

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=0
        for num in nums:
            result ^= num
        right= result & -result
        a,b = 0,0
        for num in nums:
            if num & right:
                a ^= num
            else:
                b ^= num
        return[a,b]

# Method 2: Using Set

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = set()
        for num in nums:
            if num in a:
                a.remove(num)
            else:
                a.add(num)
        return list(a)

# Method 3: Using Dict
        
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        return[k for k,v in count.items() if v == 1]

            
                
   
        
        