import itertools
import json

import pandas as pd
from itertools import  chain
data_population = pd.read_csv("population-by-zip-code.csv")
de = pd.DataFrame(data_population)
pop=de[' Population']
z=de['Zip Code']

zip_li=dict(zip(de['Zip Code'],de[' Population']))
#print("dictionary is",zip_li)

data_states = pd.read_csv("states.csv")
df = pd.DataFrame(data_states)

d = df[['Long', ' Zip Codes']].head()
#print("long and zip are",d)
L=df['Long']

s = pd.Series(df[' Zip Codes'])
print("series is",s)
zip_code_li = []
for val in s:
     #print(type(val))
     val_s=val.replace('"',"")
     #print("val_s is",val_s)
     zip_code_li.append(val_s.split())
     #print(zip_code_li)

ans_list=list(itertools.chain.from_iterable(zip_code_li))
#print("ans is",ans_list)
sum_dic = dict(zip(d['Long'], d[' Zip Codes']))

    #print("i value is",int(i))
    #print(zip_li.get(int(i)))
    #print("state value is",states)
def add():
   dic_total={}
   for state, zipc in sum_dic.items():
        zip_va = sum_dic[state].replace('"', "")
        zip_spil = zip_va.split()
        #print(zip_spil)
        Total = 0
        for i in zip_spil:
            #print(i)
            if i in ans_list:
                ans_pop = zip_li.get(int(i))
                # print("answer pop is",ans_pop)
                Total =Total+ ans_pop
        print(f"{state} total papulation is : {Total}")
        dic_total[state]=Total
        print("dictionary is",dic_total)   #dictionary
        pop_total=[dict(zip([state],[Total])) for state,Total in dic_total.items()]  #dictionary in a list

        average_pop = int((sum(pop))/len(z))
        print("average of population  per zip",average_pop)
        average_state=int((sum(pop))/len(L))
        print("average of population per state",average_state)

        output={}
        output["Pop_Total_by_State"] = pop_total
        output["average_pop_per_zip"]=average_pop
        output["averege_pop_per_state"]=average_state

   with open("Total_Data.json","w") as DA:
       json.dump(output,DA)


for states in d['Long']:
    add()
    break













