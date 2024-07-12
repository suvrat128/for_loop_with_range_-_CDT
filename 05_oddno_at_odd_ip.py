#wpt print odd numbers present in odd index position of a given string

s = input()

for ip in range(len(s)):
    if s[ip].isdigit()  and ip%2!=0 and int(s[ip])%2!= 0:
        print(s[ip])
'''
#process
1. take string as input form user
s = 'h1p3y'
2. using loop:
    iteration1:
        it will fetch 0 so ip is 0:
        checK s[0] 'h' is digit: false so nothing will print
    iteration2:
        it will fetch 1 so ip is 1:
        check s[1] '1' is digit: true:
            check 1%2 is not eqal to 0 : true:
                check int(s[1])%2 is not equal to 0: true
                    print the value of indexposition 1 = '1'
    iteration3:
        it will fetch 2 so ip is 2:
        checK s[2] 'p' is digit: false so nothing will print
    iteration4:
        it will fetch 3 so ip is 3:
        check s[3] '3' is digit: true:
            check 3%2 is not eqal to 0 : true:
                check int(s[3])%2 is not equal to 0: true
                    print the value of indexposition 3 = '3'
    iteration5:
        it will fetch 4 so ip is 4:
        checK s[4] 'y' is digit: false so nothing will print

'''