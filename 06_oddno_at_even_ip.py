# wpt print odd digits present in even index position

s = input()

for ip in range(len(s)):
    if s[ip].isdigit()  and ip%2==0 and int(s[ip])%2!= 0:
        print(s[ip]) 

'''
#process
1. take string as input form user
s = '1h3apy'
2. using loop:
    iteration1:
        it will fetch 0 so ip is 0:
        check s[0] '1' is digit: true:
            check 0%2 is eqal to 0 : true:
                check int(s[0])%2 is not equal to 0: true
                    print the value of indexposition 0 = '1'
    iteration2:
        it will fetch 1 so ip is 1:
        checK s[1] 'h' is digit: false so nothing will print
    iteration3:
        it will fetch 2 so ip is 2:
        check s[2] '3' is digit: true:
            check 3%2 is eqal to 0 : true:
                check int(s[3])%2 is not equal to 0: true
                    print the value of indexposition 2 = '3'
    iteration4:
        it will fetch 3 so ip is 3:
        checK s[3] 'a' is digit: false so nothing will print
    iteration5:
        it will fetch 4 so ip is 4:
        checK s[4] 'p' is digit: false so nothing will print

'''
