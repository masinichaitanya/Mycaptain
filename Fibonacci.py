length=int(input())
x,y=0,1
sum=0
count=1
print("Fibonacci series:",end='')
while(count<=length):
  print(sum,end=',')
  count+=1
  x=y
  y=sum
  sum=x+y
