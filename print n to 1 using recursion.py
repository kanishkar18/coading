#print n to 1 using recursion
def pri(n):
    if(n==0):
        return
    else:
        print(n)
        n=n-1
        pri(n)
        
 
pri(5)   