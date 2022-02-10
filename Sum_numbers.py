r = [3,4,5]
t = []
magic = lambda numbers : int("".join(str(i) for i in numbers[::-1]))
r, t = magic(r), magic(t)
final =[int(i) for i in list(str(r+t))][::-1]
print(magic(t))