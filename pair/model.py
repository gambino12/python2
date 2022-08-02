a=0
b=0
c=''
def init(x,y,z):
    global a
    global b
    global c
    a=x
    b=y
    c=z


def operations(a,b,c):
    res=0
    if c=='+':res= a + b
    elif c=='-':res= a - b
    elif c=='*':res= a * b
    elif c=='/':res= a / b
    return res
