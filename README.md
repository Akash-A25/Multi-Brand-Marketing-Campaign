# Multi-Brand-Marketing-Campaign
Multi-Brand Marketing Campaign Performance Analysis and Prediction Using Python, and Machine Learning
# Multi-Brand Marketing Campaign Analysis & ROI Modeling

## 📌 Project Overview
This project consolidates, cleans, and analyzes marketing campaign data across three major cosmetics and beauty e-commerce platforms: **Nykaa**, **Purplle**, and **Tira**. 

The goal of this pipeline is to handle missing data through standard statistical imputation techniques, feature-engineer key performance indicators (KPIs) such as standard ROI, and construct binary classification targets (`Profit_Loss`) to enable predictive performance modeling.

---

## 📊 Dataset Summary
* **Total Cleaned Records:** 129,232 combined rows
* **Brands Included:** Nykaa, Purplle, Tira
* **Key Attributes Tracked:**
  * **Categorical:** Campaign Type, Target Audience, Channel Used, Language, Customer Segment
  * **Numerical:** Duration, Impressions, Clicks, Engagement Score, Leads, Conversions, Revenue, Acquisition Cost
  * **Engineered Targets:** ROI, Profit_Loss (`Profit` vs `Loss`)

---

## 🛠️ Data Cleaning & Processing Pipeline

### 1. Data Consolidation & Cleanup
* Merged campaign datasets from Nykaa, Purplle, and Tira into a unified dataframe.
* Removed unneeded metadata columns (`Campaign_ID`, `Date`).
* Reordered columns to prioritize `Company_Name`.
* Filtered out rows missing critical categorical dimensions (`Campaign_Type`, `Target_Audience`, `Channel_Used`, `Language`, `Customer_Segment`).

### 2. Missing Value Imputation Strategy
To preserve dataset integrity while minimizing bias, missing values were resolved using specific strategies:
* **Duration, Impressions, Clicks, Engagement Score:** Imputed using mean values and grouped channel averages.
* **Leads:** Estimated using the global Click-to-Lead conversion ratio (~38.02%).
* **Conversions:** Estimated using channel-grouped conversion ratios relative to total clicks/leads.
* **Acquisition Cost:** Imputed using grouped mean costs relative to campaign scope and channel.

### 3. Feature Engineering & Metric Standardisation
* **ROI Recalculation:** Standardized across all datasets using the unified formula:
  $$\text{ROI} = \frac{\text{Revenue} - \text{Acquisition Cost}}{\text{Acquisition Cost}}$$
* **Target Labeling (`Profit_Loss`):** Created a binary target feature:
  * `Profit`: $\text{ROI} > 0$
  * `Loss`: $\text{ROI} \le 0$

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed along with the following dependencies:

```bash
pip install pandas numpy matplotlib seaborn jupyter


```bash
pip install pandas numpy matplotlib seaborn jupyter
