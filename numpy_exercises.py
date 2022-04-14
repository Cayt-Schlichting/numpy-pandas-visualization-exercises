import numpy as np

#array to use:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
#test data type
a_float = a.astype('float')
#1) number of negative numbers
# a>0 creates boolean array. 
# Plugging boolean array into another array creates smaller array where just true values exist
print(f'Number of negative numbers: {len(a[a < 0])}')

#2) number of positive numbers
print(f'Number of postive numbers: {len(a[a > 0])}')

#3) number of even, positive numbers
#a little verbose (even with simple logic, there should be a better way)
print(f'Number of even, positive numbers: {len(a[a>0][a[a>0]%2 ==0])}')
#where returns a tuple, position 0 holds an array of the indexes where logic is true
print(f'Number of even, positive numbers: {len(np.where((a>0) & (a%2==0))[0])}')
#use logical_and >> takes in two boolean areas of matching length
print(f'Number of even, positive numbers: {len(a[np.logical_and(a>0,a%2==0)])}')
#Finally!  You just need to make sure and put () around each piece of logic
print(f'Number of even, positive numbers: {len(a[(a>0) & (a%2==0)])}')

#4) add 3, how many positive?
print(f'After adding 3, the number of positive numbers is: {len(a[(a+3)>0])}')

#5) if you square each number, what would the new mean and stddev be?
#a*a



