def cal_power(x,y):
    result,power = 1.0,y
    if y < 0:
        power,x = -power,1.0/x
    while power:
        if power & 1:
            result *=x
        x,power = x*x,power >>1
    return result

x = int(input("Enter the base number :"))
y = int(input("Enter the power :"))
print(cal_power(x,y))

