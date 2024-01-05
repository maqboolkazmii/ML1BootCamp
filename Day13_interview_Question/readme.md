The exploratory data analysis (EDA) reveals key insights into the dataset, encompassing 10,000 records and 164 features. Here's a summary of the findings and actions taken:

1. **Handling Missing Values:**
   - 26 columns had minimal (0.21%) null values, leading to the removal of rows with missing values.
   - A total of 21 records were dropped, maintaining data purity.

2. **Duplicate Records:**
   - No duplicate records were identified, ensuring data integrity.

3. **Date and Time Handling:**
   - A new 'time' column was created, retaining only time information, simplifying subsequent analyses.
   - we have find data is only of one day from 10:00 to 12:46 .
   - 'created' and 'id' columns were dropped.

4. **Boxplot Analysis:**
   - 'Price' feature exhibited no outliers.
   - Right-skewed 'price' distribution indicates concentration of lower-priced items with a tail of higher-priced items.

5. **Percentage Change (Pct_score):**
   - Pct_score values ranged from -0.0005 to 0.0005, signifying small stock price fluctuations.
   - Near-zero values indicate overall stability and low volatility.

6. **Seasonal Decomposition:**
   - Absence of trend in "seasonal" and "noise" components suggests a stable pattern.
   - Fluctuations in "residual" component between +25 and -25 indicate unexplained variations or noise.

7. **AutoCorrelation Function (ACF) Plot:**
   - Lack of data points towards -1 suggests minimal negative autocorrelation.
   - Current observations are not strongly influenced by immediately preceding negative observations.

8. **Partial Auto-Correlation Function (PACF) Plot:**
   - Two values between 0 and 1 indicate significant direct influences of past observations at those lags.
   - Small changes around 0 suggest negligible partial correlations with other lags.

9. **Rolling Mean and Standard Deviation:**
   - Constant values indicate data stationarity.
   - A stationary time series exhibits consistent statistical properties over time, providing stability for analysis and modeling.



**Linear Regression Model:**
- Applied linear regression resulted  99% accuracy.
- Ongoing fine-tuning and feature engineering can enhance the model's predictive capabilities.

This EDA provides valuable insights into stock price behavior. The stable dataset suggests potential for reliable predictions.

