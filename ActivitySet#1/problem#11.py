name=input("Enter file:")
handle=open(name)
hours={}
for line in handle:
    if "From:" in line:
        continue
    elif "From" in line:
        time=line.split()
        time=str(time[5]).split(":")
        if time[0] not in hours:
            hours[time[0]]=1
        else:
            hours[time[0]]=hours.get(time[0],)+1

for i,j in sorted(hours.items()):
    print(i,j)
