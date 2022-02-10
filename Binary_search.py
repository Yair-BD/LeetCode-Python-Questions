lis = [1,2,3,4,5,6,7,8,9]
target = 6

def search(nums=[], target=int) -> int:
    start = 0
    end = len(nums-1)
    middle = (start + end)//2
    while start<=end:
        middle = (start + end)/2
        num = nums[middle]
        if target ==num:
            return middle
        elif target >num :
            start = middle

        elif target <num :
            end = middle
    return -1
            
