points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
arrow, last_arrow = 0, float("-inf")
points.sort(key=lambda x : x[1])

for start, end in points:
    if start > last_arrow:
        arrow +=1
        last_arrow = end

print(arrow)