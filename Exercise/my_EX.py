from re import I


def try_me(value):

    for i in value:
 
        if i % 3 == 0:
            x=print ('Strive')

        elif i % 5 == 0:
            y=print('School')
        
        elif (i % 3 == 0 and i % 5 == 0):
            z=print("Strive School")
        
        else:
            w= print(i)
    return x,y,z,w
value =[3,5,15,1] 

try_me(value)