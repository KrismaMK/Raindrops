#!/usr/bin/env python
# coding: utf-8

# # Load in packages

# In[97]:


import pandas as pd
import seaborn as sns


# # Add in data

# In[82]:


MiamiRain = pd.read_excel('C:/Users/19546/OneDrive/Documents/Data Science Class/FINAL PROJECT/Miami, FL data/Miami Intl Airport Rain.xlsx')


# In[83]:


MiamiRain.head()


# ## Seperate year and month

# In[84]:


MiamiRain["date"]


# In[85]:


def git_year(series):
    str_series=str(series)
    year=str_series[:4]
    return year 


# In[86]:


MiamiRain["year"]=MiamiRain["date"].apply(git_year)


# In[87]:


MiamiRain["year"]


# In[88]:


def git_month(series):
    str_series=str(series)
    month=str_series[4:6]
    return month


# In[89]:


MiamiRain["month"]=MiamiRain["date"].apply(git_month)


# In[90]:


MiamiRain["month"]


# In[91]:


MiamiRain['year']= MiamiRain["year"].map(str)


# ### Check updated data

# In[92]:


MiamiRain.head()


# ### Remove unwanted column

# In[93]:


del MiamiRain['date']


# In[94]:


MiamiRain.head()


# ### Remove NA data

# In[95]:


MiamiRain.dropna(how ='any')


# # Create Histogram for precipitation

# In[104]:


sns.displot(MiamiRain, y="year")


# ## View histograms for all data 

# In[105]:


sns.pairplot(MiamiRain)


# In[ ]:




