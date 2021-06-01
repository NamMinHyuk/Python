'''
*
**
***
****
*****
'''
from ntpath import sep

i = 1
for i in range(1,6):
    print('*' * i)

print('----------')
'''
*****
****
***
**
*
'''
for i in range(5,0, -1):
    print('*' * i)
print('----------')
'''
    *
   **
  ***
 ****
*****
'''
j = 1
for i in range(5,0,-1):
    print(' ' * int(i-1) + '*'*j)
    j += 1
print('----------')

'''
*****
 ****
  ***
   **
    *    
'''
j = 5
for i in range(1, 6):
    print(' '* int(i-1) + '*' * j)
    j -= 1
print('----------')
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5 ,0 ,-1):
    print(" " *int(i-1) ,end='')
    print("*" *(5 - i +1) ,end='')
    print("*" *(5 -i) ,end='')
    print(" " *int(i-1))

