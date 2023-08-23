for i in range(1,11):
	print(i)


for j in [1,2,3]:
	print(j)


	
	
for i in range(0,19,2):
	print(i)


for i in range(0,4):
	print("****")



evenList = [0,1,2,3,4,5,6,7,8,9,10]
	
def evens(evenList):
	sum = 0
	for i in evenList:	
		if(i % 2 == 0):
			sum += i
	return sum
	
	
print(evens(evenList))


for i in range(1,8):
	if i <= 4:
		print("*" * i)
	elif(i > 4):
		print("*" * (8 - i))




def values(min,max):
	evenList = []
	i = min
	while(i < max):
		if(i % 2 == 0):
			if(i == min):
				pass
			else:
				evenList.append(i)					
		i += 1
	return evenList



finalEven = values(0,10)

print(finalEven)




ageList = ["andrea","tomi","kelvin"]


def whatAge():
	ages = {}
	for i in ageList:
		age = int(input(f"Hello {i}, what is your age ?: "))
		ages[i] = age
	print(ages)

whatAge()
