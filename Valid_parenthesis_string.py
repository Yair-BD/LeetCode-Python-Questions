def validd(s):
    s = list(s)
    left_bal = 0
    for i in s:
        if i == ")":
           left_bal -= 1
        else :
            left_bal += 1
        if left_bal < 0:
            return False
    if left_bal == 0:
        return True
    
    right_bal = 0
    for i in reversed(s):
        if i == "(":
            right_bal -= 1
        else :
            right_bal += 1
        if right_bal < 0:
            return False
        
    return True

print(validd("((*()*(*)))(*)()()"))


