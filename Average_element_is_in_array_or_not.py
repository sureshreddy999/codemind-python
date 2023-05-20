n=int(input())
l=list(map(int,input().split()))
s=sum(l)//len(l)
if s in l:
    print("True")
else:
    print("False")