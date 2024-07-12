#wpt find the sum of even digits present in odd index position

s = input()
summ = 0
for ip in range(len(s)):
    if s[ip].isdigit()  and ip%2!=0 and int(s[ip])%2== 0:
        summ+=int(s[ip])
print(summ)


#the optimize code:
s = input()
summ = 0
for ip in range(1,len(s),2):
    if s[ip] in '24680':
        summ+=int(s[ip])
print(summ)
'''

'''