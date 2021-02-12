import sys
import itertools as IT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


        
selected_variables = ['Parties_Description', 'CommercialData_EstimatedHHIncome', 'EthnicGroups_EthnicGroup1Desc']


#ADD THE NEEDED FILENAME AND PUT THE GRAPHS IN THE 
state_demographic = pd.read_csv('ak2-onepercent-sample.csv', usecols=selected_variables)
Party_freq= {}

All_freq = {}
Income_freq = {}
ethnic_freq = {}

for i in range(len(state_demographic)) : 
    All_freq.update({i:[state_demographic.loc[i, "Parties_Description"],state_demographic.loc[i, "CommercialData_EstimatedHHIncome"],state_demographic.loc[i, "EthnicGroups_EthnicGroup1Desc"] ] })
for x in All_freq:
    
        if All_freq[x][1] in Party_freq:
            if All_freq[x][0] in Party_freq[All_freq[x][1]]:
                Party_freq[All_freq[x][1]][All_freq[x][0]] += 1

            else:
                #Party_freq[All_freq[x][1]]= {}
                Party_freq[All_freq[x][1]][All_freq[x][0]] = 1
        else:
            Party_freq[All_freq[x][1]]= {}
            Party_freq[All_freq[x][1]][All_freq[x][0]] = 1

for x in All_freq:
    
        if All_freq[x][2] in ethnic_freq:
            if All_freq[x][0] in ethnic_freq[All_freq[x][2]]:
                ethnic_freq[All_freq[x][2]][All_freq[x][0]] += 1

            else:
                ethnic_freq[All_freq[x][2]][All_freq[x][0]] = 1
        else:
            ethnic_freq[All_freq[x][2]]= {}
            ethnic_freq[All_freq[x][2]][All_freq[x][0]] = 1
            

index = Party_freq.keys()
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
for x in Party_freq:
    #print(x)
    if 'Constitution' in Party_freq[x]:
        a.append(Party_freq[x]['Constitution'])
    else:
        a.append(0)

    if 'Democratic' in Party_freq[x]:
        b.append((Party_freq[x]['Democratic']))
    else:
        b.append(0)

    if 'Green Libertarian' in Party_freq[x]:
        c.append(Party_freq[x]['Green Libertarian'])
    else:
        c.append(0)
    if 'Independence' in Party_freq[x]:
        d.append(Party_freq[x]['Independence'])
    else:
        d.append(0)
    if 'Libertarian' in Party_freq[x]:
        e.append(Party_freq[x]['Libertarian'])
    else:
        e.append(0)
    if 'Non-Partisan' in Party_freq[x]:
        f.append(Party_freq[x]['Non-Partisan'])
    else:
        f.append(0)
    if 'Other' in Party_freq[x]:
        g.append(Party_freq[x]['Other'])
    else:
        g.append(0)
    if 'Republican' in Party_freq[x]:
        h.append(Party_freq[x]['Republican'])
    else:
        h.append(0)
    if 'Unknown' in Party_freq[x]:
        i.append(0)
    else:
        i.append(0)
 
      

df = pd.DataFrame({'Constitution': a, 'Democratic': b, 'Green Libertarian': c, 'Independence': d, 'Libertarian': e, 'Non-Partisan': f, 'Other': g, 'Republican':h }, index=index)
ax = df.plot.bar(rot=0)
plt.xticks(fontsize=6, rotation=30)
plt.xlabel("INCOME RANGE")
plt.ylabel("COUNT")
plt.title('Income VS. Political Parties')
#plt.show()

ax.figure.savefig('Income_Parties.pdf')

index2  = ethnic_freq.keys()
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
for x in ethnic_freq:
    #print(x)
    if 'Constitution' in ethnic_freq[x]:
        a.append(ethnic_freq[x]['Constitution'])
    else:
        a.append(0)

    if 'Democratic' in ethnic_freq[x]:
        b.append((ethnic_freq[x]['Democratic']))
    else:
        b.append(0)

    if 'Green Libertarian' in ethnic_freq[x]:
        c.append(ethnic_freq[x]['Green Libertarian'])
    else:
        c.append(0)
    if 'Independence' in ethnic_freq[x]:
        d.append(ethnic_freq[x]['Independence'])
    else:
        d.append(0)
    if 'Libertarian' in ethnic_freq[x]:
        e.append(ethnic_freq[x]['Libertarian'])
    else:
        e.append(0)
    if 'Non-Partisan' in ethnic_freq[x]:
        f.append(ethnic_freq[x]['Non-Partisan'])
    else:
        f.append(0)
    if 'Other' in ethnic_freq[x]:
        g.append(ethnic_freq[x]['Other'])
    else:
        g.append(0)
    if 'Republican' in ethnic_freq[x]:
        h.append(ethnic_freq[x]['Republican'])
    else:
        h.append(0)
    if 'Unknown' in ethnic_freq[x]:
        i.append(0)
    else:
        i.append(0)
 
      

df2 = pd.DataFrame({'Constitution': a, 'Democratic': b, 'Green Libertarian': c, 'Independence': d, 'Libertarian': e, 'Non-Partisan': f, 'Other': g, 'Republican':h }, index=index2)
ax2 = df2.plot.bar(rot=0)
plt.xticks(fontsize=6, rotation=45)
plt.xlabel("Ethnicities")
plt.ylabel("COUNT")
plt.title('Ethnicity VS. Political Parties')
#plt.show()

ax2.figure.savefig('Ethnicity_Parties.pdf')






