# Use the file name mbox-short.txt as the file name
fname=input("Enter file name: ")
fh=open(fname)
s=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a=line.find("0")
    s=s+float(line[a:a+7])
    count+=1

avg=s/count
print("Average spam confidence:",avg)
    

