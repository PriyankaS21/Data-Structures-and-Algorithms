# power program
def p(b, e):
    if (e == 1):
        return b
    if (e != 1):
        return (b*p(b, e-1))

b = 2
e = 3
print("power is: ", p(b,e))