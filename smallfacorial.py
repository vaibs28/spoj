def fact(n):
    if(n==0):
     return 1;
    else:
        return (n*fact(n-1));
  
t=int(input());
a=[];
res=[];
for i in range(0,t):
    a.insert(i,input());
    n=int(a[i]);
    x=fact(n);
    res.insert(i,x);
    
for j in range(0,t):
    print(res[j]);


