print("MULTIPLES OF 7 BETWEEN THE LIMIT:")
lwr=int(input("Enter lower limit: "))	#reads upper limit
upr=int(input("Enter upper limit: "))	#reads lower limit
list1=[]	#creates empty list
for i in range(lwr,upr+1):	 if i%7==0:	
list1.append(i)	 if len(list1)==0:
print("No multiples of 7 between the limit") else
print("List of multiples of 7 :",list1)
