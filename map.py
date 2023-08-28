def squares(x):
    return x * x

numbers = []
def squareMap():   
    for i in range(1,21):
        numbers.append(i)
    # print(list(map(squares,numbers)))
    sq  = list(map(squares,numbers))
    for x in sq:
        print

squareMap()
print(type(list(map(squares,numbers))))


