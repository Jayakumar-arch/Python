#file hanndling
'''f=open("sample.txt","w")
f.write("Hello")
f.close()
print("written successfully")

name=input("Enter the file name :")
f=open(f"{name}","w")
f.write("Hello")
f.close()
print("written successfully")

f=open("Sample.txt","a")
f.write("Hiii")
f.close()
print("Written successfully")

f=open("sample.txt","a")
data=input("Enter the data to store :")
f.write(f"\n{data}")
f.close()
print("written successfully")

f=open("sample.txt","a")
print("Name :",f.name)
print("File Status :",f.closed)
print("File mode :",f.mode)
f.close()
print("File mode :",f.closed)

f=open("sample.txt","r")
print(f.read())
f.close()


f=open("sample.txt","r")
#f.write(x)
#print(f.read(1))
#print(f.read(1000))
#print(f.readlines())
o=f.readlines()
for i in o:
    print(i)
f.close()

import os
print(os.getcwd())
print(os.listdir())
os.rename('sample.txt','new name,txt')'''

#Exception
'''
#name error
try:
    a=10
    print(b)
except NameError as n:
    print("That particular variable is not defined")

#zero devision error
try:
    x=0
    y=10
    print(y/x)
except ZeroDivisionError as z:
    print("Not possible to divided")

#keyerror
print("Start")
try:
    a={"name":"Jayakumar"}
    print(a["age"])
#except KeyError as k:
    #print("There is no key")
except Exception as e:
    print("There is a exception raised")
print("end")

#assert

a=5
assert a==50,"a is equal to 5"
print(a)

#Raise

a=3
b=34
if b==0:
    rasiezerodivisionerror("This error is made by me")
c=a+b
d=a-b
e=a/b
try:
    print(c,d,e)
except Exception as e:
    print(e)'''
    


    


