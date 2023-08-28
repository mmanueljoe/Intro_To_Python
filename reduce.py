from functools import reduce

def add(x,y):
    return x  +  y

def multiply(x,y):
    return x  *  y

sq = [1,2,3,4,5,6,7,8,9,10]

tens = [10,20,30,40,50,60,70,80,90,100]

dic = {'one':1,'two':2,'three':3}

a = ('ama',24,'kojo',23)

c,d,e,f = a

b = (1,2,3,4,5)
print(reduce(add,sq))

print(reduce(multiply,tens))

print(reduce(add,dic.values()))

print(reduce(add,b))

print(reduce(add,[a]))