#number

number = -8
print(str(number))  #8  string
print(abs(number))  #8   intenger

#......................................

print(pow(2,5)) #32
print(max(1,2,3,4,5,7,100)) #100
print(round(5.7)) #6

#......................................

print("....................................")

#simple caculator
number1 =input("Please enter your number:")
number2 =input("Please enter your number:")
print( int(number1) + int(number2))


print("....................................")

#list

scores=[1,2,3,4,5,6,7]
print(scores[ :4])
print(scores[ 0:3])

print("....................................")

#function

def hello(name,age):
    print ( "Hi I am " + name + " I am " + str(age) + " years old" )

hello("shino" , 28 )
