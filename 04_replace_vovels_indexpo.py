#wpt replace all the vovels with thire index position

s = input()
ns = ''
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        ns+=str(ip)
    else:
        ns+=s[ip]
      
print(ns)
'''
#process
1. take input as string from user
#string = 'happy'
3. take new as emptystring 
2. using for loop:'
    iteration1:
        it will fetch 0 so ip is 0
        check s[0] 'h' in 'aeiouAEIOU':false
            add s[0] to new so new ='h'
    iteration2:
        it will fetch 1 so ip is 1
        check s[1] 'a' in 'aeiouAEIOU' : true
            add str(1) to new so new ='h1'
    iteration3:
        it will fetch 2 so ip is 2
        check s[2] 'p' in 'aeiouAEIOU':false
            add s[2] to new so new ='h1p'
     iteration4:
        it will fetch 3 so ip is 3
        check s[3] 'p' in 'aeiouAEIOU':false
            add s[3] to new so new ='h1pp'
     iteration5:
        it will fetch 4 so ip is 4
        check s[4] 'y' in 'aeiouAEIOU':false
            add s[4] to new so new ='h1ppy'

        
'''
