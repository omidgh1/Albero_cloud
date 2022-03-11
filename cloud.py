#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px


# In[2]:


app_time = pd.read_csv('app_time_50.csv',index_col=False)
device_time = pd.read_csv('device_time_50.csv',index_col=False)
device_fix = pd.read_csv('device_fix_50.csv',index_col=False)
users = pd.read_csv('users_50.csv',index_col=False)
del app_time['Unnamed: 0']
del device_time['Unnamed: 0']
del device_fix['Unnamed: 0']
del users['Unnamed: 0']


# In[3]:


st.title('Albero Air Cloud Simulation')
users


# In[64]:


def info(x):
    user_selected_ID = x['User_ID'].values[0]
    name_sur = x['Name'].values[0]+' '+x['Surname'].values[0]
    email = 'Email: '+str(x['Email'].values[0])
    phone = 'Phone: '+str(x['phone'].values[0])
    address = 'Address: '+str(x['address'].values[0])
    st.title(name_sur)
    st.text(phone)
    st.text(email)
    st.text(address)
    device_fix_selected_table = device_fix[device_fix['User_ID'] == user_selected_ID]
    device_fix_selected_table[device_fix_selected_table.columns[1:]]
    return device_fix_selected_table


# In[69]:


option = st.sidebar.selectbox('How would you like to search?',('User ID', 'Name'))
user_ID = 'U101'
if option == 'User ID':
    user_ID = st.sidebar.selectbox('Please choose your user ID?',users['User_ID'].values)
    user_selected_table = users[(users['User_ID']==user_ID)]
    user_ID = user_selected_table['User_ID'].values[0]
    device_fix_selected_table = info (user_selected_table)
else:
    st.sidebar.text('Please Enter the first and last name')
    First_name = st.sidebar.text_input("First name", 'Aiken')
    Last_name = st.sidebar.text_input("Last name", 'Hatchett')
    user_selected_table = users[(users['Name']==First_name)&(users['Surname']==Last_name)]
    user_ID = user_selected_table['User_ID'].values[0]
    device_fix_selected_table = info (user_selected_table)


# In[71]:


st.sidebar.text('for which device you need the plot?')
devices_id = device_fix_selected_table['Device_ID'].values
Device_ID = st.sidebar.selectbox('Please choose the Device ID?',devices_id)
a = device_time.loc[device_time['Device_ID']==Device_ID][['Date','Voc','Temp','Humidity']]


# In[73]:


fig = px.line(a, x='Date', y=["Voc",'Temp','Humidity'])
st.plotly_chart(fig)

device_time[device_time['Device_ID']==Device_ID][-10:]




