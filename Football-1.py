
# coding: utf-8

# In[72]:


import os
get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[103]:


data = pd.read_csv("C:/Users/Santhoshkumar/Desktop/Abhi/pbp-2016.csv")
data = data.drop(['Minute','Second','IsTwoPointConversionSuccessful','RushDirection','YardLineFixed','YardLineDirection', 'IsPenaltyAccepted', 'PenaltyTeam','PenaltyType','PenaltyYards'], axis =1)
data = data.drop(['IsFumble','IsInterception','IsMeasurement','Challenger','IsChallengeReversed','PassType','IsTouchdown','SeriesFirstDown','Unnamed: 10','ToGo','YardLine'], axis = 1)
data = data.drop(['NextScore','Description','Unnamed: 17', 'SeasonYear','IsIncomplete','IsChallenge'], axis = 1)
data = data.drop(['Unnamed: 12','Unnamed: 16','TeamWin','GameId'],axis = 1)
data = data.dropna()
#cut all the unwanted data, cleaning - abhi
#ata = pd.concat([data, pd.get_dummies(data['Formation'])], axis =1)
#ata = data.drop(['Formation'], axis = 1)
data = pd.concat([data, pd.get_dummies(data['PlayType'])], axis =1)
data = data.drop(['PlayType'], axis = 1)
column_a = data['Yards']
column_a
b = []

# print (data.groupby(['Formation','Yards']).groups)
data


# In[121]:


df = pd.read_csv("Madden-NFL-17-Launch-Ratings-Full-League.csv")
df = df[["First", "Last", "Team", "Position", "OVR"]]
#read the csv file, and take the first last team position and ovr - abhi

df = df.sort_values("OVR", ascending=False)
#sort based on OVR in descending order - abhi

teams =  np.unique(df[['Team']])
#put all the data from 'Team' into a list teams -abhi

posi = np.unique(df[['Position']])
#put all the data from 'position' into a list position -abhi


# In[ ]:


dict = {'C': 1, 'CB': 2, 'DT' : 2, 'FS' : 1, 'HB' : 2, 'LE' : 1, 'LG' : 1, 'LOLB' : 1, 'LT' : 1, 'MLB' : 2, 'QB' : 1, 'RE' : 1, 'RG' : 1, 'ROLB' : 1, 'RT': 1, 'SS':1,'TE':1, 'WR' : 3}


# In[161]:


filtered = []
refiltered = []

for i in teams:
    for p in posi:
        #nested for loop
        #append two things, from the df data structure, take the "team" value at i and
        #the "position" value at p
        #Take the head(1), which is the first part of the df data structure, and take the value
        #I wanna take only a set number of positions, 
        filtered.append((df[(df["Team"]==i) & (df["Position"] == p)].head(1).values))
        
for j in filtered:
    for k in j:
        print(k)

    #iterate through the list


# In[154]:




