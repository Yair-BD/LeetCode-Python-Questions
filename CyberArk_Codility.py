
def solution(A):
    curent_height = A[0]
    prev_height = 0
    castels = 1
    p_index = 0 # get
    for p in A:
        p_index += 1
        if p == curent_height:
            continue
        else: # if the next part is higher os lower - there is a chance to vally or hill
            
            if p == prev_height: # we got a hill or a vally
                castels += 1
                curent_height = p
                
            else: # we made another peak up or down and miss vally or hill
                
                prev_height = curent_height
                curent_height = p
        
        if p_index == len(A):
                castels += 1
 
    return castels


a = [2,2,5,2]

print(solution(a))
