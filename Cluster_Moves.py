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

###########################################################################################################################
#FUNCTIONS

#######################################################################
#funcao para criar uma array de fetores move.inertia_
def inertia_array(Move_Data):
    from sklearn.cluster import KMeans
    k=1
    inertia=[]
    while (k<11):
        kmeans=KMeans(n_clusters=k)
        modelo=kmeans.fit(Move_Data.get(['lat','lon']))
        inertia.append(modelo.inertia_)
        k=k+1
    return inertia 
#######################################################################
#funcao para plotar os gráficos do DataFrame identado
def Inertia_Graph(Move_Data):
    Error=inertia_array(Move_Data)
    k=[]
    for i in range(1,11,1):
        k.append(i)
    ax=sns.stripplot(k,Error,linewidth=3,size=10);
    ax.set(xlabel="Number of Clusters",ylabel="Min_Squared_Error")
    plt.title("The Elbow Method")
    plt.show()
###########################################################################
#funcao para dividir o DF em k clusters
def Move_lat_lon(k,MOVER):
    from sklearn.cluster import KMeans
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(MOVER.get(['lat','lon']))
    
    fig, (ax1,ax2) =plt.subplots(nrows=1,ncols=2,figsize=(15,6))

    ax1.set_title("Original")
    ax1.scatter(MOVER['lat'],MOVER['lon'],s=4)

    ax2.set_title("Kmeans")
    ax2.scatter(MOVER['lat'],MOVER['lon'],c=kmeans.labels_,s=4,cmap='rainbow')
    plt.show()
    return



