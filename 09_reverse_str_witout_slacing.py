# reverse the given string without slicing

s = input()
reverse = ''

for i in s:
    reverse = i+reverse
print(reverse)

'''
process:
1. take input from user
3 string = 'happy'
2. take a variabe with empty string where we store the reversed string
3. using loop:
    iteration 1:
        it will fetch 'h' so i  is 'h'
        we will add in start of the 'h' to variable reverse 
        reverse='h'
    iteration 2:
        it will fetch 'a' so i  is 'a'
        we will add in start of the 'a' to variable reverse 
        reverse='ah'
    iteration 3:
        it will fetch 'p' so i  is 'p'
        we will add in start of the 'p' to variable reverse 
        reverse='pah'
    iteration 4:
        it will fetch 'p' so i  is 'p'
        we will add in start of the 'p' to variable reverse 
        reverse='ppah'
    iteration 5:
        it will fetch 'y' so i  is 'y'
        we will add in start of the 'y' to variable reverse 
        reverse='yppah'
5. at last after complatioon of lopp we print reverse = 'yppah'

'''

# another way to reverse using indexing

s= input()
reverse = ''
for ip in range(-1,-(len(s)+1),-1):
    reverse+=s[ip]
print(reverse)

'''
process:
1. take input from user
3 string = 'happy'
2. take a variabe with empty string where we store the reversed string
3. using loop:
'''