a = 0
b = 1
n = 30
print()
print("1 :",b)
for x in range(2,n+1):
	c = a + b
	a = b
	b = c
	print(x,":",b)
