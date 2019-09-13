a = int(input("Pick an integer between 1 and 4000\n"))
b = a
values = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
         [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
         [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
         [   1, 'I']]

ro = ""
i = 0
while a > 0:
	while values[i][0] > a: i+=1
	ro += values[i][1]
	a -= values[i][0]
print("\nArabic --> Roman\n",b,"\t  ",ro)
