
n,a,b=input().split(' ')
a=int(a)
b=int(b)
x=[]
n=int(n)
for _ in range(int(n)):
    x.append(int(input()))
l=[]
def rec(i,s):
    if(i==n//2):
        l.append(s)
        return 0
    rec(i+1,s)
    rec(i+1,s+x[i])
rec(0,0)
l.sort()
def rec2(x,y):
    s=0
    e=len(l)-1
    while(s<=e):
        m=(s+e)//2
        if(l[m]<x):
            s=m+1
        else:
            if(l[m]<=y):
                if(m==0 or l[m-1]<x):
                    break
            e=m-1
    if(s>e):
        return 0
    a=m
    s=0
    e=len(l)-1
    while(s<=e):
        m=(s+e)//2
        if(l[m]<x):
            s=m+1
        else:
            if(l[m]<=y):
                if(m+1==len(l) or l[m+1]>y):
                    break
                s=m+1
            else:
                e=m-1
    return (m-a+1)
                
asq=[0]        
    
def rec1(i,s):
    if(i==n):
        asq[0]+=rec2(a-s,b-s)
        return 0
    rec1(i+1,s)
    rec1(i+1,s+x[i])
rec1(n//2,0)
print(asq[0])
        
        
