a=input()
k=int(a)
b=int(a)**2
s=str(b)
c=len(a)
d=len(a)//2
e=s[0:d+1]
f=s[d+1::]
sum=int(e)+int(f)
if(sum==k):
    print("kaprekar number")
else:
    print("not kaprekar number")
