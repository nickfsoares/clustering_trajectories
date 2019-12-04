#Nicolas de Freitas Soares
#Insight Lab	

#importing important libraries
import pandas as pd
import seaborn as sns 
sns.set(style='darkgrid')
import matplotlib.pyplot as plt
%matplotlib inline

moves=pd.read_csv("https://raw.githubusercontent.com/InsightLab/PyMove/developer/examples/geolife_sample.csv")
moves.head()

#dividing the Data
print(moves.head())
#portanto dividi dem dois moves diferentes
move1=moves[moves['id']==1]
move5=moves[moves['id']==5]
#sns.lmplot('lat','lon',data=move1,size=7,sharey=True)
#plt.title('Total Moves from id=1')
#plt.xlabel('Latitude')
#plt.ylabel('Longitude')
#plt.show()

#Creating day,month and year labels
day=[]
month=[]
year=[]
for k in range(0,len(move1['datetime']),1):
    year.append(move1['datetime'][k].split()[0].split('-')[0])
    month.append(move1['datetime'][k].split()[0].split('-')[1])
    day.append(move1['datetime'][k].split()[0].split('-')[-1])
    
move1['day']=day
move1['month']=month
move1['year']=year

#Dividing data (id1) per month
Move_October=move1[move1['month']=='10']
Move_November=move1[move1['month']=='11']
Move_December=move1[move1['month']=='12']
