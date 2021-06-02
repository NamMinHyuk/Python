def fibo01(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=' ')
        a, b = b, a + b
        i += 1
    print()
    

def fibo02(n):
    list = [0, 1]
    if n==0 or n==1:
        return 0
    if n==2:
        return list
    for i in range(2,n):
        list.append(list[i-1] + list[i-2] )
    return list
    '''
    res = list()
    a, b = 0, 1
    i = 0
    while i < n:
        res.append(a)
        a,b = b, a+b
        i+= 1
    return res
    '''

if __name__ == '__main__':
    n = int(input('n : '))
    # 입력된 숫자 만큼 반복해서 출력
    fibo01(n)
    
    # 입력된 숫자 만큼 반복해서 list에 저장하고, 
    # list를 리턴
    print(fibo02(n))
