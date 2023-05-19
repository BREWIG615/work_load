import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sys import argv

script, source = argv

df = pd.read_excel("work_load.xlsx")
# source = input('Name of person: ')

df = df[df['Num_of_hours'].notna()]

cat = []
for i in df['title']:
    cat.append(i)

index = cat
hrs = df['Num_of_hours']

plt.barh(index, hrs)
plt.title(source)
plt.yticks(cat)

plt.show()