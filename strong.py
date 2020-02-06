import math
a=int(input())
b=str(a)
c=[]
d=[]
for i in range(len(b)):
    c.append(int(b[i]))
    d.append(math.factorial(c[i]))
    e=sum(d)
if e==a:
    print("strong number")
else:
    print("not strong number")
    
    
    
    145=1!+4!+5!=145 yes
    15=1!+5!=121 no
