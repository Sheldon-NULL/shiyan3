tall,weight = map(float,input().split(" "))
BMI = weight / tall ** 2
print("{:.2f}".format(BMI))

if(BMI <= 18.5):
    print("国际偏瘦，国内偏瘦")
else:pass
if(BMI >= 30):
    print("国际肥胖",end=',')
elif(25 <= BMI < 30):
    print("国际偏胖",end = ',')
elif(18.5 <= BMI < 25):
    print("国际正常",end = ',')
else:pass
if(BMI >= 28):
    print("国内肥胖")
elif(24 <= BMI < 28):
    print("国内偏胖")
elif(18.5 <= BMI < 24):
    print("国内正常")
else:pass

