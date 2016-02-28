#add reversed numbers
t=int(raw_input())
for i in range(0,t):
	m,n=raw_input().split()
	revm=m[::-1]
	revn=n[::-1]
	revm=int(revm)
	revn=int(revn)
	sum=revm+revn
	sum=str(sum)
	revsum=sum[::-1]
	revsum=int(revsum)
	print revsum
