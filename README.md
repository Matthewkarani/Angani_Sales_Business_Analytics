# Toys Sales Analysis Using Power BI

#Project Overview

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

![Overall Performance](images/Overall Performance.jpg)
