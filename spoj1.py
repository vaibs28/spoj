o=[]
x=0
y=1
flag=0
while(y):
 n=int(input())
 if(n!=42 and flag==0):
  o.insert(x,n)
  x=x+1
 if(n==42):
 	flag=1
 	y=0
for i in range (0,x):
	print(o[i])


