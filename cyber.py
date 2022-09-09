
def solution(A):
    curent_height = A[0]
    prev_height = 0
    castels = 1
    p_index = 0# get the last p to build there a castel
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
        

    return castels

