xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())

area = (xa - xc)*(yb - ya) - (xa - xb)*(yc - ya)
print("The area of the given triangle is:",(1/2)*(abs(area)))

