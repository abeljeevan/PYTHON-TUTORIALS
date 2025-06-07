#WAP A PROGRAM TO READ ANY STRING FROM THE USER AND CREATE A LIST OF WORDS THAT STARTS WITH LETTER A
words=[]
str=input("Enter a statement:")
listwords=str.split()
for word in listwords:
    low=word.lower()
    if low[0]=='a':
        words.append(word)
print("given string:",str)
print("words start with letter A/A:",words)

    
