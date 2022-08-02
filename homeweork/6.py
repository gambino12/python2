'''
#Мимикрия
values = [1,23,5,'yes']
transformation = lambda x: x
transformed_values = list(map(transformation,values))
if values == transformed_values:
    print('ok')
else:print('nea')
#Самая далекая планета

#пам парам
line = input().lower()
lines = line.split()
lst = [sum(x in 'уеыаоэяию' for x in lin)
for lin in lines] 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
print(res)

#все равны как на подбор
def same_by(characteristic,object):
    main = characteristic(object[0])
    for i in range(len(object)):
        if characteristic(object[i]) != main: return False
    return True


values =[3,5,7,9]
if same_by(lambda x: x % 2 , values):print('same')
else:print('different')

#незнаю названия
def print_operation_table(operation, num_rows=9, num_colums=9):
    for i in range(1,num_colums+1):    
        for j in  range(1,num_rows+1):
            print(operation(i,j),end = '-' ) 
        print('\n')       
print_operation_table(lambda x, y: x * y)
''' 