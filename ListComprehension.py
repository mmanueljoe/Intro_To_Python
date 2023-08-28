
x = [1,2,3,4,5,6]

listComp = [i * i for i in x]

print(listComp)

l = lambda xList : [i * i for i in xList]
print(l([1,2]))