#HASHING  (26/12/24)
# SO We have an Array with the element of 5 
# arr = [ 1,2,3,4,2]
# In this array we have to find how many times the elements has been repeated 
# To find that we are going to write the program
def fun(arr,num):
    cnt = 0 
    for i in range(len(arr)):
        if arr == num : # If the arr == num then we have to add cnt of 1 
            cnt = cnt + 1 # here we are incrementing the number 
    return cnt 
arr = [ 1,2,3,4,2]
num = 1 
print(fun(arr,num))