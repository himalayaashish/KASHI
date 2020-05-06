
### prime mmunber

number = int(input("Enter number ::"))
isDiv = False
i = 2
while i < number:
    if number % i == 0:
        isDiv = True
        print("{} is divisible by {}".format(number,i))
    i+=1
if isDiv:
    print("{} is Not a Prime number".format(number))
else:
    print("{} is a Prme number".format(number))


### Fuction 

def fun1(a):
    print("I in Fun1 with {}".format(a))

fun1(100)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


print(add(10,20))
print(sub(10,5))

