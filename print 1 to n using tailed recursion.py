#print 1 to n using tailed recursion
def pri(n):
    if(n==0):
        return 
    else:
   
        pri(n-1)
        print( n)
        
pri(5)