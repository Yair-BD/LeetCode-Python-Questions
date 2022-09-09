import time
start_time = time.time()

def smal(list = []):
    dic = {}
    list_of_times = []
    for i in range(0,len(list)):
        count = 0
        for j in range(0,len(list)):
            if list[i] > list[j] and i != j:
                count += 1
        list_of_times.append(count)
    return list_of_times

def small(ls = []):

    sordet_ls = sorted(ls)
    print(ls)
    print(sordet_ls)
    for i in range(len(ls)):
        ls[i] = list(sordet_ls).index(ls[i])
    return ls

def smalll(list = []):
    sorted_num = sorted(list, reverse=True)
    print(sorted_num)
    small_count = {}
    for i in range(len(sorted_num) -1):
        cur_number = sorted_num[i]
        next_number = sorted_num[i+1]
        if cur_number > next_number:
            remain = len(sorted_num)-(i+1) 
            small_count[cur_number]= remain
    small_count[sorted_num[-1]] = 0

    output = []
    for num in list:
        output.append(small_count[num])

    return output

listt = [8,1,2,2,3]
print(smalll(listt))

print("\n"+"\n"+"Process finished --- %s seconds ---" % (time.time() - start_time))
