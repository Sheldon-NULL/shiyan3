import math
a,b,c = map(float,input().split(' '))
#d=0+1j
delota = b ** 2 - 4 * a * c
if(a == 0 and b == 0):
    print("无解")
elif(a == 0 and b != 0):
    print("X={}".format(-c / b))
elif(delota == 0):
    print("x1=x2={}".format(-b / 2 / a))
elif(delota > 0):
    print("x1={},x2={}".format(-b / 2 / a + math.sqrt(delota) / 2 / a,-b / 2 / a - math.sqrt(delota) / 2 / a))
else:
   print("实部是:{},虚部1={}i,虚部2={}i".format(-b / 2 / a,math.sqrt(-delota) / 2 / a,-math.sqrt(-delota) / 2 / a))
#  print("x1={},x2={}".format(-b/2/a+math.sqrt(-delota)/2/a*d,-b/2/a-math.sqrt(-delota)/2/a)*d)
