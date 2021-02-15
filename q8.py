maximum=int(input("please enter the maximum value:"))
oddtotal=0

for number in range(1,maximum+1):
	if(number % 2 !=0):
		print("{0}".format(number))
		oddtotal = oddtotal + number
print("The Sum of odd numbers from 1 to {0} = {1}".format(number, oddtotal))		
