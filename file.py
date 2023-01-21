#!/usr/bin/env python
# coding: utf-8

# # dataframe :1

# In[165]:


# Read data
import pandas as pd
import numpy as np
df_ = pd.read_csv("C:/Users/nextgenraptor/Downloads/check_data.csv")
print("The number of rows: ", len(df_.index))
df = df_.copy()
df['New Attribute Name'] = df['New Attribute Value']                         = df['Remarks']= np.nan # 3 new columns
#df


# In[166]:


print("The number of rows with attribute name 'thread size': ", len(df[df['attribute_name'] == "Thread Size"].index))


# In[167]:


# df[df['attribute_name'] == "Ultimate Shear in 3000 PSI Concrete (Lb.)"]
# df[df['attribute_value'] == "rp_303 Stainless Steel"]
# df[df['attribute_value'] == "rp_Zinc Plated Steel"]
# Find the rows to split
df.loc[(df['attribute_value'] == "rp_Zinc Plated Steel") |       (df['attribute_value'] == "rp_303 Stainless Steel") |       (df['attribute_name'] == "Thread Size"), 'Remarks'] = 'Split'
print("The number of rows to split: ", len(df[df['Remarks'] == "Split"].index))
df.loc[df['attribute_name'] == "Ultimate Shear in 3000 PSI Concrete (Lb.)" , 'Remarks'] = "Merge"
print("The number of rows to merge: ", len(df[df['Remarks'] == "Merge"].index))
#df[df['Remarks'] == "Split"]
# (df['attribute_name'] == "Ultimate Shear in 3000 PSI Concrete (Lb.)")


# In[168]:


# To make New Attribute Name = attribute_name and New Attribute Value = attribute_value
df.loc[(df['Remarks'] == "Split") |        (df['Remarks'] == "Merge"), 'New Attribute Name'] = df["attribute_name"]
df.loc[(df['Remarks'] == "Split") | (df['Remarks'] == "Merge"), 'New Attribute Value'] = df["attribute_value"]
#df[df['Remarks'] == "Split"]
#df[df['Remarks'] == "Merge"]
#df


# # dataframe1 = df

# #  dataframe : 2

# In[151]:


df2= df_[df_['attribute_name'] == "Ultimate Shear in 3000 PSI Concrete (Lb.)"]
print("The number of rows :", len(df2.index))
df2["New Attribute Name"] = df2["attribute_name"].str.split(' ').str[0] + ' ' + df2["attribute_name"].str.split(' ').str[1]
df2["New Attribute Value"] = df2['attribute_value'] +" lbs."
df2['Remarks']= np.nan
#df2


# # dataframe = df2

# # dataframe :3

# In[152]:


df3a= df_[df['attribute_value'] == "rp_303 Stainless Steel"]
print("The number of rows :", len(df3a.index))
df3a["New Attribute Name"] = "Grade"
df3a["New Attribute Value"] = df3a["attribute_value"].str.split(' ').str[0]
df3a['Remarks']= np.nan
#df3a


# In[153]:


df3b= df_[df['attribute_value'] == "rp_303 Stainless Steel"]
print("The number of rows :", len(df3b.index))
df3b["New Attribute Name"] = df3b["attribute_name"]
df3b["New Attribute Value"] = df3b["attribute_value"].str.split(' ').str[1] + ' '+ df3b["attribute_value"].str.split(' ').str[2]
df3b['Remarks']= np.nan
#df3b


# # dataframe 3 = df3a,  df3b

# # dataframe :4

# In[154]:


df4a= df_[df['attribute_value'] == "rp_Zinc Plated Steel"]
print("The number of rows :", len(df4a.index))

df4a["New Attribute Name"] = "Finish"
df4a["New Attribute Value"] = df4a["attribute_value"].str.split(' ').str[0] + ' ' + df4a["attribute_value"].str.split(' ').str[1]
df4a['Remarks']= np.nan
#df4a


# In[155]:


df4b= df_[df['attribute_value'] == "rp_Zinc Plated Steel"]
print("The number of rows :", len(df4b.index))

df4b["New Attribute Name"] = df4b["attribute_name"]
df4b["New Attribute Value"] = df4b["attribute_value"].str.split(' ').str[-1]
df4b['Remarks']= np.nan
#df4b


# # dataframe :5

# In[170]:


df5a= df_[df['attribute_name'] == "Thread Size"]
print("The number of rows :", len(df5a.index))
df5a


# In[ ]:


df4a["New Attribute Name"] = "Finish"
df4a["New Attribute Value"] = df4a["attribute_value"].str.split(' ').str[0] + ' ' + df4a["attribute_value"].str.split(' ').str[1]
df4a['Remarks']= np.nan
#df4a


# In[ ]:





# In[ ]:





# In[ ]:





# # dataframe 4 = df4a, df4b

# In[156]:


frames = [df, df2, df3a, df3b, df4a, df4b]
result = pd.concat(frames)
print("Number of rows : ", len(result. index))
result = result.sort_values("entity_id")
result.to_csv('file19072022.csv')

