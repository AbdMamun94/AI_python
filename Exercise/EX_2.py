x = [4,3,2,1,4,3,2]
check = set()
check_again = set()

for i in x:
    if i in check_again:       
        continue
    if i in check:              
        check.remove(i)        # if i get given num in check that will remove from check. for example index 4 value is 4 it will be remove from check.
        check_again.add(i)      # when any number remove from check that will add here that means in check_again
                                 # So, that means here will add those num which is Duplicate.
    else:
        check.add(i)          # here will add those num which is not duplicate. 
                                 
print(list(check))             