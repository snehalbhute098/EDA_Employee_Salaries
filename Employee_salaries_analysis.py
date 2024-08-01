#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv('Salaries.csv')


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.describe()


# In[7]:


data.head(10)


# In[8]:


# check last 10 rows of dataset


# In[9]:


data.tail(10)


# In[10]:


# Find shape of our dataset(no of rows and column)


# In[12]:


data.shape


# In[13]:


# Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement


# In[16]:


data.info()


# In[15]:


print("number of rows", data.shape[0])
print ( "number of columns", data.shape[1])


# In[17]:


#Check Null Values In The Dataset


# In[19]:


data.isnull().sum()


# In[20]:


# Drop ID, Notes, Agency, and Status Columns(extra columns cleaning)


# In[22]:


data.columns


# In[23]:


data =data.drop(['Id','Notes','Agency','Status'],axis=1)


# In[24]:


data


# In[25]:


#. Get Overall Statistics About The Dataframe


# In[26]:


data.describe()


# In[28]:


data.describe(include='all')


# In[29]:


#Find Occurrence of The Employee Names  (Top 5) (for occurence use value_count)


# In[30]:


data.columns


# In[33]:


data['EmployeeName'].value_counts().head(5)


# In[34]:


#Find The Number of Unique Job Titles


# In[35]:


data.columns


# In[39]:


data['JobTitle'].nunique()


# In[ ]:


#Total Number of Job Titles Contain Captain (case=false we have to make it case sensitive), len for count,and str.contains for presence of the tittle


# In[48]:


len(data[data['JobTitle'].str.contains('CAPTAIN',case=False)])


# In[50]:


data[data['JobTitle'].str.contains('CAPTAIN',case=False)].count()


# In[51]:


#Display All the Employee Names From Fire Department


# In[52]:


data.columns


# In[60]:


data[data['JobTitle'].str.contains('Fire',case=False)]['EmployeeName']


# In[61]:


#Find Minimum, Maximum, and Average BasePay


# In[63]:


data['BasePay'].describe()


# In[64]:


#Replace 'Not Provided' in EmployeeName' Column to NaN 


# In[71]:


import numpy as np
data['EmployeeName']=data['EmployeeName'].replace('Not provided',np.NaN)


# In[72]:


data['EmployeeName']


# In[73]:


#for permanent change we have included the data = data


# In[74]:


#Drop The Rows Having 5 Missing Values


# In[80]:


data[data.isnull().sum(axis=1)==5]


# In[82]:


data.columns


# In[89]:


data.drop(data[data.isnull().sum(axis=1)==5].index, axis=0, inplace=True)


# In[91]:


data.isnull().sum(axis=1)


# In[92]:


#basically first we have seen the isnull and sum of it of the rows only then value them as 5 and then make the change in the tabe and then update the column with provided index and then make the permanent change in the table 


# In[93]:


#Find Job Title of ALBERT PARDINI


# In[94]:


data.columns


# In[99]:


data[data['EmployeeName']== 'ALBERT PARDINI']['JobTitle']


# In[100]:


#How Much ALBERT PARDINI Make (Include Benefits)?


# In[101]:


data.columns


# In[103]:


data[data['EmployeeName']== 'ALBERT PARDINI']['TotalPayBenefits']


# In[105]:


data.columns


# In[120]:


data.info()


# In[122]:


data['BasePay'].dtypes


# In[130]:


#top 5 most common jobs 


# In[131]:


data.columns 


# In[135]:


data['JobTitle'].value_counts()


# In[ ]:




