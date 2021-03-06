#regression over the solar industry data

import numpy as np 
import statsmodels.api as sm 
X = solar_df[['FSLR','SCTY','RGSE']]
X = sm.add_constant(X)
Y=solar_df['TAN']
model = sm.OLS(Y,X,missing = 'drop') #Ordinary least squares 
result = model.fit()
print(result.summary())


fig, ax = plt.subplots(figsize=(6,4))
ax.plot(Y)
ax.plot(result.fittedvalues)
