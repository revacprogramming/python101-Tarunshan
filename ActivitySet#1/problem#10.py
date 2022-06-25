name=input("Enter file:")
handle=open(name)
d=dict()
for line in handle:
    if line.startswith("From:"):
        l=line.split()
        if l[1] not in d:
            d[l[1]]=1
        else:
            d[l[1]]+=1
l=0
k=None
for n,m in d.items():
    if m>l:
        l=m
        k=n
print(k,l)
