n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(0,n):
    if(i%2==1):
        s=s+l[i]
for j in range(0,n):
    if(j%2==0):
        s1=s1+l[j]
print(abs(s-s1))