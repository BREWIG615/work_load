import jinja2
import os 
from jinja2 import Template
import pandas as pd 
import numpy as np
import re



df = pd.read_excel('workload2.xlsx')

rows = df.to_dict(orient = 'records')

df = df.melt('person')

df = df[df['value'].notna()]

"""grouped_df = df.groupby('person'), ('variable', ';'.join), ('value', ';'.join) 

for key, item in grouped_df:
    print(grouped_df.get_group(key), "\n\n")
"""
df = df.reindex()
