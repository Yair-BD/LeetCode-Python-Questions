
def solution(A): #Time complexity O(N*max_hieght)
    breaking_point = True 
    num_of_brushes = 0
    MAX_STROCKS = 1000000000
    max_hieght = max(A)
    for hieght in range(1, max_hieght + 1):
        breaking_point = True # we started new hieght
        for building in A:
            if building >= hieght:
                if breaking_point: # we started new brush
                    num_of_brushes += 1
                    breaking_point = False
            else:
                breaking_point = True # we need next time to start new brush
        if num_of_brushes >= MAX_STROCKS:
            return -1
    return num_of_brushes

print(solution([1, 1, 1, 1]))
