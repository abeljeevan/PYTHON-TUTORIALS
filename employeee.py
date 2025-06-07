import pickle
def employee():
    emp=[]
    fh1=open("employee.txt","wb")
    while True:
        empno=int(input("Enter the employee number:"))
        empname=input("Enter the employee name:")
        empdept=input("Enter the employee department:")
        emp.append([empno,empname,empdept])
        ch=input("Enter '0' to stop:")
        if ch=="0":
            break
    pickle.dump(emp,fh1)
    fh1.close()
    print("data added successfully")

employee()
   
                
