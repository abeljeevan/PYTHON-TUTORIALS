#WAP in python to receive upper limit and lower limit, then create a list of multiples of 7 between the given limits
print("MULTIPLES OF 7 BETWEEN THE LIMIT:")
lwr=int(input("Enter lower limit: ")) 
upr=int(input("Enter upper limit: ")) 
list1=[] 
for i in range(lwr,upr+1):
    if i%7==0:
        list1.append(i) 
if len(list1)==0:
    print("No multiples of 7 between the limit")
else:
    print("List of multiples of 7 :",list1)
