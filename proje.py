import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv("database.csv")
print(data.columns)
data=data[["Date","Time","Latitude","Longitude","Depth","Magnitude"]]
print(data.head())

import datetime,time
timeSet=[]
zip()
for d,t in zip (data["Date"], data["Time"]):
    try:
        ts=datetime.datetime.strptime(d+' '+t,"%m-%d-%Y %H:%M:%S")
        timeSet.append(ts.timetuple())
        

    except ValueError:
        timeSet.append("ValuEror")
timeSet=pd.Series(timeSet)
data["Pctime"]=timeSet.values
final_data=data.drop(["Date","Time"],axis=1)
final_data=final_data[final_data.Pctime!="ValuEror"]
print(final_data.head())


from mpl_toolkits.basemap import Basemap 
m=Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution="c")
enlem=data["Latitude"].tolist()
boylam=data["Longitude"].tolist()
x,y=m(boylam,enlem)
figur=plt.figure(figsize=(12,10))
plt.title("Deprem Haritası")
m.plot(x,y,"o",markersize=2,color="blue")
m.drawcoastlines()
m.fillcontinents(color="coral",lake_color="aqua")
m.drawmapboundary()
m.drawcountries()
plt.show()