a=input("enter car name:")
a1=input("customer name:")
a2=input("driver name:")
date_input = input("Enter date (DD/MM/YYYY): ")
date_input=input("Enter pick up date(DD/MM/YYYY): ")
date_input=input("Enter drop date(DD/MM/YYYY):")
a0=float(input("enter the advance:"))
a=="sedan"
a=="innova"
a=="ertiga"
if a=="sedan":
	print("day rent is 1400")
	num=float(input("how many days:"))
	num1=float(input("how many kilometers:"))
	numbers = input("Enter the Toll and parking: ")
	num2=int(input("enter the hills:"))
	num3=int(input("enter the permit:"))
	numbers = list(map(int, numbers.split()))
	result = sum(numbers)
	print("Sum:", result)

	default=8
	default_value=1400
	print("rent is :",default_value*num)
	d=default_value*num
		
	print("fule charge is:",default*num1)
	e=default*num1
	f=d+e+result+num2+num3
	print("Total amount is",f)
	g=f-a0
	print("Total cash is:",g)

elif a=="innova":
	print("day rent is 2000")
	num=float(input("how many days:"))
	num1=float(input("how many kilometers:"))
	numbers = input("Enter the Toll and parking: ")
	num2=int(input("enter the hills:"))
	num3=int(input("enter the permit:"))
	numbers = list(map(int, numbers.split()))
	result = sum(numbers)
	print("Sum:", result)

	default=11
	default_value=2000
	print("rent is :",default_value*num)
	a22=default_value*num
	print("fule charge is:",default*num1)
	a33=default*num1
	a44=a22+a33+result+num2+num3
	print("Total value is:",a44)
	h=a44-a0
	print("the cash is:",h)


elif a=="ertiga":
	print("day rent is 1900")
	num=float(input("how many days:"))
	num1=float(input("how many kilometers:"))
	numbers = input("Enter the Toll and parking: ")
	num2=int(input("enter the hills:"))
	num3=int(input("enter the permit:"))
	numbers = list(map(int, numbers.split()))
	result = sum(numbers)
	print("Sum:", result)

	default=10
	default_value=1900
	print("rent is :",default_value*num)
	a5=default_value*num
	print("fule charge is:",default*num1)	
	a6=default*num1
	a7=a5+a6+result+num2+num3
	print("Total Amount is:",a7)
	i=a7-a0
	print("the cash is:",i)
	

elif a=="crysta":
	print("day rent is 2400")
	num=float(input("how many days:"))
	num1=float(input("how many kilometers:"))
	numbers = input("Enter the Toll  and parking: ")
	num2=int(input("enter the hills:"))
	num3=int(input("enter the permit:"))
	numbers = list(map(int, numbers.split()))
	result = sum(numbers)
	print("Sum:", result)

	default=14
	default_value=2400
	print("charge is :",default_value*num)
	a8=default_value*num
	a9=default*num
	print("fule charge is:",default*num1)
	a10=a8+a9+result+num2+num3
	print("total amount is:",a10)
	a11=a10-a0
	print("the cash is:",a11)
	