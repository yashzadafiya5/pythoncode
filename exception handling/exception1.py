 #write a program to accept age from user in years. display message "you are eligible for voting" if age is above or equal to 18



try:
	number = int(input("enter a age"))
	if number >=18:
		print("you are eligible for voting")
	else:
 		print("you are not eligible for voting") 
		
except ValueError:
	print('only numbers are allow')
	