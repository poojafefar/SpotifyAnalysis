# -*- coding: utf-8 -*-
"""analysis-of-spotify-trends (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vh8higYN_S15FcJutIJw03Y344jVFJRM

![image.png](data:image/png;base64,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)

# **Introduction :**
---
> Spotify is an audio streaming platform that provides DRM-restricted music, videos, and podcasts from record labels and media companies. It has more than 50 million tracks which user can browse using various parameters like artists, album, genre, or via playlists.



---

> Here we have taken the data of top 50 songs of 2019 from spotify database and we have performed various data analytics and visualisation operations on the dataset. Hereby using these mathematical models we can analyise the genre, beats per minute, loudness, valence, length, acousticeness, speechiness and hence finding out the popularity and the common thread between them.

---

>
"""

# Commented out IPython magic to ensure Python compatibility.
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # used for working with arrays & linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy import stats # used for scientific computing and technical computing.
!pip install squarify
import squarify as sq # Bar charts can't be effective to handle and visualize large data 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns # provides a high-level interface for drawing attractive and informative statistical graphics
import sklearn #including classification, regression, clustering and dimensionality reduction
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB,BernoulliNB
from sklearn.svm import LinearSVC, SVC
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
# %matplotlib inline
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

"""### **Question 1: Print the first 5 rows that are present in the data?**"""

filename='top50.csv'
df=pd.read_csv(filename,encoding='ISO-8859-1')
df.head()

"""

```
# This is formatted as code
```

### **Question 2: How many rows and columns are present in the data?**"""

#Calculates the number of rows and columns
print(df.shape)

"""### **Question 3: Rename the columns as given below?**
Track.Name:'track_name'

*  Artist.Name:'artist_name'
*  Track.Name:'track_name'
* Genre: 'genre'
*   Energy: 'energy'
*   Liveness: 'liveness'
*   List item
*   Popularity: 'popularity"
* Loudness..dB..:'Loudness(dB)'
* Valence.:'Valence' 
* Speechiness-:Speechiness
* Acousticness..:'Acousticness'
* Beats.Per.Minute:'beats_per_minute'
* Length.:'Length'
"""

#Renaming the columns
df.rename(columns={'Track.Name':'track_name','Artist.Name':'artist_name','Beats.Per.Minute':'beats_per_minute','Loudness..dB..':'Loudness(dB)','Valence.':'Valence','Length.':'Length', 'Acousticness..':'Acousticness','Speechiness.':'Speechiness'},inplace=True)
df.head()

"""
### **Question 4: Replace all the null values and missing values by '0'?**"""

#counts the null values and replace it by 0
df.isnull().sum() #show the missing values in the data set 
df.fillna(0)

from google.colab import drive
drive.mount('/content/drive')

"""
### **Question 5: What are the datatypes of the different columns in the dataset?**

"""

# The datatypes of the different attributes of the dataset
print(df.dtypes)

"""


### **Question 6 : How many genre are there? List the number of songs in each genre.**

---

"""

#Calculating the number of songs of each genre
print(type(df['Genre']))
popular_genre=df.groupby('Genre').size().unique
print(popular_genre)
genre_list=df['Genre'].values.tolist()

"""
### **Question 7 : How many artist are there? list the number of songs each artist has created.**"""

#Calculating the number of songs by each of the artists
print(df.groupby('artist_name').size())
popular_artist=df.groupby('artist_name').size()
print(popular_artist)
artist_list=df['artist_name'].values.tolist()

"""
### **Question 8 : Set the precision for the data values in the table 3.**"""

pd.set_option('precision', 3)
df.describe()

"""

###  **Question 9 : Plot a histogram for the dataset keeping liveness as the base measure with normalization bin size - 10.**
"""

#Finding out the skew for each attribute
skew=df.skew()
print(skew)
# Removing the skew by using the boxcox transformations
#transform=np.asarray(df[['Liveness']].values)
#df_transform = stats.boxcox(transform)[0]
# Plotting a histogram to show the difference 
plt.hist(df['Liveness'],bins=10) #original data
plt.show()

"""

### **Question 10 : Calculate the correlation among the attributes. Set the precision at 3 use the spearman method to plot.**

"""

pd.set_option('display.width', 100)
pd.set_option('precision', 3)
correlation=df.corr(method='spearman')
print(correlation)

"""

### **Question 11 : Plot a bar graph with count of tracks on the Y axis and Genre on the X axis**

"""

xtick = ['dance pop', 'pop', 'latin', 'edm', 'canadian hip hop',
'panamanian pop', 'electropop', 'reggaeton flow', 'canadian pop',
'reggaeton', 'dfw rap', 'brostep', 'country rap', 'escape room',
'trap music', 'big room', 'boy band', 'pop house', 'australian pop',
'r&b en espanol', 'atl hip hop']
length = np.arange(len(xtick))
genre_groupby = df.groupby('Genre')['track_name'].agg(len)
plt.figure(figsize = (15,7))
plt.bar(length, genre_groupby)
plt.xticks(length,xtick)
plt.xticks(rotation = 90)
plt.xlabel('Genre', fontsize = 20)
plt.ylabel('Count of the tracks', fontsize = 20)
plt.title('Genre vs Count of the tracks', fontsize = 25)

"""### **Question 12 : Plot a heatmap showing correlation between different attributes?**








"""

# heatmap of the correlation 
plt.figure(figsize=(10,5))
plt.title('Correlation heatmap')
sns.heatmap(correlation,annot=True,vmin=-1,vmax=1,cmap="GnBu_r",center=1)

"""

### **Question 13 : Plot a bar graph with count of songs on the Y axis and Artist Name on the X axis**

"""

fig = plt.figure(figsize = (15,7))
df.groupby('artist_name')['track_name'].agg(len).sort_values(ascending = False).plot(kind = 'bar')
plt.xlabel('Artist Name', fontsize = 20)
plt.ylabel('Count of songs', fontsize = 20)
plt.title('Artist Name vs Count of songs', fontsize = 30)

"""### **Question 14 : Plot data and a linear regression model corresponding to loudness and energy attributes.** """

# Analysing the relationship between energy and loudness
fig=plt.subplots(figsize=(10,10))
sns.regplot(x='Energy',y='Loudness(dB)',data=df,color='black')

"""### **Question 15 : Plot regression model on energy and popularity also plot its kernel density estimate** """

fig=plt.subplots(figsize=(10,10))
plt.title('Dependence between energy and popularity')
sns.regplot(x='Energy', y='Popularity',ci=None, data=df) #regression plot
sns.kdeplot(df.Energy,df.Popularity) #kernel density estimation

"""### **Question 16 : Plot a scatter matrix to show the interdependency between the attributes of the dataset.**"""

scatter_matrix(df)
plt.gcf().set_size_inches(20, 20)
plt.show()

"""### **Question 17 : Plot a box plot of each attributes scaling from 0 to 50 .**"""

df.plot(kind='box', subplots=True)
plt.gcf().set_size_inches(20,10)
plt.show()

"""

### **Question 18 : Plot a square chart on the basis of number of song .**
 

"""

plt.figure(figsize=(14,8))
sq.plot(sizes=df.Genre.value_counts(), label=df["Genre"].unique(), alpha=.8 )
plt.axis('off')
plt.show()

"""### **Question 19 : Plot a pie chart on the number of songs created by each artist.**"""

#Pie charts 
labels = df.artist_name.value_counts().index
sizes = df.artist_name.value_counts().values
colors = ['red', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan', 'green', 'black','yellow']
plt.figure(figsize = (10,10))
plt.pie(sizes, labels=labels, colors=colors)
autopct=('%1.1f%%')
plt.axis('equal')
plt.show()

#Linear regression, first create test and train dataset
x=df.loc[:,['Energy','Danceability','Length','Loudness(dB)','Acousticness']].values
y=df.loc[:,'Popularity'].values

# Creating a test and training dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

# Linear regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

#Displaying the difference between the actual and the predicted
y_pred = regressor.predict(X_test)
df_output = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_output)

#Checking the accuracy of Linear Regression
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.figure(figsize=(10,10))
plt.plot(y_pred,y_test,color='black',linestyle='dashed',marker='*',markerfacecolor='red',markersize=10)
plt.title('Error analysis')
plt.xlabel('Predicted values')
plt.ylabel('Test values')

# Cross validation score
x=df.loc[:,['Energy','Danceability']].values
y=df.loc[:,'Popularity'].values
regressor=LinearRegression()
mse=cross_val_score(regressor,X_train,y_train,scoring='neg_mean_squared_error',cv=5)
mse_mean=np.mean(mse)
print(mse_mean)
diff=metrics.mean_squared_error(y_test, y_pred)-abs(mse_mean)
print(diff)

x=df.loc[:,['artist_name']].values
y=df.loc[:,'Genre'].values

# Label encoding of features
x.shape
encoder=LabelEncoder()
x = encoder.fit_transform(x)
x=pd.DataFrame(x)
x

# Label Encoding of target
Encoder_y=LabelEncoder()
Y = Encoder_y.fit_transform(y)
Y=pd.DataFrame(Y)
Y

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 1)

#Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(x_train)
x_train=sc.transform(x_train)
x_test=sc.transform(x_test)

# KNN Classification
# sorted(sklearn.neighbors.VALID_METRICS['brute'])
knn = KNeighborsClassifier(n_neighbors = 17)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)

error=[]
for i in range(1,30):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i=knn.predict(X_test)
    error.append(np.mean(pred_i!=y_test))

plt.figure(figsize=(10,10))
plt.plot(range(1,30),error,color='black',marker='o',markerfacecolor='cyan',markersize=10)
plt.title('Error Rate K value')
plt.xlabel('K Value')
plt.ylabel('Mean error')

x=df.loc[:,['Energy','Length','Danceability','beats_per_minute', 'Acousticness']].values
y=df.loc[:,'Popularity'].values

# Creating a test and training dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred=gnb.predict(X_test)
df_output = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_output)

# Testing the accuracy of Naive Bayes 
scores=cross_val_score(gnb,X_train,y_train,scoring='accuracy',cv=3).mean()*100
print(scores)

sns.jointplot(x=y_test, y=y_pred, kind="kde", color="r")

x=df.loc[:,['Energy','Length','Danceability','beats_per_minute', 'Acousticness']].values
y=df.loc[:,'Popularity'].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

# Linear SVM model 
LinSVC = LinearSVC(penalty='l2', loss='squared_hinge', dual=True)
LinSVC.fit(X_train, y_train)
y_pred=gnb.predict(X_test)
df_output = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_output)

# Testing the accuracy
scores=cross_val_score(LinSVC,X_train,y_train,scoring='accuracy',cv=3).mean()*100
print(scores)

sns.jointplot(x=y_test, y=y_pred, kind="reg", color="b");

