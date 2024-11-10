# Toys Sales Analysis Using Power BI

![Overall Performance](https://i.ytimg.com/vi/2fIXb2wWh1k/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBDsSO86ka9HrdUYGRqXpfNwPCHiA)


## Group Members

Faith Wafula

Lydiah Njeri

Mathew Kararani

Martin Karimi

Nancy Maina


# Project Overview

This project aims to apply data analytics techniques to a real-world business challenge. The objective is to analyze sales data from a toy business and build an intuitive dashboard that provides actionable insights for improving sales performance and supporting strategic decision-making.

# Business Problem

A toy company, operating across various product categories, seeks to:

a) Identify trends in overall business performance.

b) Highlight the best and worst-selling products.

c) Understand customer profiles and preferences.

d) Detect seasonal or trend-based patterns in sales.

# Objectives

a) Design a Power BI dashboard that provides interactive, high-impact visuals of key performance indicators (KPIs).

b) Deliver insights on sales trends, customer segmentation, and product performance.

c) Enable the business to make data-driven decisions that enhance profitability and growth.

# Data Description
The dataset is provided in an Excel workbook named Sales Data with the following components:

Main Data: Contains sales transaction details.

Product Master: Lists product-specific information.

Data Dictionary: Describes fields in both the Main Data and Product Master sheets.

# Dataset
The dataset used in this project consists of multiple sheets, including Main Data, Product Master, and a Data Dictionary describing the following fields:

# Field Name	Description
Field Name	Description
OrderNumber	Unique: identifier for each order.

QuantityOrdered:	Number of units ordered for a specific product.

PriceEach:	Price per unit of the product.

OrderLineNumber:	Line number of the product in the order, used to distinguish items in a single order.

Sales: 	Total sales amount for the order line (calculated as QuantityOrdered * PriceEach).

OrderDate:	Date when the order was placed.

Status: 	Current status of the order (e.g., Shipped, Cancelled, Pending).

QTR_ID:	Quarter in which the order was placed.

DAY_ID: 	Day on which the order was placed.

MONTH_ID:	Month in which the order was placed.

YEAR_ID:	Year in which the order was placed.

ProductLine:	Category or line to which the product belongs.

MSRP:	Manufacturer's Suggested Retail Price for the product.

ProductCode:	Unique code identifying the product.

CustomerName:	Full name of the customer placing the order.

Phone: 	Customer's contact phone number.

AddressLine1:	First line of the customer's address.

City:	City where the customer is located.

PostalCode:	Postal or ZIP code for the customer's address.

Country:	Country where the customer is located.

Territory:	Geographical sales territory associated with the customer.

ContactLastName:	Last name of the customer contact person.

ContactFirstName:	First name of the customer contact person.

Branch:	Branch or location responsible for handling the order.


# Data Cleaning and Preparation

The data cleaning and preparation process includes the following steps:

1. Import Files: Load all required files into Power BI.

2. Remove Inconsistencies in the sales and Territory  column: Ensure data integrity by removing any inconsistency rows across all files.

3. Data Type Conversion: Convert the temporal data   from  integer to Date format for accurate calculations.

4. Establish Relationships: Connect the various files by setting up relationships using their respective primary and foreign keys.

5. Calculate Financial Metrics: Since management prioritizes understanding the total cost, retail value, and profit for product creation, add three new columns in the sales file:

Total Cost: Calculated as Total Cost = Units * Product Cost.

Total Retail: Calculated as Total Retail = Units * Product Price.

Profit: Calculated as Profit = Total Retail - Total Cost.

# Data Analysis:

To address the key questions, we developed an interactive dashboard to analyze sales and inventory data. This dashboard allows users to filter and explore data by store, city, product, or specific time periods, providing a comprehensive view of the company's performance across various dimensions.

## Analysis of "Toy Sales Overall Performance" Dashboard
The "Toy Sales Overall Performance" dashboard provides a comprehensive view of sales metrics, giving insight into total sales, monthly averages, peak season performance, and profitability. With total sales of $8.29M, the company maintains a strong monthly average of $690.91K. December is identified as the peak sales period, reaching $1.74M, likely due to holiday demand. The dashboard’s breakdown by product line shows that Classic Cars and Vintage Cars are the top contributors, driving $2.97M and $1.64M in sales, respectively. Regional sales data reveals that EMEA holds the largest market share at 49.77%, followed by North America with 38.35%. Customer insights highlight the Euro Shopping Channel as the top client with purchases amounting to $0.77M. Sales by day of the week demonstrate Friday as the most profitable, generating $1.81M. This information can aid in strategizing marketing efforts and stock allocation to maximize profitability and meet regional demand.

![Overall Performance](https://github.com/user-attachments/assets/7916b817-9890-46bd-9fd3-f9b9ae48b39c)

## Analysis of "Toy Sales Product Diversity Analysis" Dashboard
The "Toy Sales Product Diversity Analysis" dashboard emphasizes product variety and performance in relation to customer demand and regional popularity. With 99K units ordered, an average of 8.26K monthly orders, and a peak season sales volume of 1.74M, the dashboard highlights the scale of product movement. Classic Cars lead in quantity ordered across multiple years, reflecting consistent customer interest, followed by Vintage Cars and Motorcycles. Profitability analysis shows that the EMEA region yields the highest profit at $3.3M, showcasing its importance as a key market. North America follows with $1.1M, while APAC has lower profitability, indicating potential for targeted marketing. The quantity ordered status pie chart highlights 91K units as shipped, with minimal cancellations or disputes, underscoring effective inventory management. This dashboard is essential for understanding product performance and identifying trends across regions, enabling strategic product allocation and sales planning.

![Product Diversity](https://github.com/user-attachments/assets/49569715-c718-4422-b96b-85e51d7311e9)

## Analysis of "Geospatial Analysis" Dashboard
This dashboard, titled "Toy Sales Geospatial Analysis," provides a visual summary of toy sales data across different countries, broken down by region. Key performance indicators (KPIs) are highlighted at the top, showing total sales of $8.29 million, a profit of $2.90 million, sales in 19 countries, and 73 cities. The map displays sales by country, with bubble sizes indicating the volume of sales in each location. The data table on the right lists each region’s total sales and profit, with Spain, France, and the UK leading in the EMEA region. The USA has the highest sales and profit in the NA region, with $2.99 million in sales and over $1 million in profit. Interactive filters on the left allow users to view data by year, quarter, customer, branch, and status, enabling a customized view of sales trends. This dashboard provides a clear overview of sales distribution, profitability, and geographic performance.

![Geospatial Analysis](https://github.com/user-attachments/assets/c8cb2bb4-0f90-4b5f-b21a-449ee5abb782)

## Analysis of "Toy Sales Customer Segmentation" Dashboard
The "Toy Sales Customer Segmentation" dashboard offers insights into customer demographics, total sales, and profit distribution. With a customer base of 92, this dashboard displays the top and bottom-performing customers by revenue, providing a clear picture of customer loyalty and spending behavior. The Euro Shopping Channel emerges as the top customer with $0.77M in sales, while Microsale Inc. records the lowest at $28K, suggesting diverse customer engagement levels. Product line sales data shows Classic Cars as the most popular category, generating $2.97M, followed by Vintage Cars at $1.64M, indicating these as key areas for growth. Sales by day data reveal that Fridays yield the highest sales of $1.81M, while Tuesdays generate the lowest at $0.18M, which could inform promotional scheduling. This segmentation analysis aids in customer profiling, enabling personalized marketing strategies and product recommendations to enhance customer retention and maximize revenue.
![Customer profiling](https://github.com/user-attachments/assets/996fd319-fdb9-4083-b09d-552b1bfadd4f)

![Customer Segmention](https://github.com/user-attachments/assets/a4cdf176-ccfc-4f70-8d17-dfd80e5a11df)

# Key Recommendations 
## Key Findings:
a) Top Products: Classic cars and vintage cars drive significant revenue.

b) Sales Seasonality: November sees peak sales; there is a mid-year sales dip.

c)Regional Performance: EMEA is the highest-performing region, with NA showing growth potential.
Recommendations:

## Product Strategy
Prioritize inventory for high-demand products, create themed bundles, cross-promote low-performing items.

Low-Performing Products: For underperforming items like trains, consider discounting, price reductions, re-evaluating listings, and collecting customer feedback.
Seasonal Marketing Strategy:

Intensify marketing for holidays (October-November) with gift sets and themed discounts.
Boost off-peak sales (June-July) through discounts and loyalty incentives.

## Geographical Market Strategy:

Focus on the EMEA region with locally tailored ads.
Expand in NA with regional campaigns, influencer partnerships, and incentives.
Operational Improvements:

Optimize stock for peak demand, enhance supply chain efficiency, especially in EMEA and NA.

## Customer Engagement:

Implement a loyalty program and strengthen customer support during high-traffic periods.
Implementation Plan:

Short Term (0-3 months): Launch holiday campaigns and ensure inventory for top products.
Medium Term (3-6 months): Develop bundles, introduce a loyalty program, and expand promotional reach.
Long Term (6-12 months): Evaluate campaign success and consider market expansion.
Key Performance Indicators (KPIs):

Track sales growth, customer retention, market expansion success, and stock availability.


# Tools Used
Power BI: For dashboard creation and data visualization.
Python Programming (Plotly): For data cleaning and initial exploration.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
