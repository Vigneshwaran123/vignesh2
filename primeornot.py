a=int(input())
iscomposite=0
for b in range(2,a):
  if(a%b==0):
    iscomposite=1
if(iscomposite==1):
  print("no")
else:
  print("yes")
