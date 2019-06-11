a=int(input())
b=int(input())
if (a,b<=10000):
    for i in range(a+1,b+1):
        if(i%2!=0):
            print(i)
