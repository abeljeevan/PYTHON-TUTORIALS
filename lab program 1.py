With open(“file2.txt”,‟w‟) as f1:
    while True:
    
        str1 = input(“Enter content to file : “)
        f1.writelines(str1)
        f1.write('\n')
        ch = input(“Enter 0 to stop writing : “ )
        if ch == '0':
        break
f2 = open(“file2.txt”)
v,c,u,l,o = 0, 0, 0, 0, 0
data = f2.read()
vowels=[„a‟,‟e‟,‟I‟,‟o‟,‟u‟] # vowels list for check
for ch in data: # for checks char/char
    if ch.isalpha(): # checks for alphabet
if ch.lower() in vowels: # checks for vowels or consonants v+=1
else:
c+=1
if ch.isupper(): # checks for uppercase u+=1
elif ch.islower(): # checks for lowercase l+=1
 



f2.close()
 
else:
 

o+=1
 
print(“Total Vowels in file : “,v)
 
print(“Total Consonants in file : “,c) print(“Total Capital letters in file : “,u) print(“Total Small letters in file : “,l) print(“Total Other characters : “,o)
