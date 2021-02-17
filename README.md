# Predicting Year-over-Year Change in Foot Traffic during to COVID-19

### Tamar Novetsky, Alene Rhea, and Michael Stanley<br/>NYU Center for Data Science, Machine Learning, Spring 2020

The COVID-19 pandemic has transformed gathering sites into transmission sites. There is a new need to predict where people are gathering, in order to enforce social distancing, supply PPE, and establish guidelines and recommendations. The goal of this project is to predict changes in foot traffic to points of interest within key centers of the US pandemic.  

Specifically, we aim to predict the year-over-year change in weekly foot traffic for thousands of specific locations (e.g., individual stores, airports, etc.) based on the type of business, the timing of COVID-19 regulations in the area, the demographics and economy of the surrounding area, and the weather.  We have acquired 15 months of weekly foot traffic data for millions of locations in the US from SafeGraph.  We have incorporated a number of additional datasets to generate the feature set described above.  

Predicting change in foot traffic is a regression problem.  The primary focus is on prediction rather than interpretability, so we evaluate regression models over a range of complexity.  The data has a temporal aspect, as each week is considered a separate sample, and this temporality is considered when defining new features, as well as training, validation, and test sets.

We found xgboost to be the best performing model and that it generalizes well to the test set.  The xgboost model clearly outperformed the linear baseline, with 80% lower MAE on the validation set. A custom evaluation metric allows the model to be fairly robust to outliers. Feature importance analysis indicates that features from many different sources improved model performance.
