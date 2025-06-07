import pickle
list=[]
while True:
    studentname=input("enter the name:")
    total=int(input("enter the number:"))
    student={"studentname":"total"}
    list.append(student)
    ch=input("enter the choice:")
    if ch=='0':
        break
file=open("student.dat",'wb')
pickle.dump(list,file)
file.close()
