#by JAFF 
#https://github.com/JAFF-CYBERTHEIF
def move_zeros(array):
    i=0
    j=0
#loop to detect and delete 0's
    while i< len(array):
        if array[i]==0:
            del array[i]
            j+=1
        else:
            i+=1
# loop to append the deleted 0's at the end of the array
    for k in range(j):
        array.append(0)
           
    return array
  
print("enter array as space seperated numbers") 
ar = list(map(int, input().strip().split(' ')))
print(move_zeros(ar))
