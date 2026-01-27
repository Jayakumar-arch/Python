#1.Write a program to print the first N natural numbers. Input : 10 , Output : 1 2 3 4 5 6 7 8 9 10
'''
a=int(input("Enter the number :"))
for a in range(1,a+1):
    print(a,end=" ")'''

#2 first N even natural numbers
'''
a=int(input("Enter the number :"))
for a in range(2,a+2,2):
    print(a,end=" ")'''

#3 The first N odd natural numbers.
'''
a=int(input("Enter the number :"))
for a in range(1,a+2,2):
    print(a,end=" ")'''

#4 print first N multiples of 3.
'''
a=int(input("Enter the number :"))
for a in range(1,a+1,1):
    multiples=3*a
    print("multiples of 3",multiples)'''

#5 print first N multiples of 5
'''
a=int(input("Enter the number :"))
for a in range(1,a+1,1):
    multiples=5*a
    print(multiples)'''

#6 print all the multiples of 2 
'''
a=int(input("Enter the number :"))
for a in range(1,a+1,1):
    multiples=2*a
    print(multiples,end=" ")'''

#7 print all the numbers which are multiples of either 2 or 3
'''
a=int(input("Enter the number :"))
for a in range(1,a+1):
    if a%2==0 or a%3==0:
        print(a,end=" ")'''
#8 print all the numbers which are multiples of either 2, 5 or 7 till N
'''
a=int(input("Enter the number :"))
for a in range(1,a+1):
    if a%2==0 or a%5==0 or a%7==0:
        print(a,end=" ")'''

#9 print the first N multiples of either 3, 5 or 7.
'''
a=int(input("Enter the number :"))
for a in range(1,a+1):
    if a%3==0 or a%5==0 or a%7==0:
        print(a,end=" ")'''

#10 the sum of all digits in a positive integer
'''
num = input("Enter a positive integer: ")
total = 0
for digit in num:
    total += int(digit)
print("Sum of all digits:", total)'''

# 11 Count the number of digits in a positive integer
'''
a=int(input("Enter a number"))
count=0
while a>0:
    count+=1
    a//=10
print("Number of count :",count)'''

# 12 program to find factors of a given number
'''
a=int(input("Enter a number : "))
for i in range(1,a+1,1):
    if a%i==0:
        print(i)'''

# 13 program to count factors of a given number
'''
a=int(input("Enter a number : "))
count=0
for i in range(1,a+1,1):
    if a%i==0:
       count+=1
print("Number of factors",count)'''

# 14 program to find whether the given number is a prime number or not
'''
a=int(input("Enter a number : "))
count=0
for i in range(1,a+1,1):
    if a%i==0:
       count+=1
if count==2:
    print("Yes given number is prime number")
else:
    print("No given number is not a prime number")'''

# 15 Print all prime numbers from 2 up to and including 'n'
'''
n=int(input("Enter a number : "))
for i in range(2,n+1,1):
    count=0
    for j in range(1,i+1,1):
        if i%j==0:
           count+=1
    if count==2:
        print(i)'''
# 16 program to find the greatest common factor of given 2 integers
'''
a=int(input("Enter a number A: "))
b=int(input("Enter a number B : "))
gcf=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcf=i
print("Greatest common factor",gcf)'''

# 17 the common factors of two positive integers n and m. 
'''n=int(input("Enter a number N: "))
m=int(input("Enter a number M: "))
for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
        print(i)'''

# 18 program to get the Fibonacci series between 0 to 50
'''n=int(input("Enter a number N: "))
a=0
b=1
for i in range(n):
     print(a,end="")
     c=a+b
     a=b
     b=c'''
# 19 find the factorial of a given number
'''
a=int(input("Enter a number A: "))
fact=1
for i in range(1,a+1,1):
     fact=fact*i
print("factorial of a given number :",fact)'''
#20 set of integers, and then prints the sum of the even and odd integers.
'''
a=int(input("Enter the of elements: "))
odd=0
even=0
for i in range(a):
     a=int(input("Enter the integer :"))
     if a%2==0:
          even+=a
     else:
          odd+=a
print("sum of the even number :",even)
print("sum of the odd number :",odd)'''
# 21 Palidrome
'''
s=input("enter the string or number:")
rev=s[::-1]
if s==rev:
     print("Palidrome")
else:
     print(" Not Palidrome")'''

# 22 Armstrong number
'''
n=int(input("Enter a number n: "))
n1=n
n2=n
count=0
while n>0:
     count+=1
     n//=10
print(count)
s=0
while n1>0:
     r=n1%10
     s=s+(r**count)
     n1//=10
print(n)
print(n1)
print(n2)
print(s)
if s==n2:
     print("Armstrong number")
else:
     print(" Not Armstrong number")'''

#23 Patterns
'''
for j in range(1,4,1):
     for i in range(1,5,1):
          print("*",end=" ")
     print()
for i in range(1,n+1):
     for j in range(1,i+1):
          print("*",end=" ")
     print()'''
'''n=int(input("Enter the number :"))
for k in range(n):
     for i in range(1,n+1):
        print(" "*(n-1),end=" ")
        for j in range(0,i+1):
         print("*",end=" ")
     print()'''
#reverse without using function 
'''
s=input("enter the string or number:")
rev=""
i=len(s)-1
while i>=0:
     rev=rev+s[i]
     i=i-1
print(rev)'''
# factorical
'''
n=int(input("Enter a number A: "))
fact=1
for i in range (1,n+1,1):
     fact=fact*i
print(fact)'''

#sum of digit and count digit
'''
n=int(input("Enter a number n: "))
sum_digit=0
count=0
while n>0:
     digit=n%10
     sum_digit+=digit
     count+=1
     n//=10
print(sum_digit)
print(count)'''

#prime number
'''
n=int(input("Enter a number n: "))
count=0
for i in range(1,n+1,1):
     if n%i==0:
          count=count+1
if count==2:
     print("prime number")
else:
     print(" not prime number")'''

# username=alphabets+space
# password=only 8 digits,uppercase-1,lowercase-1,1-number,1-symbol
'''
username=input("Enter the username: ")
password=input("Enter the password : ")
for i in username:
     if(i.isalpha() or i.isspace()):
          print("valid username")
     else:
          print("Invalid username")
     break
uppercase=0
lowercase=0
number=0
symbol=0
for i in password:
     if len(password)==8:
          if i.isupper():
               uppercase+=1
          elif i.islower():
               lowercase+=1
          elif i.isdigit():
               number+=1
          else:
               symbol+=1
     else:
          print(" not a password has exacterly 8 digit")
if(len(password)==8 and uppercase>=1 and lowercase>=1 and number>=1 and symbol>=1):
     print("valid password")
else:
     print("Invalid password")'''

#revers the string or number
'''s=input("Enter the number or string : ")
temp=""
for i in range((len(s)-1),-1,-1):
     temp=temp+s[i]
print(temp)
if s==temp:
     print("palindrome")
else:
     print("not palindrome")'''
'''count=0
for i in s:
     count+=1
print(count)
t=""
for i in range(count-1,-1,-1):
     t=t+s[i]
print(t)
if s==t:
     print("palindrome")
else:
     print("not palindrome")'''

#reverse the number
'''
s=int(input("Enter the number : "))
rev=0
while s>0:
     digit=s%10
     rev=rev*10+digit
     s//=10
print("Reverse the number : ",rev)'''




   
          








     















    



    





