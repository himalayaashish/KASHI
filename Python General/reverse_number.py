def reverse_number(x):
    result, x_remainder = 0, abs(x)
    while x_remainder:
        result = result * 10 + x_remainder % 10
        x_remainder //=10
    return -result if x<0 else result 


x = int(input("Enter the Number"))
answer = reverse_number(x)
print("The reverse of {} ==> {}".format(x,answer))
