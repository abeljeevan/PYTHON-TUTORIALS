#WAP IN PYTHON TO CREATE A LIST OF 'N' NUMBERS THEN GENERATE A NEW LIST BY SELECTING NUMBER FROM THE FIRST LIST WHICH IS DIVISIBLE BY 7
list1=[]
list2=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
        no=int(input("Enter the no:"))
        list1.append(no)
for num in list1:
        if num%7=='0':
                list2.append(num)
print("given list=",list1)
print("Multiples of 7:",list2)                

                
                
                
                
                
                
                

                
                
