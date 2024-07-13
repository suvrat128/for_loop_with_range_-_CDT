# reverse the given string without slicing

s = input()
reverse = ''

for i in s:
    reverse = i+reverse
print(reverse)

# another way to reverse using indexing

s= input()
reverse = ''
for ip in range(-1,-(len(s)+1),-1):
    reverse+=s[ip]
print(reverse)
