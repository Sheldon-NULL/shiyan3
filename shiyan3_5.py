a,b=map(int,input().split(" "))
sum=4
def js(x):
    global sum
    if(x==1):return b
    else:pass
    p,q=4,44
    while(x!=1):
        p=q
        q=q*10+b
        x-=1  
        sum+=p
    return sum

print(js(a))