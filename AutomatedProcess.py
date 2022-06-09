# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:28:42 2022

@author: nicko
"""

#Importing libraries needed for automation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading data into script
df1 = pd.read_excel('C:/Users/nicko/Downloads/my_python/shift-data.xlsx')
df2 = pd.read_excel('C:/Users/nicko/Downloads/my_python/third-shift-data.xlsx')

#Imported data, let me check .head for first five rows
print(df1.head(), df2.head())

#Doing an quick analysis check on employees from both shifts
#Want to pull out list of all employees within both of my xlsx
print(df1['Name'], df2['Name'])


#Confirmed list, now let's combine both sheets into one
df_combined = pd.concat([df1,df2])
print(df_combined)
#above .concat keeps all 6 columns, but now has combined to total of 58 rows (58x6)


#Performing calculation below
pivot = df_combined.groupby(['Shift']).mean()
productivity_of_shifts = pivot.loc[:, "Production Run Time (Min)":"Products Produced (Units)"]
print(productivity_of_shifts)




#Graphing data for visualization
productivity_of_shifts.plot(kind='bar')
plt.show()

#Analyzing data above, shift number 3 is more productive then shift 1, coming in at 128.33 avg units produced VS 54.48 from shift 1



#Output my data into a new sheet that will contain analysis information on Production Run Time, and Products Produced by both shifts
df_combined.to_excel('Results.xlsx')
