
from array import *

value = array('i',[1,2,3,4,5,6,7,8,9,10]) 

#print(value[0]) 

# for i in range(len(value)):
#     print(value[i])


for i in range(len(value)):
    if i / 3 == 1:
        print ('Strive')
    elif i / 5 == 1:
        print('School')
    elif (i / 3 == 1 and i / 5 == 1):
        print("Strive School")
    else:
        print(value[i])