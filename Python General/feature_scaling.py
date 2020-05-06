import numpy as np
import pandas as pd
import pandas as pd
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

##################################################
#"https://jovianlin.io/feature-scaling/"
#"https://towardsdatascience.com/scale-standardize-or-normalize-with-scikit-learn-6ccc7d176a02"
##################################################

np.random.seed(1)



df = pd.DataFrame({'x1':np.random.normal(0,2,10000),
'x2':np.random.normal(5,3,10000),
'x3':np.random.normal(-5,5,10000)
})
print(df.head())
scale = preprocessing.StandardScaler()
scale_df = scale.fit_transform(df)
scale_df = pd.DataFrame(scale_df,columns=['x1','x2','x3'])
print(scale_df.head())

fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(10,10))
# *** you have to pass both row and column in subplots

ax1.set_title("Before scaling")
sns.kdeplot(df['x1'],ax=ax1)

sns.kdeplot(df['x2'],ax=ax1)

sns.kdeplot(df['x3'],ax=ax1)


ax2.set_title("After scaling")
sns.kdeplot(scale_df['x1'],ax=ax2)

sns.kdeplot(scale_df['x2'],ax=ax2)

sns.kdeplot(scale_df['x3'],ax=ax2)

# Ecudian distance
# cosine distance
# Manhaten distancce 
# BERT ==> 
# Text data apply ML model

###################################################

df = pd.DataFrame({'x1':np.random.chisquare(8,1000),
'x2':np.random.beta(8,2,1000) * 40,
'x3':np.random.normal(50,3,1000)})

scale = preprocessing.MinMaxScaler()
scale_df = scale.fit_transform(df)

scale_df = pd.DataFrame(scale_df,columns=['x1','x2','x3'])
fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(6,5))
# *** you have to pass both row and column in subplots

ax1.set_title("Before scaling")
sns.kdeplot(df['x1'],ax=ax1)

sns.kdeplot(df['x2'],ax=ax1)

sns.kdeplot(df['x3'],ax=ax1)

ax2.set_title("After scaling")
sns.kdeplot(scale_df['x1'],ax=ax2)

sns.kdeplot(scale_df['x2'],ax=ax2)

sns.kdeplot(scale_df['x3'],ax=ax2)

#########################################################
x = pd.DataFrame({'x1':np.concatenate([np.random.normal(20,1,1000),
np.random.normal(1,1,25)]),

'x2':np.concatenate([np.random.normal(30,1,1000),
np.random.normal(50,1,25)]),
})

scale = preprocessing.RobustScaler()
rob_scale_df = scale.fit_transform(x)

rob_scale_df = pd.DataFrame(rob_scale_df,columns=['x1','x2'])


fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(6,5))
# *** you have to pass both row and column in subplots

ax1.set_title("Before scaling")
sns.kdeplot(x['x1'],ax=ax1)

sns.kdeplot(x['x2'],ax=ax1)



ax2.set_title("After scaling")
sns.kdeplot(rob_scale_df['x1'],ax=ax2)

sns.kdeplot(rob_scale_df['x2'],ax=ax2)


df = pd.DataFrame({'X':np.random.randint(-100,100,1000).astype(float),
'y':np.random.randint(-80,80,1000).astype(float),
'z':np.random.randint(-150,150,1000).astype(float),
})

#print(df.head())

scale = preprocessing.Normalizer()
scale_df = scale.fit_transform(df)
scaled_df = pd.DataFrame(scale_df,columns=df.columns)
print(df.head())
print("#"*30)
print(scaled_df.head())

fig = plt.figure(figsize=(9,5))
# 1,2,1 == right,  121 is wrong and used in old version(2.7-)
ax1= fig.add_subplot(1,2,1,projection='3d')
ax2=fig.add_subplot(1,2,2,projection='3d')
ax1.scatter(df['X'],df['y'],df['z'])
ax2.scatter(scaled_df['X'],scaled_df['y'],scaled_df['z'])
plt.show()

