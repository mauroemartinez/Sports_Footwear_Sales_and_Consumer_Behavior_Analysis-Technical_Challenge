# 👟 Sports Footwear Sales & Consumer Behavior Analysis

### [📊 View Dashboard Preview (GIF)](https://raw.githubusercontent.com/mauroemartinez/Sports_Footwear_Sales_and_Consumer_Behavior_Analysis-Technical_Challenge/main/Other%20Files/Preview.gif)
**Context:** Technical challenge for a BI Developer / Analytics Engineer position. This project demonstrates the integration of Python for data ingestion and advanced DAX for trend analysis.

<p align="center">
  <img src="https://raw.githubusercontent.com/mauroemartinez/Sports_Footwear_Sales_and_Consumer_Behavior_Analysis-Technical_Challenge/main/Other%20Files/Preview.gif" alt="Sports Footwear Dashboard Demo" width=85%>
</p>

**Stack:** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black) ![Power Query](https://img.shields.io/badge/Power_Query-217346?style=flat-square&logo=powerbi&logoColor=white) ![DAX](https://img.shields.io/badge/DAX-0176D3?style=flat-square&logo=microsoft&logoColor=white) ![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=Kaggle&logoColor=white)

## 📋 Executive Summary
This end-to-end BI solution analyzes global sales and consumer sentiment for the sports footwear industry. Using a dataset of ~900 models, the report identifies key drivers in revenue, customer satisfaction, and inventory needs across different global markets.

## ⚙️ Engineering & Technical Decisions
* **Automated Ingestion (`Python`):** Instead of static file loading, I implemented a Python script to fetch data directly from Kaggle. This ensures data integrity and allows for quarterly updates without manual downloads.
* **ETL & Dimensional Modeling (`Power Query`):** I performed the complete ETL process to transform a raw, flat dataset into a functional **Star Schema**. This involved normalizing dimensions (Products, Geography, Categories) to optimize cross-filtering performance and maintain data integrity.
* **Controlled Calendar Table:** Avoided `CALENDARAUTO()` to prevent file bloat and regain control over granularity. Built a custom `DAX Calendar` to manage 1:N relationships efficiently.
* **Advanced Time Intelligence:** Opted for a **3-Month Moving Average** over YTD to expose real seasonality peaks (Sept/Oct) by filtering out historical "noise".
* 
## 🧠 Strategic Business Insights
* **Revenue vs. Volume:** Germany leads in revenue despite lower sales volume compared to the USA and India, indicating a higher-margin market preference.
* **Market Diversification:** The Top 3 models represent less than 1% of total sales, showing a healthy, well-diversified portfolio across 899 models.
* **Satisfaction Segmentation:** 52% of customers rate their experience as "Good" or "Very Good." A critical insight: **Unisex products** flag a potential design or fit issue due to higher "Poor" ratings.
* **Customer Demographics:** Low-income segments contribute significantly (~$50M), proving strong brand penetration in mass-market tiers.

## 🎨 User Experience & Analytics Versatility
* **Dynamic Parameters:** Implemented Field Parameters for Metrics and Categories, allowing the "Overview" page to answer hundreds of questions within a single visual. You can make it only visible for the developers, so that they can go further in their analysis.
* **Insight-Driven Navigation:** Used Bookmarks to create a focused storytelling experience, preventing cognitive overload. It is intended for non-technical users, while technical ones can use the dynamic parameters.

## 🏗️ Data Model
The architecture follows a clean Star Schema, optimized through Power Query for efficient relationship management and calculation speed.

<p align="center">
  <img src="https://github.com/mauroemartinez/Sports_Footwear_Sales_and_Consumer_Behavior_Analysis-Technical_Challenge/blob/main/Other%20Files/Data%20Model.png" alt="Sports Footwear Data Model" width=90%>
</p>

---
**Focus:** Analytics Engineering | Data Modeling | Consumer Insights
