num=int(input("enter the value of n:"))
hold=num
sum=0
if num<=0:
	print("enter a positive numeber!")
else:
	while num > 0:
		sum=sum + num
		num=num - 1
		print("sum of first",hold,"natural numbers is: ", sum)		
