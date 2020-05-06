a = 10
print(id(a))
#94108855012987 some location in RAM

b = 10
print(id(b))
#94108855012987 same location in RAM as value of a and b are same


#Multiple Assignment
a,b = 10,20
print("The value for a is {} and the value for b is {}".format(a,b))

#Swap two numbers
a,b = 100,200
print("The value for a before swap is {} and the value for b before swap is {}".format(a,b))
a,b = b,a
print("The value for a after swap is {} and the value for b after swap is {}".format(a,b))

#String sclice
s = "I love coding in Python"
print(s[2:6]) # love
print(s[2:6] +" " + s[16:]) #love Python
print(s[2:6] +" " + s[16:23]) #love Python

# If my string is very long the we start from back with -ve sign
print(s[2:6] +" " + s[-6:]) #love Python

#Reverse string
print(s[::-1]) # nohtyP ni gnidoc evol I

#Reverse a sub string
print(s[:17] + " " + s[:-7:-1] ) #I love coding in  nohtyP


#List 
l1 = [10,20,30]
id1 = id(l1)
print(id1)
del l1
l2 = [10,20,30]
id2 = id(l2)
print(id2)
print(id1==id2) #True


l1 = [10,20,30]

l2=l1
print("The value of l1 is {} and its location is {}".format(l1,id(l1)))
print("The value of l2 is {} and its location is {}".format(l2,id(l2)))
# If we change value of l2 only. Then it will also change the value of l1.

l2[2] = 50
print("Changing value of 3rd element of l2 only ")

print("l1 was [10,20,30] but has been changed to {} because of change in reference of l2 {}".format(l1,id(l1)))
print("The value of l1 is {} and its location is {}".format(l1,id(l1)))







