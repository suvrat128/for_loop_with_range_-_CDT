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
# string = h2a4py
1. take input from user
2. asumming there is no even digit present at odd indexposition so summ = 0
3. using loop
    iteration 1:
        it will fetch 1 index position so ip = 1
        check s[1] = '2' is in '24680' true:
            summ = 0+ 2 
    iteration 2:
        it will fetch 3 indexposition so ip = 3
        check s[3] = '4' is in '24680' true:
            summ = 2+4
    iteration 3:
        it will fetch 5 indexposition so ip = 5
        check s[5] = 'y' is in '24680' false: so summ still 6
4. at last after completion of loop print the value of summ =6

'''