a=int(input())
b=int(input())
if (a,b<=10000):
    for i in range(a,b+1):
        if(i%2!=0):
            print(i)
else:
    print("")
