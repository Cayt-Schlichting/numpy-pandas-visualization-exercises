from pydataset import data
import pandas as pd
import numpy as np

#1 - STUDENT GRADES DATASET
#create student dataframe
np.random.seed(385)
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

#1a)
df['passing_english'] = df.english >=70

#1b) - want True on top
df.sort_values(by='passing_english',ascending=False)

#1c) 
df.sort_values(by=['passing_english','name'],ascending=[True,True])

#1d)
df.sort_values(by=['passing_english','english'],ascending=[False,False])

#1e)
df['grade'] = round((df.english + df.math + df.reading)/3,2)
# could also take mean of columns
#This would work if we want mean of ALL numeric columns - BUT includes booleans
df.mean(axis=1,numeric_only=True) 
#or we could specify the columns we want to play with:
df[['english','math','reading']].mean(axis=1)


#2 - MPG DATASET
# data('mpg',show_doc=True)
mpg = data('mpg')
# # of rows/columns
print(f'There are {mpg.shape[0]} rows in this dataframe') 
print(f'There are {mpg.shape[1]} columns in this dataframe') #index not considered a column
# 
mpg.info() #useful
mpg.describe()
# rename city and highway - keep those changes
mpg.rename(columns = {'hwy':'highway','cty':'city'},inplace=True)
#
mpg[mpg.highway < mpg.city] #no, returns empty dataframe
#
mpg['mileage_difference'] = mpg.highway - mpg.city
# biggest difference
mpg.nlargest(n=1,columns='mileage_difference',keep='all')
#V2 - this would only return the highest differences, not the rest of the columns
mpg.mileage_difference.nlargest(n=1,keep='all')

# best highway mileage for compact car
mpg[mpg['class']=='compact'].nlargest(columns='highway',n=1,keep='all')[['manufacturer','model','year','displ','highway']]
#worst highway mileage for compact car
mpg[mpg['class']=='compact'].nsmallest(columns='highway',n=1,keep='all')[['manufacturer','model','year','displ','highway']]
#
mpg['avg_mpg'] = (mpg.highway + mpg.city)/2
# dodges that are cars.  NOTE: ~ is the NOT operator in pandas
#there are none
mpg[(mpg.manufacturer == 'dodge') & ~(mpg['class'].isin(['suv','minivan','pickup']))]
#so I assume they meant which dodge VEHICLE has the best/worst mileage:
mpg[mpg.manufacturer == 'dodge'].nlargest(columns='avg_mpg',n=1,keep='all')
mpg[mpg.manufacturer == 'dodge'].nsmallest(columns='avg_mpg',n=1,keep='all')

#3) MAMMALS DATASET
data('Mammals',show_doc=True)

mam = data('Mammals')
# # rows/cols
print(f'There are {mam.shape[0]} rows in this dataframe') 
print(f'There are {mam.shape[1]} columns in this dataframe')
mam.info()
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   weight    107 non-null    float64
#  1   speed     107 non-null    float64
#  2   hoppers   107 non-null    bool   
#  3   specials  107 non-null    bool

mam.describe()
#             weight       speed
# count   107.000000  107.000000
# mean    278.688178   46.208411
# std     839.608269   26.716778
# min       0.016000    1.600000
# 25%       1.700000   22.500000
# 50%      34.000000   48.000000
# 75%     142.500000   65.000000
# max    6000.000000  110.000000
#  3 ways to get weight of the fastest animal
mam[mam.speed == mam.speed.max()].weight ##55
mam.sort_values(by='speed',ascending=False).head(1) #55 - doesn't work if tie for fastest
mam.nlargest(columns='speed',n=1,keep='all') #55

# percentage of specials
mam[mam.specials].shape[0]/mam.shape[0]*100 #9.3%
#hoppers w/ above median speed
mam[mam.hoppers & (mam.speed > mam.speed.median())].shape[0] # 7
mam[mam.hoppers & (mam.speed > mam.speed.median())].shape[0]*100 / mam.shape[0] # 6.5%

