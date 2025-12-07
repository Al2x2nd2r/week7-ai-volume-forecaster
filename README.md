# Volume Forecasting Analysis Report
## Statistical Patterns Discovered
### Trend Analysis
- I noticed the trend of a mild upward movement with linear growth.
- Daily growth rate: Approximately 0.351 units/day
- Significance: This indicates a slow but steady increase in volume over time. This could indicate an increase demand or growth in the business.

### Seasonal Patterns
1. **Weekly Pattern**: The highest days were Thursday (μ=1424), Wednesday (μ=1420), and Friday (μ=1422). The Lowest days were Sunday (μ=1313) and Satuday (μ=1321). This suggests a pattern where mid-week days preform better.
2. **Monthly Pattern**: I was unable to reach any solid conclusion for the monthly pattern. It's likely the aforementioned weekly pattern continues on throughout the year, rather than any certain month notably increasing or decreasing in growth.
3. **Yearly Pattern**: I was unable to reach any solid conclusion for the yearly pattern. As with the monthly pattern, it's likely the aforementioned weekly pattern continues on throughout the year, rather than any certain month notably increasing or decreasing in growth.

### Statistical Properties
- Mean: 1390.78 Units
- Standard Deviation: 192.38 Units
- Coefficient of Variation: 0.138

## Forecasting Methods Applied
### Moving Average
- Window size tested: 7 days
- Accuracy (MAE): 65.8921
- Pros: Simplicity and Smoothing of Data are the biggest pros when it comes to moving averages. They are easy to implement and understand, and the smoothing of data helps with any short-term fluctuation or noise allowing you to see the actual trend.
- Cons: However, there are some cons when it comes to moving averages. Since it averages out past data, it can be late to react to recent trends or any sudden changes. Another issue, as we saw, is that it doesnt cover seasonality well. I was unable to reach a conclusion on the monthly pattern because it cannot capture repeated/cyclical patterns effecitvely.

### Exponential Smoothing
- Alpha parameter: 0.3
- Accuracy (MAE): 71.9890
- Pros: Bceause exponential smoothing applies greater weight to newer data, exponential smoothing adjusts more quickly than moving averages. Exponential smoothing is also very easy to implement.
- Cons: Exponential smoothing still seems to ignore monthly/yearly patterns. Another downside is that the forecast accuracy seems to depend heavily on choosing the right Alpha.

## AI/ML Concepts Applied
### From Chapter 15:
1. **Temporal Reasoning**: The system uses past data patterns such as trends and weekly cycles to predict future values based on how the data has been evolving.
2. **Markov Assumption**: The data does not follow the Markov assumption because it predicts future values based off of several past observations, not just the most recent.
3. **Prediction Uncertainty**: Uncertainty is managed by tracking errors and smoothing out excess noise.

## Next Steps (Week 8 Preview)
- Implement ARIMA models
- Add machine learning algorithms
- Create 13-month forecast
- Build interactive Excel workbook

## Challenges Encountered
First, I struggled with getting statsmodel to import correctly, which required quite a bit of troubleshooting with the installation and dependancies. While I was trying to fix statsmodels, I managed to break my Python interpreter and had to create a new environment, reinstall my packages, and reconfigure the project. After fixing my environment and configuring it properly, I had to spend time restructuring the formatting and indentation of the code.

## Learning Reflections
I learned how important it is to have a properly configured stable environment and how easily dependancies can cause serious issues.