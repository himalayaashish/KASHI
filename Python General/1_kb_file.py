# 1 kb
a = 1
with open('test.txt','w') as f:
    for i in range(1001):
        f.write(str(a))
