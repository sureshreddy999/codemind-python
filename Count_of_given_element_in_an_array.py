n=int(input())
l=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if l[i]==s:
        c+=1
print(c)
