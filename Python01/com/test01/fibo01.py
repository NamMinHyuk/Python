n = input('input n : ')

# fibonacci 수열 : 0 1 1 2 3 5 8 13 21 34 55 89 ...
'''
def fib(n):
    fibList=[0, 1]
    if n==0 or n==1:
        return 0
    if n==2:
        return fibList
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList

print(fib(int(n)))
'''
a, b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b
    i += 1
print()
