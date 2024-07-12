# wpt print the element which are in even index position of given string


s = input()

for ip in range(len(s)):
    if ip%2==0:
        print(s[ip])
'''
#process
1. take input from user
# string = 'happy'
2. using for loop:
    iteration1:
        it will fetch 0 so ip is 0
        check 0%2==0:true
            print the value present at 0 index position h
    iteration 2:
        it will fetch 1 so ip is 1
        check 1%2==0: false nothing will print in this iteration
    iteration3:
        it will fetch 2 so ip is 2
        check 2%2==0:true
            print the value present at 2 index position p
    iteration 4:
        it will fetch 3 so ip is 3
        check 3%2==0: false nothing will print in this iteration
    iteration5:
        it will fetch 4 so ip is 4
        check 4%2==0:true
            print the value present at 4 index position y
        
'''