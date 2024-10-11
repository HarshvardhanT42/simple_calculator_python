a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))

def switch(n):
    if n == 1:
        x = a + b
        print("the addition of 1st and 2nd no is ", x )
    elif n == 2:
        x = a - b
        print("the subtraction of 2nd no from 1st no is ",x )
    elif n == 3:
        x = a * b
        print("the multiplication of 1st and 2nd no is ",x )
    elif n == 4:
        x = a % b
        print("the division of 1st and 2nd no is ",x)
    else :
        print("wrong option is selceted, try again!!")
    
print("1. addition")
print("2.subtraction")
print("3. multiplication")
print("4. division")

n = int(input("please select the option"))

print(switch(n))