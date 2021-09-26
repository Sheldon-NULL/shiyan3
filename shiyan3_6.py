a,b = map(int,input().split(' '))
def gbs(m,n):
    if(m < n):
        m,n = m,n
    else:pass
    i = 0
    i = m % n
    while(i != 0):
        m = n
        n = i
        i = m % n
    return n
print(a * b // gbs(a,b),gbs(a,b))
