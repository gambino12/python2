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
    x = 0
    if c=='+':x=lambda a, b: a + b
    if c=='-':x=lambda a, b: a - b
    if c=='*':x=lambda a, b: a * b
    if c=='/':x=lambda a, b: a / b
    return x