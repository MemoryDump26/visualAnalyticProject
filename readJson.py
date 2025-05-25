import pandas as pd
import json

dataFile = open('perCountryData.json', 'r')
data = json.load(dataFile)

'''
print(len(data['regions']))
print(data['regions'][0].keys())

print(len(data['regions'][0]['distributions']))
print(data['regions'][0]['distributions'][0].keys())
print(data['regions'][0]['distributions'][0]['distribution'][0].keys())

print(data['regions'][0]['cluster_names'])
'''

'''
"cluster_names": [],
"distributions": [
    "country": string,
    "distribution": [
        {
            "cluster_counts": {

            },
            "total_sequences": int,
            "week": date,
        }
    ]
],

'''
df_columns = ['Country', 'Week', 'Total sequences'] + data['regions'][0]['cluster_names'] + ['others']
df = pd.DataFrame(columns=df_columns)

for country in data['regions'][0]['distributions']:
    for week in country['distribution']:
        others = week['total_sequences'] - sum(week['cluster_counts'].values())
        d = {
            'Country': [country['country']],
            'Week': [week['week']],
            'Total sequences': [week['total_sequences']],
            **week['cluster_counts'],
            'others': [others],
        }

        df = pd.concat([df, pd.DataFrame(d)])

# df = df.fillna(0)
df = df.replace(0, float('nan'))
print(df)
df.to_csv('output.csv')
