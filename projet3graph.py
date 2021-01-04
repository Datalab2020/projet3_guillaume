#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import metrics


# In[2]:


DATABASES = {
    'bdd_garnaud':{
        'NAME': 'bdd_garnaud',
        'USER': 'garnaud',
        'PASSWORD': '>JGi5%Lh?$dv',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    },
}

# choose the database to use
db = DATABASES['bdd_garnaud']

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user = db['USER'],
    password = db['PASSWORD'],
    host = db['HOST'],
    port = db['PORT'],
    database = db['NAME'],
)


# In[3]:


engine = create_engine(engine_string)


# In[4]:


df = pd.read_sql_table('infos',engine)
df2 = pd.read_sql_table('blagues',engine)


# In[5]:


df.info()
df2.info()


# In[6]:


df.describe
df2.describe


# In[7]:



df2.shape


# In[8]:



df2.columns


# In[9]:


df2.head(10)


# In[10]:


newdf=['rate','vote']
df[newdf].mean()


# In[11]:


df[newdf].sort_values(by = 'vote', ascending = False)


# In[12]:


df[newdf].sort_values(by = 'rate', ascending = False)


# In[13]:


df2.describe


# In[14]:


df2.info()


# In[15]:


del df2['id']


# In[16]:


df2.info()


# In[17]:


df2.describe


# In[18]:


print(df2.loc[df2['citations'] == 'gun'])


# In[19]:


df2[df2['citations'] == "gun"]


# In[20]:


guerre=df2[df2['citations'].str.contains("gun|bomb|fight|kill|combat|revolver")]


# In[21]:


guerre


# In[22]:


cuisine=df2[df2['citations'].str.contains("dinner|eat|cooking|meal|breakfast|food|lunch")]


# In[23]:


cuisine


# In[24]:


les_fêtes=df2[df2['citations'].str.contains("birthday|fireworks|dancing|santa|gift|christmas|party|thanksgiving")]


# In[25]:


les_fêtes


# In[26]:


df = pd.read_sql_table('infos',engine)
df2 = pd.read_sql_table('blagues',engine)


# In[27]:


result = pd.merge(df, df2, on='id')


# In[28]:


result


# In[29]:


virus=result[result['citations'].str.contains("Coronavirus|flu|tired|sick|cold|bone fracture|cancer|disease")]
virus
f=sns.scatterplot(x="rate", y="vote", data=virus)


# In[30]:


les_fêtes=result[result['citations'].str.contains("birthday|fireworks|dancing|santa|gift|christmas|party|thanksgiving")]


# In[31]:


les_fêtes


# In[32]:


f=sns.scatterplot(x="rate", y="vote", data=les_fêtes)


# In[33]:


cuisine=result[result['citations'].str.contains("dinner|eat|cooking|meal|breakfast|food|lunch")]


# In[34]:


sns.scatterplot(x="rate", y="vote", data=cuisine)


# In[35]:


guerre=result[result['citations'].str.contains("gun|bomb|fight|kill|combat|revolver")]


# In[36]:


sns.scatterplot(x="rate", y="vote", data=guerre)


# In[38]:


le_sport=result[result['citations'].str.contains("sport|basket|football|soccer|tennis|ping pong|swimming|marathon|volley-ball|combat sport|golf")]


# In[39]:


le_sport


# In[40]:


sns.scatterplot(x="rate", y="vote", data=le_sport)


# In[ ]:




