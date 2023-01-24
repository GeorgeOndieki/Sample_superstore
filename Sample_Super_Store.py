#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import openpyxl as xl
import numpy as np


# In[28]:


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python practise files\SampleSuperstore.csv")


# In[29]:


df.head()


# In[30]:


# We start by cleaning data and knowing the data types and the shape
df.info()


# In[31]:


# shape
df.shape


# In[32]:


# check for null values
df.isna().sum()
# no null values available


# In[33]:


# check for presence of duplicates
df.duplicated().any()


# In[34]:


# we get rid of the duplicates
df1= df.drop_duplicates()


# In[35]:


df1


# In[36]:


df1.drop(columns='Postal Code',inplace=True)


# In[37]:


# The mostly used mode of shipment
sb.countplot(x='Ship Mode', data=df1)


# In[38]:


# lets find the most convinient mode of shipment which result to more profits.

sb.barplot(x='Ship Mode', y='Profit', data= df1 )


# In[39]:


# The most sold Category
sb.countplot(x='Category', data=df1)


# In[40]:


#The most profitable category
sb.barplot(x='Category', y='Profit', data= df1 , estimator=np.mean)


# In[41]:


# Lets find out the sub-category of goods with the least profits
df1.groupby('Sub-Category').Profit.sum().sort_values()


# In[42]:


plt.figure(figsize=(16,10))
sb.barplot(x='Sub-Category', y='Profit', data= df1)


# In[43]:


# The most sold Segment
sb.countplot(x='Segment', data=df1)


# In[44]:


# The most profitable sold segment

sb.barplot(x='Segment',y='Profit' ,data=df1 , estimator=sum)


# In[45]:


df1.State.value_counts()


# In[46]:


plt.figure(figsize=(20,9))
plt.xticks(rotation=90)
sb.set_style('whitegrid')
sb.countplot(x='State',data=df1)


# In[47]:


df1.Region.value_counts().plot(kind='bar')


# In[48]:


df1.corr()


# In[49]:


df1.cov()


# In[50]:


# To find the correlation of values
sb.pairplot(df1)


# In[51]:


# let us find out if the sales and profit correlate
df1.plot(x='Sales', y='Profit', kind= 'scatter')


# In[ ]:





# In[52]:


sb.relplot(x='Sales',y='Profit', hue='Segment' , data=df1)

