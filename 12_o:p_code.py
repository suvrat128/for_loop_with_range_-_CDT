# what is the output of given program


l=[11,22,33,44,55]
for i in l:
    l.remove(i)
print(i)
print(l)


# o/p
'''
55
[22,44]
'''
'''
# process
iteration 1:
    it will fetch 11 so i is 11
        now remove i 11
        updeted list =[22,33,44,55]
iteration2:
    it will fetch 33 because i is at 1 indexposition so i is 33
        now remove i 33
        updeted list = [22,44,55]
iteration3:
    it will fetch 55 because i is at 2 indexposition so i is 55
        now remove i 55
        updeted list = [22,44]
there is no indexposition 3 so for loop will stop
2. at last it will print 55
and list [22,44]
'''