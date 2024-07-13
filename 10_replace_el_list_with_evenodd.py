# l[11,2,44,66,77] ---> o/p ['odd','even','even','even','odd']
#modification of list

l = [11,2,44,66,77]
for ip in range(len(l)):
    if l[ip]%2==0:
        l[ip]='even'
    else:
        l[ip]='odd'
print(l)

#creating newlist without modifing existion list
l=[11,2,44,66,77]
l1 = []
for i in l:
    if i%2==0:
        l1.append('even')
    else:
        l1.append('odd')
print(l1)

