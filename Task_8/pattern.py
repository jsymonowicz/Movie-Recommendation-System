'''
This program prints the following pattern:
*
**
***
****
*****
****
***
**
*
'''

for i in range(1, 10):
#for rows 1-5 number of '*' is proportional to row number:
    if i <= 5:
        print('*'*i)
#for rows 6-9 number of '*' is inversely proportional to row number:
    else:
        print('*'*(10-i))