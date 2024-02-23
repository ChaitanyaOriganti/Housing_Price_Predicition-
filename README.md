## Predicting Housing Prices in King County, USA

### Introduction
Welcome to the repository for our comprehensive analysis of residential property sales in King County, USA, with a focus on Seattle. This dataset, spanning transactions from May 2014 to May 2015, offers valuable insights into the housing market with 21,614 entries. Our analysis aims to deepen understanding of factors influencing property prices through meticulous examination and visualization, unraveling patterns and providing actionable insights in King County's dynamic real estate landscape.

### Dataset Overview
The dataset includes key attributes such as:
- Identification (id)
- Transaction date (date)
- Price
- Bedrooms
- Bathrooms
- Living area (sqft_living)
- Lot size (sqft_lot)
- Floors
- Waterfront status
- View
- Property condition
- Grade
- Above-ground living area (sqft_above)
- Basement area (sqft_basement)
- Year built (yr_built)
- Year renovated (yr_renovated)
- Zip code (zipcode)
- Latitude (lat)
- Longitude (long)
- Living area in 2015 within the neighborhood (sqft_living15)
- Lot size in 2015 within the neighborhood (sqft_lot15)

### Objective
Our primary objective is to explore the predictive power of advanced machine learning algorithms in real estate valuation. We aim to assess and compare the effectiveness of these models in predicting house prices and categorizing houses into 'low_value' and 'high_value' based on specific criteria. Through this analysis, we seek to uncover the strengths and limitations of each model, providing valuable insights for homebuyers, sellers, and real estate professionals.

### Business Objectives
1. **Predict Housing Prices**: Accurately predict housing prices based on property features to empower informed decision-making.
2. **Categorize Houses**: Effectively categorize houses into 'low_value' and 'high_value' for quick decision-making by real estate professionals and investors.

### Tools & Techniques Used
- **Python**: Leveraging its data science libraries (Pandas, NumPy) for data manipulation and numerical operations.
- **Visualization**: Matplotlib and Seaborn for meaningful visualizations.
- **Machine Learning**: Scikit-learn for classification, regression, and ensemble learning.
- **Models Used**: Support Vector Regressor, Random Forest Regressor, Gradient Boosting Regressor, Neural Network Regression.
- **Interactive Analysis**: Jupyter Notebooks for interactive data exploration.
- **Dashboards**: Tableau for creating dynamic and visually appealing dashboards.
- **Preprocessing Techniques**: One-hot encoding for categorical variables, date transformation for temporal analysis, and standard scaling for numerical features.
- **Model Evaluation**: Train-test splitting for comprehensive model performance assessment on unseen data.

### Repository Structure
- **Data**: Contains the dataset `kc_house_data.csv`.
- **Notebooks**: Jupyter Notebooks for data preprocessing, exploratory data analysis, and modeling.
- **Scripts**: Python scripts for specific functions or tasks.
- **Visualizations**: Visualization outputs from Matplotlib, Seaborn, and Tableau.
- **Reports**: Final reports and analysis summaries.
