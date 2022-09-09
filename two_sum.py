class Solution:
    """_summary_ 
    Get an array of numbers and target
    returns the index of the two numbers that indices the sum of target
    """
    def twoSum(nums, target) :
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
    print(twoSum([3, 3], 6))