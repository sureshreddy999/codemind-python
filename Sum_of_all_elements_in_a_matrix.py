r,c=map(int,input().split())
mat=[]
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sum(sub_list))
print(sum(mat))