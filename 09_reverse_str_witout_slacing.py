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
    iteration 1:
        it will fetch -1 indexposition so ip is -1
        it will add value of indexposition -1 = 'y' to reverse variable
        reverse = 'y'
    iteration 2:
        it will fetch -2 indexposition so ip is -2
        it will add value of indexposition -2 = 'p' to reverse variable
        reverse = 'yp'
    iteration 3:
        it will fetch -3 indexposition so ip is -3
        it will add value of indexposition -3 = 'p' to reverse variable
        reverse = 'ypp'
    iteration 4:
        it will fetch -4 indexposition so ip is -4
        it will add value of indexposition -4 = 'a' to reverse variable
        reverse = 'yppa'
     iteration 1:
        it will fetch -5 indexposition so ip is -5
        it will add value of indexposition -5 = 'h' to reverse variable
        reverse = 'yppah'
5. at last after complatioon of lopp we print reverse = 'yppah'
        
'''