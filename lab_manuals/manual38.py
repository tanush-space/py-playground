'''Write a program to perform
•	File creation
•	Reading from a file
•	Copy the contents of one file into another file
'''

f1=open("file1.txt","w")
data=input("Enter text to write in file: ")
f1.write(data)
f1.close()

f1=open("file1.txt","r")
print("Reading from file1:")
content=f1.read()
print(content)
f1.close()

f2=open("file2.txt","w")
f2.write(content)
f2.close()
print("Contents copied to file2.txt")
