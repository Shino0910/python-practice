
#1.number

from ast import operator
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME


number = -8
print(str(number))  #8  string
print(abs(number))  #8   intenger

#2......................................

print(pow(2,5)) #32
print(max(1,2,3,4,5,7,100)) #100
print(round(5.7)) #6

#......................................

print("....................................")

#3. simple caculator
number1 =input("Please enter your number:")
number2 =input("Please enter your number:")
print( int(number1) + int(number2))


print("....................................")

# 4.list

scores=[1,2,3,4,5,6,7]
print(scores[ :4])
print(scores[ 0:3])

print("....................................")

#5.function

def hello(name,age):
    print ( "Hi I am " + name + " I am " + str(age) + " years old" )

hello("shino" , 28 )

#..........................................

#5.function
def add(num1, num2):
    print(num1 + num2)
    return 10


value= add(3,4) 
print(value)   


#..........................................
print("....................................")

def add(num1, num2):
    print(num1 + num2)
    


value= add(3,4) 
print(value)   

#..........................................
print("....................................")


#6. function and if statement :compare numbers

def maxNum(x,y,z):
    if x>y and y>z:
        return x
    elif y>x and y >z:
        return y
    else:
        return z

print(maxNum(2,3,4))

#..........................................
print("....................................")

#7. advanced caculator

numx=float(input("Please enter number:"))
numy=float(input("please enter number:"))
operator = input("Please enter operator:")

if operator== "+":
    print(numx+ numy)
elif operator== "-":
    print (numx-numy)
elif operator == "*":
    print (numx* numy)
elif operator == "/":
    print (numx/numy)
else:
    print("error")


#..........................................
print("....................................")

#8 .guess number game(no limit)


answer=1098
guess =None

while answer!=guess:
    guess= int(input("please enter the number:"))
    if guess > answer:
        print("too more")
    elif guess < answer:
        print("too less")
    else:
        print("you win")

#..........................................
print("....................................")

# function of for 
def power(x,y):
    result = x
    for index in range(y-1):
        result= result * x
    return result


print(power(2,5))

#檔案寫入