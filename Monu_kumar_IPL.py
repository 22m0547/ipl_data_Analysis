#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Analysis of the IPL Data using Python with the help of libraries like Pandas, Matplotib and Seaborn.


# In[7]:


#loading the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[8]:


#loading the ipl matches dataset
ipl=pd.read_csv('matches.csv')


# In[9]:


#having a glance at the first five records of the dataset
ipl.head()


# In[12]:


#Lookin at the number of rows and columns in the dataset
ipl.shape


# In[13]:


#Getting the frequency of most man of the match awards
ipl['player_of_match'].value_counts()


# In[14]:


#Getting the top 10 players with most man of the match awards
ipl['player_of_match'].value_counts()[0:10]


# In[15]:


#Getting the top 5 players with most man of the match awards
ipl['player_of_match'].value_counts()[0:5]


# In[16]:


#making a bar-plot for the top 5 players with most man of the match awards
plt.figure(figsize=(5,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]))
plt.show()


# In[17]:


#Getting the frequency of result column
ipl['result'].value_counts()


# In[18]:


#Finding out the number of toss wins w.r.t each team
ipl['toss_winner'].value_counts()


# In[19]:


#Extracting the records where a team won batting first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[20]:


#Looking at the head
batting_first.head()


# In[21]:


#Making a histogram 
plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.show()


# In[22]:


#Finding out the number of wins w.r.t each team after batting first
batting_first['winner'].value_counts()


# In[23]:


#Making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[ ]:





# In[24]:


#Making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[25]:


#extracting those records where a team has won after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[26]:


#looking at the head
batting_second.head()


# In[27]:


#Making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[28]:


#Finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[29]:


#Making a bar plot for top-3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["blue","green","orange"])
plt.show()


# In[30]:


#Making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[31]:


#Looking at the number of matches played each season
ipl['season'].value_counts()


# In[32]:


#Looking at the number of matches played in each city
ipl['city'].value_counts()


# In[33]:


#Finding out how many times a team has won the match after winning the toss
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[34]:


325/636

