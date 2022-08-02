
def init(str):
    global x
    x = str

def search(name,name2,num):
    x = reader()
    for i in x :
        if name == x[i]

    
            

    

def add(data):
    reader
    

def reader ():
    x=[]
    y=[]
    with open(f'storage.txt','r',encoding='utf8') as f1:
        x=f1.readline().lower().split('\n')
        y = x.split(',')
    return x,y
