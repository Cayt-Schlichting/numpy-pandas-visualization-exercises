import numpy as np
import pandas as pd
# import matplotlib

### EXERCISES - PART 1 ####
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
#1
print(f'The number of elements in fruits is: {fruits.size}')
#2
print(f'The fruits index is: {fruits.index}')
#3
print(f'The values in fruits are: {fruits.values}')
#4 - #this only grabs the type of the first value
print(f'The values in fruits are type: {fruits.dtype}')

#5
print(f'The first 5 values from fruits are: \n{fruits.head()}')
print(f'The last 3 values from fruits are: \n{fruits.tail(3)}')
print(f'Two random values from fruits are: \n{fruits.sample(2)}')
#6 describe
print(f'Describing fruits: \n{fruits.describe()}')
#7
print(f'Here are the unique values in fruits: \n {fruits.unique()}')
#8
print(f'Count of unique values in fruits:\n{fruits.value_counts()}')
#9 most frequent
print(f'The most common value in fruits is: {fruits.value_counts().nlargest(n=1,keep="all")}')
#or:
fruits.mode() #doesn't provide count
#10
print(f'The least common value in fruits is: \n{fruits.value_counts().nsmallest(n=1,keep="all")}')

### EXERCISES - PART 2 ####
#1 - capitalize
fruits.str.upper()
#2 Count the letter 'a'
  #make sure lowercase, then count 'a' in each element, 
  #this creates new series with count of each >>> then take sume of that series
sum(fruits.str.lower().str.count('a'))
#3
vowels = list('aeiou')
count = 0
count = pd.Series(np.zeros(fruits.shape()))
for i in vowels:
    count += sum(fruits.str.lower().str.count(i))
print(f'There are {count} vowels in this series')
#3 - alt
#concate whole series into one string, then pull out vowels and determine length
len([x for x in fruits.str.cat() if x in vowels])
#3 - alt
 #applying a vowel function
def count_vowels(val):
    cnt = 0
    vowels = list('aeiou')
    for i in val.lower():
        if i in vowels: cnt += 1
    return cnt
  #if we want number of vowels per element
fruits.apply(count_vowels)
  #if we want number of vowels in the whole series
sum(fruits.apply(count_vowels))

#4 longest string
#ew, but works
fruits[fruits.str.len() == fruits.str.len().max()]
#YAY - I knew there'd be an index equivalent!
fruits[fruits.str.len().idxmax()]
#5
fruits[fruits.str.len() >= 5]
#6
fruits[fruits.apply(lambda n: True if n.count('o') >= 2 else False)]
#7 
fruits[fruits.str.contains('berry')].values
#8 
fruits[fruits.str.contains('apple')].values
#9
fruits[fruits.apply(count_vowels).idxmax()]

### EXERCISES - PART 3 ####
alp = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
#1 - most freq letter
alp.value_counts().nlargest(n=1,keep='all') #y 13
#2 - least freq letter
alp.value_counts().nsmallest(n=1,keep='all') #l 4
#3 how many vowels
  #This will get a 0 or 1 for each, then just take the sum of the whole series
sum(alp.apply(count_vowels)) #34
#4 how many consonants
  #this works because there is one char per element
alp.size-sum(alp.apply(count_vowels)) #166
#5 uppercase them
alp_up = alp.str.upper()
#6 bar plot of the frequencies of 6 most common letters
## FINISH ME in Jupyter

#PART 3, SECTION 2
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
## FINISH ME in Jupyter