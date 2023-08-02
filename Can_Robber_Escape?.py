n=int(input())
lst=map(int,input().split())
k=0
for i in lst:
    if i>=n:
        print("NO")
        k=1
        break
if(k!=1):
    print("YES")