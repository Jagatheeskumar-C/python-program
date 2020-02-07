a="3792"
b="5342"
c="1372"
a1=a[0:1]
b1=b[0:1]
c1=c[0:1]
a2=a[1:2]
b2=b[1:2]
c2=c[1:2]
a3=a[2:3]
b3=b[2:3]
c3=c[2:3]
a4=a[3:4]
b4=b[-1]
c4=c[-1]
s=a1+b1+c1
x=sorted(s)
y=sorted(a2+b2+c2)
z=sorted(a3+b3+c3)
w=sorted(a4+b4+c4)
print(x[0]+y[0]+z[0]+w[0])
l1=(x[0]+y[0]+z[0]+w[0])
print(sum(map(int,str(l1))))



in;3792,5342,1372
op:1342,10
