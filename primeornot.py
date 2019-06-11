a=int(input())
iscomposite=0
for i in range(2,a):
  if(a%i==0):
    iscomposite=1
    break
if(iscomposite==1):
  print("no")
else:
  print("yes")
