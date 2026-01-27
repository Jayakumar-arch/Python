# 1 find the smallest number among two given integers.
"""a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
if a>b:
    print("A is biggest number ")
else:
    print("B is smallest  number")""" 

# 2 find the largest number among two given integers

"""a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
if a>b:
    print("A is largest number " )
else:
    print("B is smallest  number")"""

# 3 find the absolute value of a given integer.
"""A=int(input("Enter the number :"))
if A<0:
    a=-A
    print(a)

else:
     print(A)"""

# 4 given number is even number or odd number

'''a=int(input("Enter the number :"))
if a%2==0:
    print("Given number is even number")
else:
    print("Given number is odd number")'''

# 5.given number is a multiple of 5 or not.
'''
a=int(input("Enter the number :"))
if a%5==0:
    print("Given number is multiple by 5")
else:
    print("Given number is not  multiple by 5")'''

# 6.given number is a multiple of 10 or not.
'''
a=int(input("Enter the number :"))
if a%10==0:
     print("Given number is multiple by 10")
else:
     print("Given number is not  multiple by 10")'''

# 7.given number is a two-digit number or not.
'''
a=int(input("Enter the number :"))
if  9<=a<=99:
    
    print("The number is a two-digit number  ")
else:
    print("The number is not  a two-digit number  ")'''

# 8.given number is a three-digit number or not.
'''
a=int(input("Enter the number"))
if 99<=a<=999:
      print("The number is a three-digit number  ")
else:
    print("The number is not a three-digit number  ")'''

# 9. given number ends with zero or not
'''
a=int(input("Enter the number :"))
if a%10==0:
    print("number ends with zero ")
else:
    print("number not  ends with zero ")'''

# 10. accept a number and check if its square is above 50 or below 50
'''
a=int(input("Enter the number :"))
a_sq=a**2
print("square the number :",a_sq)
if a>=50:
     print("above 50 ")
else:
    print("below 50")'''

# 11.to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not
'''
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
difference =a-b
if difference==0:
     print("The difference is Zero")

else:
     print("The difference is not Zero")'''

#12.to read the Computer Science marks of a student and print if the student has passed or failed. The student has passed if marks is 50 or above otherwise failed).
'''
computer_mark=int(input("Enter the mark :"))
if computer_mark>=50:
    print("The student has pass " )
else:
    print("The student has fail")'''

# 13.a program to accept a number and check if the number is divisible by 10.
'''
a=int(input("Enter the number :"))
if a%10==0:
    print("The given number is divisible by 10")
else:
    print("The given number is not divisible by 10")'''

#14. program to take a two-digit number and print the biggest digit.
'''
a=int(input("Enter the two-digit number :"))
print(a)
b=a%10
print(b)
c=a//10
print(c)
if b>c:
    print("B is the Biggest number",b)
else:
     print("C is the Biggest number",c)'''

#15. a program to accept the choice from the user. If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult”.
'''
a=int(input("Enter the choice 1 or any number :"))
if a==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")'''

#16.Write a program to accept a value from the user. If the value entered is 1 then print “You can go out and play” otherwise “You can go out and play”
'''
a=int(input("Enter the value 1 or any number"))
if a==1:
    print("You can go out and play")
else:
    print("You cannot go out and play")'''

#17.Write a program to accept the length and breadth of a shape and print if they are the same. If they are the same, print it’s a square otherwise its rectangle
'''
length=int(input("Enter the length :"))
breadth=int(input("Enter the breadth :"))
if (length==breadth):
    print("Square")
else:
    print("rectangle")'''

#18
'''
a=int(input("enter the number :"))
if (a>65 and a<=90):
    print("The ASCII value of an uppercase alphabet",a)
else:
    print("The not ASCII value of an uppercase alphabet",a)'''

#19
'''
a=int(input("enter the number :"))
if (a>97 and a<=122):
    print("The ASCII value of an lowercase alphabet  :",a)
else:
    print("The not ASCII value of an lowercase alphabet  :",a)'''

#20
'''
a=int(input("enter the number :"))
if (a>48 and a<=57):
    print("The ASCII value of an numeric :",a)
else:
    print("The not ASCII value of an numeric    :",a) '''

#21
'''
a=int(input("enter the number :"))
if(a%3==0 and a%5==0):
    print("The number is multiple of both 3 and 5")
else:
    print("The number is  not multiple of both 3 and 5")'''

#22
'''
a=int(input("enter the number :"))
if(a>99 and a<=999 and a%10==0):
    print("The given number is three digit number and also multiple of 10 :",a)
else:
     print("The given number is three digit number and also not multiple of 10 :",a)'''

#23
'''
a=int(input("enter the number :"))
if(a>=99 and a<=999 and a%2==0 and  a%5==0 and a%10==0):
    print("The given number is three digit number and also multiple of 2,5,10 :",a)
else:
     print("The given number is not three digit number and also not multiple of 2,5,10 :",a)'''

#24
'''
a=int(input("enter the number a :"))
b=int(input("enter the number  b:"))
if(a%2==0 and b%2==0):
    result=a*b
    print("Both number are even")
    print("Product :" ,result)
else:
    result=a+b
    print("Both number are not  even")
    print("Sum:",result)'''

#25
'''
a=int(input("enter the number a :"))
if(a%10==7 or a%7==0):
    print("Buzz number :",a)
else:
    print("not buzz number :",a)'''

#elif 1.
'''
a=int(input("enter the number a :"))
b=int(input("enter the number b :"))
c=int(input("enter the number c:"))
if(a>b and a>c):
    print("A is largest number :",a)
elif(b>a and b>c):
     print("B is largest number :",b)
else:
     print("C is largest number :",c)'''
#elif 2.
'''
a=int(input("enter the number a :"))
b=int(input("enter the number b :"))
c=int(input("enter the number c:"))
if(a<b and a<c):
    print("A is Smallest number :",a)
elif(b<a and b<c):
     print("B is Smallest number :",b)
else:
     print("C is Smallest number :",c)'''
#elif 3.
'''
a=int(input("enter the number a :"))
if(a>0):
    print("Positive :",a)
elif(a<0):
    print("Negative :",a)
else:
    print("Zero :",a)'''

#elif 4.
'''
a=int(input("enter the number of day:"))
if(a<=5):
    fine=a*0.40
elif(a<=10):
    fine=a*0.65
else:
    fine=a*0.80
print("Total fine to be paid :",fine)'''

#elif 5.
'''
a=int(input("enter the number a :"))
b=int(input("enter the number b :"))
op=input("Enter operation (+,-,*,/) :" )
if op=="+":
    result=a+b
    print("Result",result)
elif op=="-":
     result=a-b
     print("Result",result)
elif op=="*":
     result=a*b
     print("Result",result)
elif op=="/":
     result=a/b
     print("Result",result)
else:
    print("Invalid operation")'''
#elif 6
'''
a=int(input("Enter the number a :"))
if a%5==0:
    print("The number is a multiple of 5")
elif a%3==0:
    print("The number is a multiple of 3")
elif a%7==0:
    print("The number is a multiple of 7")
else:
    print("The number is not multiple of 3,5and 7")'''

#elif 7
'''
weight = int(input("Enter the weight of the parcel: "))
booking = input("Enter the type of booking ('O' for ordinary and 'E' for express): ")

charge = 0

if booking == "O":
    if weight <= 100:
        charge = 80
    elif weight <= 500:
        charge = 150
    elif weight <= 1000:
        charge = 210
    else:
        charge = 250

elif booking == "E":
    if weight <= 100:
        charge = 100
    elif weight <= 500:
        charge = 200
    elif weight <= 1000:
        charge = 250
    else:
        charge = 300

else:
    print("Invalid booking type")

if charge != 0:
    print("Parcel charge:", charge)'''

#elif 8
'''
price=int(input("Enter the price of laptop :"))
discount=0
if price<=50000:
    discount=0
elif price<=100000:
    discount=10
elif price<=150000:
    discount=15
else:
    discount=20
discountamount=(price/100)*discount
totalprice= price-discountamount
print("Discount   :",discount,"%")
print("Totalprice :",totalprice)'''

'''for j in range(1,6,1):
    for i in range(1,5,1):
        print("*",end="")
    print()'''

    

        
    


 
     
 
    

 
