'''
1. for문을 사용하여 구구단 전체를 출력하는 gugu() 라는 함수를 만들자.
2. while문을 사용하여 함수 호출시 입력된 단만 출력하는 gugudon(x)를 만들자.
3. main함수에서 gugu()와 gugudon(x) 함수를 호출하되, gugudon에 입력해주는 숫자는 input을 사용하자.
'''

def gugu():
    print('구구단 전체출력')
    for i in range(2,10):
        print('<<{}단>>'.format(i))
        for j in range(1, 10):
            print('%d * %d = %d' % (i, j, i*j))
            
    print()

def gugudon(x):
    print('<<{}단>>'.format(x))
    i = 1
    while i < 10:
        print('%d * %d = %d' % (x, i, x*i))
        i += 1
    
if __name__ == '__main__':
    gugu()
    x = input('원하는 단을 입력해주세요 : ')
    gugudon(int(x))