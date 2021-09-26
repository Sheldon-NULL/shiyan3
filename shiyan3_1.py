import math
x=eval(input())
#一句单分支
if(x<0):
    print(-(x/(x*x+1)))
else:
    print(math.sqrt(x+1))
#两句单分支
if(x<0):
    print(-(x/(x*x+1)))
else:
    pass
if(x>=0):
    print(math.sqrt(x+1))
else:
    pass
#双分支结构
if(x<0):
    print(-(x/(x*x+1)))
elif(x>=0):
      print(math.sqrt(x+1))
else:
    pass
#条件运算符
print(-(x/(x*x+1))if x<0 else math.sqrt(x+1))