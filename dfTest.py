import pandas as pd
import numpy as np
import math

df = pd.read_csv('output.csv')

dff = df[df['Country']=='Vietnam']
dff = dff.dropna(axis='columns', how='all')

week_hover = {}

for idx, row in dff.iterrows():
    sortedRow = row[4:].sort_values(ascending=False)
    sortedRow = sortedRow.dropna(how='all')
    week_hover.update({row['Week']: sortedRow.to_dict()})

# print(week_hover)

def get_hover_info(week, data):
    info = data.get(week, {})
    
    result = ''
    for variant, amount in info.items():
        result += str(variant)
        result += ': '
        result += str(amount)
        result += '<br>'
    return result

customdata=[get_hover_info(_x, week_hover) for _x in week_hover.keys()],
print(customdata)

