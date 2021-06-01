subject = ['java', 'javascript', 'python']

for s in subject:
    print(s, end=' ') # 가로로 하고싶을때 end 
else:
    print('재밋다.')
    
for i in range(1, 100):
    print(i, end=' ')
    
print('--------')

print('구구단')

for i in range(2,10):
    print('<<' + str(i) + '단>>')
    for j in range(1,10):
        # print(str(i) +' * ' + str(j) + ' = ' + str(i*j))
        print(i, '*' , j, '=', i*j, sep=' ')
    print()    
# range 함수 사용해서 10 ~ 1까지 거꾸로 출력.
for i in range(10, 0, -1):
    print(i, end=' ')
    