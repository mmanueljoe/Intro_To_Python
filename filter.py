def is_even(i):
    return i % 2 == 0

sq = [1,2,3,4,5,6,7,8]
print(list(filter(is_even,sq)))



def too_old(x): 
    return x > 30

ages =[22,25,29,34,56,24,12]
print(list(filter(too_old,ages)))