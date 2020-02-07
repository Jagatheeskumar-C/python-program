n=int(input())
for i in range(1,n+1,2):
    b=n-i//2
    print(' '*b+"*"*i+' '*b)
for i in range(1,n,2)[::-1]:
    b=n-i//2
    print(' '*b+"*"*i+' '*b)    
    
    input=5
    
    output
      *
    * * *
   * * * * *
    * * *
      *
