# element get swap with ajustent element --->l[11,22,33,44,55,66] to l[22,11,44,33,66,55]

l = [11,22,33,44,55,66]

for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)

