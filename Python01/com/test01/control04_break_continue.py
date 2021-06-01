i = 1

while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else: # 반복문이 정산적으로 돌았을때 돈다. break로 빠졌기때문에 안돔
    print('i:', i) 
    
print('--------')

for i in range(1,10):
    if i&2==0:
        continue
    print(i)
else:
    print('i:', i)