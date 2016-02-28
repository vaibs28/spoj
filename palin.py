def pal(n):
 n=str(n)
 rev=n[::-1]
 rev=int(rev)
 return rev

ans=[]
i=0
t=int(input())
for i in range (0,t):
 n=int(input())
 while(1):
  n=n+1;
  
  if(n==pal(n)):
   ans.insert(i,n)
   i=i+1;
   break
for i in range(0,t):
 print ans[i]
