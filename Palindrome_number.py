
def is_pal_str(x: int):
    x = str(x)
    end = len(x)-1
    start = 0
    while end >= start:
        if x[start] != x[end]:
            return False
        end -= 1
        start += 1
    return True



def isPalindrome(x):
        if x<0:
            return False
        l = []
        sifra = -1
        while x != 0:
            sifra = x%10
            l.append(sifra)
            sifra = x//10
            x = x//10
        end = len(l)-1
        start = 0
        while end >= start:
            if l[start] != l[end]:
                return False
            end -= 1
            start += 1
        return True
    
    

def IsPalindromee(x):
    
        if(x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revertedNumber = 0
        while(x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        
        return x == revertedNumber or x == revertedNumber/10


print("yair")
print(IsPalindromee(11))