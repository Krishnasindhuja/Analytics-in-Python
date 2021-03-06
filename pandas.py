#determining the correlation of the date from solar companies using plots and matrices depending on their returns 

import datetime
import matplotlib.pyplot as plt
import pandas_datareader as data
start = datetime.datetime(2015,7,1)
end = datetime.datetime(2016,6,1)
solar_df = data.DataReader(['FSLR','TAN','RGSE','SCTY'],'google',start,end)['Close']
solar_df
rets=solar_df.pct_change()
rets
#plt.scatter(rets.FSLR,rets.TAN)  #better correlated 
#plt.scatter(rets.RGSE,rets.SCTY) #not well correlated 
solar_corr = rets.corr()
solar_corr
plt.scatter(rets.mean(),rets.std())
plt.xlabel('Expected returns')
plt.ylabel('Standard deviation')
for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(
    label,
    xy = (x,y), xytext=(-20,20),
    textcoords = 'offset points', ha='right', va='bottom',
    bbox = dict(boxstyle='round, pad=0.5', fc='yellow', alpha= 0.5),
    arrowprops = dict(arrowstyle='->',connectionstyle = 'arc3,rad=0')
    )
plt.show()
