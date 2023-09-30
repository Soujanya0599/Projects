#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries

# In[1]:


#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns


# ## Loading heart stroke dataset

# In[2]:


df = pd.read_csv('heart_stroke_dataset.csv') #dataset uploaded to jupyter notebook


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.shape


# In[8]:


total = df.isnull().sum()
null_values = pd.concat([total], axis=1, keys=['Total'])
null_values


# # Data transformation

# ## Cleaning the data based on missing values
# 
# 

# In[9]:


df.drop("id", axis=1, inplace=True)


# In[10]:


## Dropping instances with missing data on smoking_status attribute as they cannot be estimated or predicted easily without any other factrors
df = df[df['smoking_status'].notna()]


# In[11]:


df


# ## Replacing missing BMI data with its mean based on age and gender

# In[12]:


age_groups=[]

for v in df["age"]:
#     print(v)
    if v<=6:
        age_groups.append("0-6")
    elif v<=12:
        age_groups.append("7-12")
    elif v<=18:
        age_groups.append("13-18")
    elif v<=24:
        age_groups.append("19-24")
    elif v<=30:
        age_groups.append("25-30")
    elif v<=45:
        age_groups.append("31-45")
    elif v<60:
        age_groups.append("46-59")
    elif v>=60:
        age_groups.append("60+")

df['age_group']= age_groups
df


# In[13]:


total = df.isnull().sum()
null_values = pd.concat([total], axis=1, keys=['Total'])
null_values


# In[14]:


mean_bmi_by_gender_age = df.groupby(['age_group','gender'])['bmi'].mean().apply(lambda x: round(x,1))
mean_bmi_by_gender_age


# In[15]:


for v in df['age_group'].unique():
    df.loc[(df['age_group']==v) & (df['gender']=='Male'),'bmi'] = df.loc[(df['age_group']==v) & (df['gender']=='Male'),'bmi'].fillna(mean_bmi_by_gender_age.loc[v]['Male'])
    df.loc[(df['age_group']==v) & (df['gender']=='Female'),'bmi'] = df.loc[(df['age_group']==v) & (df['gender']=='Female'),'bmi'].fillna(mean_bmi_by_gender_age.loc[v]['Female'])
    
    if df.loc[(df['age_group']==v) & (df['gender']=='Other'),'bmi'].empty==False:
        df.loc[(df['age_group']==v) & (df['gender']=='Other'),'bmi'] = df.loc[(df['age_group']==v) & (df['gender']=='Other'),'bmi'].fillna(mean_bmi_by_gender_age.loc[v]['Other'])


# In[16]:


total = df.isnull().sum()
null_values = pd.concat([total], axis=1, keys=['Total'])
null_values


# In[17]:


df


# In[18]:


df.info()


# In[19]:


df.describe()


# In[20]:


df.columns


# In[21]:


df.shape


# In[22]:


df.to_csv(r'transformed_heart_stroke_data.csv')


# # Data Visualization

# In[23]:


attributes = df.select_dtypes(include=[object]).columns

for v in attributes:  
    print(v ,":", df[v].unique())


# In[25]:


fig, axs = plt.subplots(6, 2, figsize=(15,25))

i=1
j=1

df1=df.loc[df['stroke']==1]
df2=df.loc[df['stroke']==0]

for v in attributes:
    sns.countplot(x=v,data=df1,ax=axs[i-1][0])
    axs[i-1][0].set_xlabel(v)
    axs[i-1][0].set_ylabel('People with heart stroke')


    sns.countplot(x=v,data=df2,ax=axs[i-1][1])
    axs[i-1][1].set_xlabel(v)
    axs[i-1][1].set_ylabel('People without heart stroke')

    j+=1
    if j%2==0:
        j=1
        i+=1

plt.savefig("countplot.jpg")

