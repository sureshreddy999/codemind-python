def reverse(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def prime(k):
    c=0
    for i in range(1,k+1):
        if k%i==0:
            c+=1
    if c==2:
        return True
    return False
n=int(input())
r=reverse(n)
if prime(n)==True and prime(r)==True:
    print("circular prime")
elif prime(n)==True and prime(r)==False:
    print("prime but not a circular prime")
elif prime(n)==False and prime(r)==False:
    print("not prime")
