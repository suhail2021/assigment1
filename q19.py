str1=input("please enter your own string:")
vowels=0
str1.lower()
for i in str1:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		vowels=vowels+1
print("total number of vowels in this string = ",vowels)		