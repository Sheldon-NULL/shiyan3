
a = eval(input())
str = ""
js=a//2
for j in range(1,a+1,2):
    str = ' ' * (js)
    str+='*' * (j)
    print(str)
    js-=1
    if(js<0):break
    else:pass
js=1
key=a-2
#for j in range(a,0,1):
while(js<=a//2):
    str = ' ' * (js)
    str+='*' * (key)
    key-=2
    print(str)  
    js+=1
 #   if(js>a%2):break
 #  else:pass