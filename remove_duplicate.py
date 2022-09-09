# Problem number 26 leetcode.com
def removeDuplicates( nums: list[int]) -> int:
    i = j = 0
    diff_num = 1
    goint_trough_number = j < len(nums)
    while goint_trough_number:
        if nums[i] == nums[j]:
            j += 1
            goint_trough_number = j < len(nums)
        else:
            diff_num += 1
            i += 1 
            nums[i] = nums[j]
            j += 1 
            goint_trough_number = j < len(nums)
    return diff_num, nums[:diff_num]

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([0,0]))