    
def search( nums=[], target = int) -> int:
        left = 0
        right = len(nums)  -1
        while left<=right:
            mid = (left + right)//2
            num = nums[mid]
            if num == target:
                return mid
            if nums[left] <= nums[mid] :
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
                    
print(search([4, 5, 6, 7, 8, 0, 1, 2], 8))


# 1, 3, 5, 7, 9, 8, 6, 4, 2
list = [1, 3, 5, 7, 9, 8, 6, 4, 2]
tar = 5
        