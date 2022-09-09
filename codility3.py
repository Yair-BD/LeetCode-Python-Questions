# find the max and min in the array
# make a array of size max - min + 1 and sett all to ""

def solution(A): # O(size_of_new_array)
    max_meters, min_meters = max(A), min(A) # O(n)
    size_of_new_array = max_meters - min_meters + 1
    if max_meters== min_meters:
        size_of_new_array = max_meters + 1
    new_array = [0]*(size_of_new_array) 
    meters_from_the_used = 0
    deviation = 0
    
    if min_meters < 0: # O(1)
        deviation = abs(min_meters) # O(1)
    print(deviation)
    for index_of_rack in A:
        new_array[index_of_rack + deviation] = ""
    print(new_array)
    
    for index in range(size_of_new_array): # O(size_of_new_array)
        if new_array[index] == "":
            meters_from_the_used = 0
        else:
            meters_from_the_used += 1
            new_array[index] = meters_from_the_used
    
    print(new_array)
       
    meters_from_the_used = 0        
    for index in range(size_of_new_array -1 , -1, -1): # O(size_of_new_array)
        if new_array[index] == "":
            meters_from_the_used = 0
        else:
            meters_from_the_used += 1
            if meters_from_the_used < new_array[index]:
                new_array[index] = meters_from_the_used
    
    print(new_array)

    max_meters_from_the_used = 0
    for distance in new_array: # O(size_of_new_array)
        if distance != "":
            if distance > max_meters_from_the_used:
                max_meters_from_the_used = distance
                
    return max_meters_from_the_used
       
print(solution([5, 5]))