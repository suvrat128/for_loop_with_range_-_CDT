# wpt print the index position of vovels

s = input()

for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        print(ip)

'''
#process
1. take input as string from user
#string = 'happy'
2. using for loop:'
    iteration1:
        it will fetch 0 so ip is 0
        check s[0] 'h' in 'aeiouAEIOU':false nothing will print in this iteration
    iteration2:
        it will fetch 1 so ip is 1
        check s[1] 'a' in 'aeiouAEIOU' : true
            print the indexposition = 1
    iteration3:
        it will fetch 2 so ip is 2
        check s[2] 'p' in 'aeiouAEIOU':false nothing will print in this iteration
     iteration4:
        it will fetch 3 so ip is 3
        check s[3] 'p' in 'aeiouAEIOU':false nothing will print in this iteration
     iteration5:
        it will fetch 4 so ip is 4
        check s[4] 'y' in 'aeiouAEIOU':false nothing will print in this iteration

'''