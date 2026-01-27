'''a=[1,1,2,3,4,5,5,5]
b=[]
for i in a:
    if not(a[i] in b):
        b.append(a[i])
print(b)'''

#tuple
'''
t1=(1,2,3,4,5)
t2=("apple","banana","cherry")
t3=(1,"hello",3.14,True)
print("First :",t1[0])
print("silice :",t1[1:4])
t4=(6,7,8)
print("concat :",t1+t4)
print("Repeat :",t2*2)'''

#conversion
'''
print("Tuple from list :",tuple([1,2,3]))
print("Tuple from string :",tuple("Python"))
'''
#function returning tuple
'''def stats(a,b):
    return(a+b,a-b,a*b,a/b)
print("stats tuple :",stats(10,3))'''
'''n=(5,4,3,5,6,5,7,8,9)
print("Length :",len(n))
print("Max :",max(n))
print("Min :",min(n))
print("Sum :",sum(n))
print("Count :",n.count(5))
print("Index :",n.index(9))
print("Sorted :",sorted(n))'''

#set
'''
s={1,2,3}
print(s)'''
#find
'''
s={"apple","banana","cherry"}
print("banana"in s)'''

#add & updata
'''s={1,3,4}
#s.add(2)
#print(s)
s.update([2,3,4])
print(s)'''
#remove
'''
s={"apple","banana","cherry"}
s.remove("banana")'''
#union,intersection
'''a={1,2,3,56,6}
b={2,3,1,2,5,7,8,9}
print(a.intersection(b))
a.intersection_update(b)
print(a)'''
#difference,symmetric difference
'''
s1={1,2,3,4,5}
s2={3,4,5,6,7,8}
#print(s1.symmetric_difference(s2))
print(s1.difference(s2))'''

#dictionary
'''d={"key1":"value1","key1":"value2","key3":"value3"}
print(d)

user={"name":"Ram","age":25,"city":"Salem"}
print(user)
#access method
print(user["name"])
print(user.get("age"))
for i in user:
    print(i,":",user[i])
print(user.keys())
print(user.values())
print(user.items())
#user["name"]="Anil"
#print(user)
#user.update({"age":22})
#user.pop("city")
#user.clear()
print(user)
#mulit-dimensional dictionary
students={"str1":{"name":"Ram","age":25,},
          "str2":{"name":"Anu","age":22}}
print(students["str1"])'''

#functions

def demo():
    a=10
    b=20
    print(a+b)
def add(a,b):
    print(a)
    print(b)
    print(a+b)
#add(23,67)

#reverce the number or string
def rev(n):
    n=str(n)
    print(n[::-1])
#rev(2345653)
#rev("hello")
def palindrome(s):
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
#palindrome("mom")
def countdigits(n):
     count=0
     while n>0:
         n//=10
         count+=1
     print(count)
#countdigits(1000)
def stringcount(a):
    count=0
    for i in a:
        count+=1
    print(count)
#stringcount("alphabet")










