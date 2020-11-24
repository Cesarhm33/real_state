#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


df = pd.read_csv('LArealestate.csv')
df


# In[ ]:


df.info()


# In[ ]:


df.city.isnull().sum()


# In[ ]:


df.city.unique()


# In[ ]:


df['city']= df['city'].replace('culver city', 'Culver City')


# In[ ]:


dummy_variable_1 = pd.get_dummies(df["city"])


# In[ ]:


dummy_variable_1


# In[ ]:


dummy_variable_2 = pd.get_dummies(df["type"])
dummy_variable_2


# In[ ]:


df = pd.concat([df, dummy_variable_1], axis=1)
df = pd.concat([df, dummy_variable_2], axis=1)


# In[ ]:


del df['city']#elimino city la he hecho dummy
del df['type']#elimino type la he hecho dummy
del df['condo']#elimino condo por que type tiene dos variables


# In[ ]:


df.head()


# In[ ]:


df['Beverly Hills'].value_counts()


# In[ ]:


df['Culver City'].value_counts()


# In[ ]:


df['Palms'].value_counts()


# In[ ]:


fig, ax = plt.subplots(figsize=(5,5))
sns.boxplot(df['Beverly Hills'],df["price"])


# In[ ]:


fig, ax = plt.subplots(figsize=(5,5))
sns.boxplot(df['Palms'],df["price"])


# In[ ]:


fig, ax = plt.subplots(figsize=(5,5))
sns.boxplot(df['Culver City'],df["price"])


# In[ ]:




