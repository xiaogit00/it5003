from collections import defaultdict 
from typing import List

class Solution:
    def twoSums(self, nums: List[int]): # O((2N)^3??)
        m = len(nums)
        res = defaultdict(list)
        for i in range(m-1): # O(N^2)
            for j in range(i+1, m):
                sum = nums[i] + nums[j]
                if (nums[i], nums[j]) not in res[sum] and (nums[j], nums[i]) not in res[sum]: # O(2N)
                    res[sum].append((nums[i], nums[j]))
        return res
    def contains3Zeros(self, nums): #O(N)
        k = sorted(nums)
        if k[0] == 0 and k[1] == 0 and k[2] == 0:
            return True
        else:
            return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negNums = [i for i in nums if i < 0] #O(N)
        posNums = [i for i in nums if i >= 0] #O(N)
        if len(posNums) == 0:
            return []
        if len(negNums) == 0:
            if self.contains3Zeros(posNums): #O(N)
                return [[0, 0, 0]]
            else:
                return []
        #[-1,0,1,0]
        negOne = list(set(negNums)) #O(N)
        posOne = list(set(posNums)) #O(N)
        negTwo = self.twoSums(negNums) # O(N^3)
        posTwo = self.twoSums(posNums) # O(N^3)
        print(posTwo)
        res = []
        for num in negOne: #O(N^2)
            if -num in posTwo.keys():
                for pair in posTwo[-num]:    
                    res.append([num, pair[0], pair[1]])
        for num in posOne: #O(N^2)
            if -num in negTwo.keys():
                for pair in negTwo[-num]:
                    res.append([num, pair[0], pair[1]])
        if len(posNums) > 2 and self.contains3Zeros(posNums):
            res.append([0,0,0])
        return res

n = Solution()
nums = [-1,0,1,2,-1,-4]
print(n.threeSum(nums))

'''
Learning: 
1. The main difference between my approach and the model one is that I created a dictionary of 
lists first, and tried to iterate through the dict keys and *then* through the lists. A simpler
method would just be to check within the 2 inner loops whether 2 sums in negative numbers adds 
up to something in the set of positive numbers. Using sets for the lookup elements for O(1) time. 

2. Second, zero handling. I didn't think about the different logical cases it could take, thus 
my zero handling is mixed in with positive number handling. If I separated them out, it'll be 
a lot easier. In this case, you only need to handle 1 zero. If there's 2 zeros, they can't 
add to anything meaningful. If there's 3 zeros, then I'll just need to add 1 case to the ans. 

Overall takeaway? Try to do more things when you are already iterating through some loop. Tuck
expensive operations together - instead of creating another construct, where you might 
have to reiterate again, or waste space complexity. The way to do that is to gain more experience 
and finessing your logical handling. At least I managed to get the 
overall thing right without help. 

'''