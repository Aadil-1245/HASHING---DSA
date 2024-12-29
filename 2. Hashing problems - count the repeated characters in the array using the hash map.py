# Hashing 
# Count the characters in the array that has been repeated 
def fun(c,n):
    global cnt 
    for i in range(len(n[0])):
        if n[0][i] == c[0]:
            cnt += 1 
    return cnt 
cnt = 0 
n = ["abcdaabcddfd"]
c = "a"
print(fun(c,n))