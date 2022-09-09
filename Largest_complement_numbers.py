list = [1,4,-1,-6,6,-4,2,-1,0]
bigest = sorted(list)
print(bigest)
for i in bigest:
    if abs(i) in bigest:
        big = i
    if i > 0 :
        print(big)
        break