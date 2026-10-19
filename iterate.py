a=[1,3,5,7,8,10,2]
maxi=-1000
sumi=0
for i in a:
    if i>maxi:
        maxi=i
    sumi+=i
print(maxi,sumi)