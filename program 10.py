#Program to create and read a text file line by line and display each word
with open("File1.txt","w")as f1:
    while True:
        str1=input("Enter connection to file:")
        f1.writelines(str1)
        f1.write('/n')
        ch=input("Enter 0 to stop adding:")
        if ch=='0':
            break
f2=open("file1.txt")
for line in f2:
    words=line.split()
    for w in words:
        print(w+'#',end='#')
f2.close()

                 
