
#we will be creating a function for intersection

def intersection(set1, set2):#From the reading, union requires 2 values

    #Creat a new set
    set3 = set()

    #create a loop to iterate through incoming set1
    for i in set1:
        #create if statement to check for similarites between set1 and set2. If similar, add to set three
        if i in set2:
            set3.add(i)#add each individual value to new set3


    #now we have all values in set3, we return it
    return set3

bb = {3,4,5,'f'}
dd = {'r',4,6,78}

print (intersection(bb,dd))