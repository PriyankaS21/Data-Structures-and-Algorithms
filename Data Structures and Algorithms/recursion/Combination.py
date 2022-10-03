
def fact(n):
    res=1
    for i in range(2, n+1):
        res = res*i
    return res

def Combination(n, r):
    return (fact(n)/(fact(r) * fact(n-r)))

n = 5
r = 3
print(int(Combination(n, r)))