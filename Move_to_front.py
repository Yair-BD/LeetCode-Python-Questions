
import time
start_time = time.time()

list = [0,0,1,0,0,3,4,3,2,4,5,5,4,3,3,2,2,5,5,7,8,9,9,9,9,9,9,9,9,9,9,9,8,8,7,7,6,66,6,66666,666555,0,0]
def solution(n=[], k = int):
    if len(list) == 0:
        return None
    else:
        for num in n[:k]:
            n.remove(num)
            n.append(num)
    return n 
    
def solution2(A=[], k = int):
    N = len(A)
    b = [None]*N
    for i in range(0,N):
        b[(k+i)%N] = A[i]
    return b


print("\n"+"\n")
print(solution2(list,6))
print("\n"+"\n")


print("\n"+"\n"+"Process finished --- %s seconds ---" % (time.time() - start_time))
