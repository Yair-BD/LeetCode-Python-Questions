class Solution:
    """_summary_ 
    Get an array of numbers and target
    returns the index of the two numbers that indices the sum of target
    """
    def twoSum(self, nums, target) :
        sort_nums = sorted(nums) #O (n(Logn))
        i, j = 0, len(nums) - 1
        while  i <= j: # O (n)
            if sort_nums[i] + sort_nums[j] > target:
                j -= 1
            elif sort_nums[i] + sort_nums[j] < target:
                i +=1
            elif sort_nums[i] + sort_nums[j] == target:
                y = nums.index(sort_nums[i])
                nums[nums.index(sort_nums[i])] = -0.5
                x =  nums.index(sort_nums[j])
                
                return [y, x]
    
    
    def better_two_sum(self, nums, target):
        """_summary_ 
        Get an array of numbers and target
        returns the index of the two numbers that indices the sum of target
        """
        dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [dict[diff], i]
            dict[n] = i
            
opsion1 = Solution()

print(opsion1.better_two_sum([3,3], 6))