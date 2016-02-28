t=int(input())
ans=[]

for i in range(0,t):
	n=int(input())
	count=0
	while(n>=5):
		count+=n//5
		n =n//5
	ans.insert(i,count)
	 
for i in range(0,t):
	print ans[i]


