
from csv import writer
import json
import pandas as pd

keywordId = 10000000
categoryId = 1000
jDict = dict()
jDict['keyword'] = {}
jDict['category'] = {}
print(jDict)
df = pd.read_csv("data.csv")
total_rows=len(df.axes[0])
# lis = [['Internship', 'work'], ['chicken', 'food'], ['chicken', 'food'], ['chicken', 'food'], ['chicken', 'food']]
for _ in range(total_rows):
    keyW = df.loc[_,'keyword']
    catW = df.loc[_,'category']

    if keyW not in jDict['keyword'].keys():
        keywordId += 1
        jDict['keyword'][keyW] = keywordId

    if catW not in jDict['category'].keys():
        categoryId += 1
        jDict['category'][catW] = categoryId

    with open('data1.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([jDict['keyword'][keyW],jDict['category'][catW]])
        f_object.close()

print(jDict)
json_object = json.dumps(jDict, indent = 2)
print(jDict)
with open("dict.json", "w") as outfile:
    json.dump(jDict, outfile)

#

