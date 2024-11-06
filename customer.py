#!/usr/bin/env python
# coding: utf-8

# In[33]:


#import the necessary libraries
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# In[34]:


#load the combined data
df = pd.read_csv('combined_data.csv')
df.head()


# - Perform customer segmentation(RFM SEGMENTATION)
# 1. Perform RFM- Recency, Frequency and Monetary 
# - Recency: How recently did a customer make a purchase? Helps identify active vs. dormant customers.
# - Frequency: How often does a customer buy products? Identifies loyal customers with frequent purchases.
# - Monetary: How much does a customer spend? Shows high-value customers who contribute more revenue.

# In[35]:


#perform customer segmentation
#get the recency, Frequency and Monetary value of each customer
#first, combine the MONTH_ID, YEAR_ID, DAY_ID to form a single date column
df['Date'] = df[['YEAR_ID','MONTH_ID','DAY_ID']].apply(lambda x: '-'.join(x.values.astype(str)), axis=1)
df.head()


# In[36]:


#change the date column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# In[37]:


#calculate the recency, frequency and monetary value of each customer
#get the most recent date in the dataset
most_recent_date = df['Date'].max()

# Calculate Recency as the difference in days between the most recent date and each customer's last purchase date
df['Recency'] = df.groupby('CustomerName')['Date'].transform(lambda x: (most_recent_date - x.max()).days)   

# Calculate Frequency as the number of unique purchase dates per customer. We use transform to broadcast the result back to the original dataframe
df['Frequency'] = df.groupby('CustomerName')['Date'].transform('nunique')

# Calculate Monetary as the total Exact Sales per customer.
df['Monetary'] = df.groupby('CustomerName')['Exact Sales'].transform('sum')

#drop the duplicate rows
rfm = df[['CustomerName', 'Recency','Frequency','Monetary']].drop_duplicates()




# In[38]:


rfm.head(15)


# In[39]:


#sort the data by recency, frequency and monetary value
rfm = rfm.sort_values(by=['Recency','Frequency','Monetary'], ascending=[True, False, False])
rfm.head(15)


# In[40]:


#apply the RFM scoring as before
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1]).astype(int)
# Use pd.cut() with custom bin ranges
rfm['F_Score'] = pd.cut(rfm['Frequency'], bins=4, labels=[1, 2, 3, 4]).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4]).astype(int)
rfm['RFM_Score'] = rfm['R_Score'] * 100 + rfm['F_Score'] * 10 + rfm['M_Score']

print(rfm[['CustomerName', 'R_Score', 'F_Score', 'M_Score', 'RFM_Score']])


# In[41]:


df['CustomerName'].nunique()


# In[42]:


#group the customers into segments
# Define rfm_level function
def rfm_level(df):
    if df['RFM_Score'] >= 300:
        return 'Best Customers'
    elif ((df['RFM_Score'] >= 200) and (df['RFM_Score'] < 300)):
        return 'Average Customers'
    elif ((df['RFM_Score'] >= 100) and (df['RFM_Score'] < 200)):
        return 'Potential Customers'
    else:
        return 'Churned Customers'
    

# Create a new variable RFM_Level
rfm['RFM_Level'] = rfm.apply(rfm_level, axis=1)

rfm.head()  


# In[43]:


#plot the customer segments
#fig = px.scatter(rfm, x='Recency', y='Frequency', color='RFM_Level', title='RFM Segments')
#fig.show()


# In[44]:


# plot the customer segments
#fig = px.scatter(rfm, x='Recency', y='Monetary', color='RFM_Level', title='RFM Segments')
#fig.show()


# In[45]:


#plot bar chart of th breakdown of customers in the best customers segment
#fig = px.bar(rfm['RFM_Level'].value_counts().sort_values(ascending=True).reset_index(), x='count', y='RFM_Level', title='Breakdown of Customers in Each Segment')
#fig.show()


# ## Time Analysis for the Customers

# - Extract the names of days from the Date column.

# In[46]:


#extract the day of the week from the date column
df['Day'] = df['Date'].dt.day_name()
df.head()


# In[47]:


#get the total sales per day of the week
#total_sales_per_day = df.groupby('Day')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
#plot the total sales per day of the week
#fig = px.bar(total_sales_per_day, x='Day', y='Exact Sales', title='Total Sales per Day of the Week')
#fig.show()


# - Analyze the days with highest sales for the best_customers segments

# - Best Customers

# In[48]:


#analyze the time series of these customers
#first, get the data for the best customers
#best_customers = best_customers['CustomerName'].values
#get the complete data of customers in the best customers segment
#best_customers_data = df[df['CustomerName'].isin(best_customers)]
#best_customers_data.head()


# ## Geography Segmentation 
# - Analyze customer location data to understand which regions generate the most revenue, have higher order frequencies, or larger average order values.

# In[49]:


# Grouping data by city, country, and territory to get aggregates
region_data = df.groupby(['CustomerName','City', 'Country', 'Territory']).agg({
    'Exact Sales': 'sum',
    'Total Profit': 'sum',
    'QuantityOrdered': 'count'
}).reset_index()
# Calculate the average order value- the average amount spent per order
region_data['Average_Order_Value'] = region_data['Exact Sales'] / region_data['QuantityOrdered']



# In[50]:


region_data.head()


# In[51]:


#segment the regions in quartiles
# Defining segmentation conditions
conditions = [
    (region_data['Exact Sales'] > region_data['Exact Sales'].quantile(0.75)) & 
    (region_data['Total Profit'] > region_data['Total Profit'].quantile(0.75)),
    (region_data['Exact Sales'] < region_data['Exact Sales'].quantile(0.25)) & 
    (region_data['Total Profit'] < region_data['Total Profit'].quantile(0.25))
]
# Defining the labels for each segment
labels = ['Top Region', 'Underperforming Region']
# Creating the Segment column. np.select- assigns the label based on the conditions
region_data['Segment'] = np.select(conditions, labels, default='Average Region')


# In[52]:


region_data.head()


# In[53]:


# Creating a map visualization
fig = px.scatter_geo(region_data, 
                     locations="Country",
                     locationmode="country names",
                     color="Segment",
                     hover_name="City",
                     size="Exact Sales",
                     projection="natural earth",
                     title="Geographic Segmentation by Sales and Profit")
st.plotly_chart(fig)


# - Perform Kmeans clustering

# In[54]:


#perform clustering - to group customers based on their RFM scores
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#select the RFM scores
rfm_scores = rfm[['Recency', 'Frequency', 'Monetary']]
#standardize the data
scaler = StandardScaler()
#apply the scaler
rfm_scores_scaled = scaler.fit_transform(rfm_scores)

#instantiate the KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
#fit the model
kmeans.fit(rfm_scores_scaled)
#predict the clusters
rfm['Cluster'] = kmeans.predict(rfm_scores_scaled)  
rfm['Cluster'].value_counts()


# In[55]:


#combine the customer segments with the clusters
rfm['Cluster'] = rfm['Cluster'].map({0:'Cluster 1', 1:'Cluster 2', 2:'Cluster 3'})
rfm.head()


# In[56]:


#display customers in each cluster
fig = px.scatter(rfm, x='Recency', y='Frequency', color='Cluster', title='Clusters of Customers', labels={'Recency':'Recency (Days)', 'Frequency':'Frequency (No. of Orders)'})
st.plotly_chart(fig)


# In[57]:


# for each cluster, plot the customerName and monetary value
fig = px.bar(rfm.groupby('Cluster')['Monetary'].sum().sort_values(ascending=False).reset_index(), x='Cluster', y='Monetary', title='Total Sales by Cluster')
fig.update_layout(
    bargap=0.5,
    xaxis_title='Cluster',
    yaxis_title='Monetary Input ($)',
    

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)

)
st.plotly_chart(fig)
    


# In[58]:


#display all customers in each cluster
#cluster 1
cluster1 = rfm[rfm['Cluster']=='Cluster 1'].sort_values(by='Monetary', ascending=False)
fig = px.bar(cluster1.head(10), x='Monetary', y='CustomerName', title='Cluster 1(Top 10, Low Recency and Low Frequency)', category_orders={'CustomerName': cluster1['CustomerName'].to_list()})
fig.update_layout(
    bargap=0.1,
    xaxis_title='Monetary Input ($)',
    yaxis_title='Customer Name',
    

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[59]:


#bottom 10 customers in cluster 1 make it a vertical bar chart
cluster1_bottom = rfm[rfm['Cluster']=='Cluster 1'].sort_values(by='Monetary', ascending=True)
fig = px.bar(cluster1_bottom.head(10), x='Monetary', y='CustomerName', title='Cluster 1( Bottom 10, Low Recency and Low Frequency)')
fig.update_layout(
    bargap=0.1,
    xaxis_title='Monetary Input ($)',
    yaxis_title='Customer Name',
    hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)
)
st.plotly_chart(fig)


# In[60]:


#cluster 1 time series
cluster1_data = df[df['CustomerName'].isin(cluster1['CustomerName'].values)]
cluster1_seasonality = cluster1_data.groupby(['YEAR_ID','MONTH_ID'])['Exact Sales'].sum().reset_index()
fig = px.line(cluster1_seasonality, x='MONTH_ID', y='Exact Sales', color='YEAR_ID', title='Seasonality of Cluster 1')
st.plotly_chart(fig)


# In[61]:


#day of the week with the highest sales
cluster1_data = cluster1_data.groupby('Day')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster1_data, x='Day', y='Exact Sales', title='Day of the Week with the Highest Sales(cluster 1)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Day',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[62]:


#show which products are the most popular in each cluster
#combine the cluster data with the main data
cluster1 = cluster1.merge(df, on='CustomerName')
cluster1_products = cluster1.groupby('ProductLine')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster1_products, x='ProductLine', y='Exact Sales', title='Most Popular Products in Cluster 1')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Product Line',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[64]:


#


# In[65]:


#cluster 2      
cluster2 = rfm[rfm['Cluster'] == 'Cluster 2'].sort_values(by='Monetary', ascending=False)
fig = px.bar(cluster2.head(10), x='Monetary', y='CustomerName', title='Cluster 2 (Top 10, High Recency and Low Frequency)',category_orders={'CustomerName': cluster2['CustomerName'].tolist()})
fig.update_layout(
    barmode='stack',
    bargap=0.2,
    xaxis_title='Monetary Input ($)',
    yaxis_title='Customer Name',
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)
#order the bars from the highest to the lowest

st.plotly_chart(fig)


# In[ ]:


#bottom 10 cluster 2
cluster2_bottom = rfm[rfm['Cluster'] == 'Cluster 2'].sort_values(by='Monetary', ascending=True)
fig = px.bar(cluster2_bottom.head(5), x='Monetary', y='CustomerName',title='Cluster 2 (Bottom 5, High Recency and Low Frequency)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Monetary Input ($)',
    yaxis_title='Customer Name',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[66]:


#cluster 2 time series
cluster2_data = df[df['CustomerName'].isin(cluster2['CustomerName'].values)]
cluster2_seasonality = cluster2_data.groupby(['YEAR_ID','MONTH_ID'])['Exact Sales'].sum().reset_index()
fig = px.line(cluster2_seasonality, x='MONTH_ID', y='Exact Sales', color='YEAR_ID', title='Seasonality of Cluster 2')
st.plotly_chart(fig)


# In[67]:


#day of the week with the highest sales
cluster2_data = cluster2_data.groupby('Day')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster2_data, x='Day', y='Exact Sales', title='Day of the Week with the Highest Sales(cluster2)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Day',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[68]:


#cluster 2
cluster2 = cluster2.merge(df, on='CustomerName')
cluster2_products = cluster2.groupby('ProductLine')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster2_products, x='ProductLine', y='Exact Sales', title='Most Popular Products in Cluster 2')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Product Line',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[ ]:




# In[ ]:


#cluster 3
cluster3 = rfm[rfm['Cluster']=='Cluster 3'].sort_values(by='Monetary', ascending=False)
fig = px.bar(cluster3, x='CustomerName', y='Monetary',title='Cluster 3(Low Recency and High Frequency)')
fig.update_layout(
    bargap=0.6,
    xaxis_title='Customer Name',
    yaxis_title='Monetary Input ($)',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[ ]:


#cluster 3 time series
cluster3_data = df[df['CustomerName'].isin(cluster3['CustomerName'].values)]
cluster3_seasonality = cluster3_data.groupby(['YEAR_ID','MONTH_ID'])['Exact Sales'].sum().reset_index()
fig = px.line(cluster3_seasonality, x='MONTH_ID', y='Exact Sales', color='YEAR_ID', title='Seasonality of Cluster 3')
st.plotly_chart(fig)


# In[ ]:


#day of the week with the highest sales
cluster3_data = cluster3_data.groupby('Day')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster3_data, x='Day', y='Exact Sales', title='Day of the Week with the Highest Sales(cluster3)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Day',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[ ]:


#cluster 3
cluster3 = cluster3.merge(df, on='CustomerName')
cluster3_products = cluster3.groupby('ProductLine')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(cluster3_products, x='ProductLine', y='Exact Sales', title='Most Popular Products in Cluster 3')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Product Line',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[ ]:




# - Time Analysis in General 

# In[69]:


#TOTAL SALES PER DAY OF THE WEEK
total_sales_per_day = df.groupby('Day')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(total_sales_per_day, x='Day', y='Exact Sales', title='Total Sales per Day of the Week(In General)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Day',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[71]:


#total product line sales   
total_product_sales = df.groupby('ProductLine')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(total_product_sales, x='ProductLine', y='Exact Sales', title='Total Sales per Product Line(In general)')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Product Line',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)

)
st.plotly_chart(fig)


# In[72]:


#top 10 countries with highest sales
total_country_sales = df.groupby('Country')['Exact Sales'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(total_country_sales.head(10), x='Country', y='Exact Sales', title='Top 10 Countries with the Highest Sales')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Country',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[73]:


#bottom 10 countries with lowest sales
total_country_sales = df.groupby('Country')['Exact Sales'].sum().sort_values(ascending=True).reset_index()
fig = px.bar(total_country_sales.head(10), x='Country', y='Exact Sales', title='Bottom 10 Countries with the Lowest Sales')
fig.update_layout(
    bargap=0.4,
    xaxis_title='Country',
    yaxis_title='Exact Sales',

hoverlabel=dict(
    bgcolor="white",
    font_size=16,
    font_family="Rockwell"
)



)
st.plotly_chart(fig)


# In[ ]:


#save rfm table as csv
rfm.to_csv('rfm', index=False)


# In[ ]:




