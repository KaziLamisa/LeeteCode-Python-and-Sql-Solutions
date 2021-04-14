# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
#  
# 
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# 
# Input: nums = []
# Output: []
# Example 3:
# 
# Input: nums = [0]
# Output: []
# 
# 



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        if len(nums)<3 or min(nums)>0 or max(nums)<0:
            return res
        
        nums=sorted(nums)
        
        for i in range(len(nums)-2):
            
            if i==0 or ( i>0 and nums[i]!=nums[i-1]) :
                low = i+1
                high = len(nums)-1
                target = 0-nums[i]
            
                while(low<high):
                    if nums[low]+nums[high]==target:
                        res.append([nums[i],nums[low],nums[high]])
                        low+=1
                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                    elif nums[low]+nums[high]>target:
                        high-=1
                    else:
                        low+=1
                    
        res.sort()
        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print s.threeSum(nums)
        

